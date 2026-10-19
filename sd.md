# Stable Diffusion

## Building

```bash

# Web frontend build
cd examples/server/frontend
pnpm install

# Binaries
mkdir build && cd build
cmake -DSD_CUDA=ON -DSD_SERVER_BUILD_FRONTEND=ON
cmake --build . --config Release -j 12
```