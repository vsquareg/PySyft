# stdlib
from typing import Any
from typing import Dict
from typing import List
from typing import Union

# third party
from google.protobuf.reflection import GeneratedProtocolMessageType
import numpy as np
import torch as th

# relative
from .specialized_compressor import SpecializedCompressor
from .util import registered_compressors
from ...core.common.serde.serializable import Serializable
from ..common.serde.deserialize import _deserialize as deserialize
from ..common.serde.serializable import bind_protobuf
from ..common.serde.serialize import _serialize as serialize
from ...proto.core.tensor.tensor_pb2 import Tensor as Tensor_PB

@bind_protobuf
class CompressedTensor(th.Tensor, Serializable):
    """
    [Experimental: high-performace duet channel] compressed tensor stores the compression algorithms applied
    HpDT TODO: Should be moved into core -> tensor?
    HpDT TODO: Find better alternative for this.
    """
    @staticmethod
    def __new__(cls, child, compressors, *args, **kwargs):
        if 'core.tensor' in str(type(child)):
            child = th.Tensor(child.child)
        return super().__new__(cls, child, *args, **kwargs)

    def clone(self, *args, **kwargs):
        return CompressedTensor(self.child, self.compressors)

    def to(self, *args, **kwargs):
        new_obj = CompressedTensor([], self.compressors)
        tempTensor=super().to(*args, **kwargs)
        new_obj.data=tempTensor.data
        new_obj.requires_grad=tempTensor.requires_grad
        new_obj.refresh_child()
        return(new_obj)

    def __init__(self, child: th.Tensor, compressors: List[SpecializedCompressor] = []):
        if 'core.tensor' in str(type(child)):
            child = th.Tensor(child.child)
        th.Tensor.__init__(child)
        self.child = child
        self.requires_grad = child.requires_grad
        self.compressors = compressors
        if self.requires_grad:
            self.grad = child.grad
            self.compressed_grad = child.grad
        self.refresh_super_tensor()

    def compress_more(self, compressor):
        if getattr(CompressedTensor, "grad_compessor", False):
            if compressor.is_eligible(self.compressed_grad):
                self.compressed_grad = compressor.compress(self.compressed_grad)
                self.compressors.append(compressor)
        else:
            if compressor.is_eligible(self.child):
                self.child = compressor.compress(self.child)
                self.compressors.append(compressor)

    def decompress(self) -> th.Tensor:
        compressors = self.compressors.copy()
        decompressed = self.child
        decompressed_grad = self.compressed_grad
        while compressors:
            compressor = compressors.pop()
            if getattr(CompressedTensor, "grad_compessor", False):
                decompressed_grad = compressor.decompress(decompressed_grad)
            else:
                decompressed = compressor.decompress(decompressed)
        decompressed.requires_grad = self.requires_grad
        decompressed.grad = self.grad
        return decompressed

    def encode_compressors(self) -> np.ndarray:
        encoded_compressors = list()
        for compressor in self.compressors:
            encoded_compressors.append(registered_compressors[compressor])
        return np.array(encoded_compressors)

    def decode_and_attach_compressors(self, encoded):
        self.compressors = self.decode_compressors(encoded)

    def decode_compressors(self, encoded):
        compressors = []
        inv_registered_compressors = {v: k for k, v in registered_compressors.items()}
        for encoded_compressor in encoded:
            compressors.append(inv_registered_compressors[encoded_compressor])
        return compressors

    def refresh_child(self):
        compressed = self.data
        for compressor in self.compressors:
            compressed = compressor.compress(compressed)
        self.child = compressed

    def refresh_super_tensor(self):
        decompressed = self.decompress()
        self.data = decompressed
        self.grad = decompressed.grad

    def __repr__(self):
        return "CompressedTensor(%r, %r)" % (
            self.child,
            self.compressors,
        )

    def _object2proto(self) -> Tensor_PB:
        use_tensors = True
        arrays = [serialize(self.encode_compressors())]

        self.child.requires_grad = self.requires_grad
        self.child.grad = self.compressed_grad
        tensors = [serialize(self.child)]

        return Tensor_PB(
            obj_type='compressed',
            use_tensors=use_tensors,
            arrays=arrays,
            tensors=tensors,
            requires_grad=self.requires_grad,
        )

    @staticmethod
    def _proto2object(proto: Tensor_PB, return_compressed=False):
        child = [deserialize(tensor) for tensor in proto.tensors]
        child = child[0]

        res = CompressedTensor(child, [])

        encoded_compressors = [deserialize(array) for array in proto.arrays]
        res.decode_and_attach_compressors(encoded_compressors)
        res.refresh_super_tensor()

        return res

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        return Tensor_PB