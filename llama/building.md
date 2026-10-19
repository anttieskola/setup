# Bulding llama.cpp

1. Clean (if build before)

```bash
rm -rf build
```

2. Configure

This is for my rig 2 x 4060TI 16G.

```bash
# Configure
cmake -B build -DGGML_CUDA=ON  -DGGML_CUDA_FA_QUANTS="all" -DCMAKE_CUDA_ARCHITECTURES=89

# Build
cmake --build build -j12
```

This is for my older rig.

```bash
# Configure
cmake -B build -DGGML_CUDA=ON  -DGGML_CUDA_FA_QUANTS="all" -DCMAKE_CUDA_ARCHITECTURES=86

# Build
cmake --build build -j12
```
