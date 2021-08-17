# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/tensor/tensor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.adp import entity_pb2 as proto_dot_core_dot_adp_dot_entity__pb2
from syft.proto.lib.numpy import array_pb2 as proto_dot_lib_dot_numpy_dot_array__pb2
from syft.proto.lib.torch import tensor_pb2 as proto_dot_lib_dot_torch_dot_tensor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/core/tensor/tensor.proto',
  package='syft.core.tensor',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eproto/core/tensor/tensor.proto\x12\x10syft.core.tensor\x1a\x1bproto/core/adp/entity.proto\x1a\x1bproto/lib/numpy/array.proto\x1a\x1cproto/lib/torch/tensor.proto\"\xd7\x01\n\x06Tensor\x12\x10\n\x08obj_type\x18\x02 \x01(\t\x12*\n\x06\x65ntity\x18\x03 \x01(\x0b\x32\x15.syft.core.adp.EntityH\x00\x88\x01\x01\x12\x13\n\x0buse_tensors\x18\x04 \x01(\x08\x12*\n\x06\x61rrays\x18\x05 \x03(\x0b\x32\x1a.syft.lib.numpy.NumpyProto\x12,\n\x07tensors\x18\x06 \x03(\x0b\x32\x1b.syft.lib.torch.TensorProto\x12\x15\n\rrequires_grad\x18\x07 \x01(\x08\x42\t\n\x07_entityb\x06proto3'
  ,
  dependencies=[proto_dot_core_dot_adp_dot_entity__pb2.DESCRIPTOR,proto_dot_lib_dot_numpy_dot_array__pb2.DESCRIPTOR,proto_dot_lib_dot_torch_dot_tensor__pb2.DESCRIPTOR,])




_TENSOR = _descriptor.Descriptor(
  name='Tensor',
  full_name='syft.core.tensor.Tensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='obj_type', full_name='syft.core.tensor.Tensor.obj_type', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity', full_name='syft.core.tensor.Tensor.entity', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_tensors', full_name='syft.core.tensor.Tensor.use_tensors', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arrays', full_name='syft.core.tensor.Tensor.arrays', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tensors', full_name='syft.core.tensor.Tensor.tensors', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requires_grad', full_name='syft.core.tensor.Tensor.requires_grad', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_entity', full_name='syft.core.tensor.Tensor._entity',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=141,
  serialized_end=356,
)

_TENSOR.fields_by_name['entity'].message_type = proto_dot_core_dot_adp_dot_entity__pb2._ENTITY
_TENSOR.fields_by_name['arrays'].message_type = proto_dot_lib_dot_numpy_dot_array__pb2._NUMPYPROTO
_TENSOR.fields_by_name['tensors'].message_type = proto_dot_lib_dot_torch_dot_tensor__pb2._TENSORPROTO
_TENSOR.oneofs_by_name['_entity'].fields.append(
  _TENSOR.fields_by_name['entity'])
_TENSOR.fields_by_name['entity'].containing_oneof = _TENSOR.oneofs_by_name['_entity']
DESCRIPTOR.message_types_by_name['Tensor'] = _TENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), {
  'DESCRIPTOR' : _TENSOR,
  '__module__' : 'proto.core.tensor.tensor_pb2'
  # @@protoc_insertion_point(class_scope:syft.core.tensor.Tensor)
  })
_sym_db.RegisterMessage(Tensor)


# @@protoc_insertion_point(module_scope)
