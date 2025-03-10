# Bulding llama.cpp

1. Clean (if build before)

```bash
rm -rf build
```

2. Configure

This is for my rig 2 x 4060TI 16G.

```bash
# Configure
cmake -B build -DGGML_CUDA=ON -DGGML_CUDA_F16=ON -DCMAKE_CUDA_ARCHITECTURES=89 -DGGML_CCACHE=OFF


# Build
cmake --build build -j12
```
