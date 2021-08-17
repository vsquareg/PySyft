from .sparse_compressor import SparseCompressor

registered_compressors = {
    SparseCompressor: 1,
}

named_compressors = {
    'SparseCompressor': SparseCompressor,
}