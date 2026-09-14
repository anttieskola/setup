# Using PI coding agent
- [Homepage](https://pi.dev/)

## Setup

- Run agent in debian WSL for simplicity
  - So you can basically have studio/code opened with the solution same time
- Uses my own llama.cpp server, see [models.json](./agent/models.json)



## What models I want to use

- https://unsloth.ai/docs/models/qwen3.6
- https://unsloth.ai/docs/models/qwen3.8


### Qwen 3.8 - 27B

- Can run Qwen3.8-27B-UD-IQ3_XXS.gguf, with context 262144 => 23 tokens/s (max context)
- Can run Qwen3.8-27B-UD-IQ4_XS.gguf, with context 200192 => 18 tokens/s
- Can run Qwen3.8-27B-UD-Q4_K_S.gguf, with context 200192 => 13 tokens/s

```bash
#!/bin/bash

# This is optimized for Qwen3.8 27B Unsloth 3.0 dynamic models
# with my rig with 2 x 16GB max context, 23 token/s

SERVER="/usr/local/llama.cpp/llama-server"
MODELS="/mnt/artemis1/models-server"

$SERVER \
	--host 0.0.0.0 --port 8080 -t 12 \
	--temp 0.9 --top-p 0.90 --top-k 20 --min-p 0.0 \
	--presence-penalty 0.0 --repeat-penalty 1.0 \
	--reasoning-effort medium \
	--spec-draft-n-max 2 \
	-fit off \
	-ngl all \
	-c 262144 \
	--no-slots \
	--models-max 1 \
	--models-dir $MODELS
```
