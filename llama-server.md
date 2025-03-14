# llama.cpp

Do all this in the console, without X11 or Wayland running.
Preqrequisites cmake (apt package) and cuda installed/installler.
Latest cuda installer found in [NVIDIA CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive)
Example

```bash
# download
wget https://developer.download.nvidia.com/compute/cuda/12.8.0/local_installers/cuda_12.8.0_570.86.10_linux.run
# make it executable
chmod +x cuda_12.8.0_570.86.10_linux.run
# create silent runner script for it, seen below
```

```bash
# if earlier version of cuda is installed, remove it
sudo /usr/local/cuda/bin/cuda-uninstaller

# install cuda 12.6.3
#!/bin/bash
sudo ./cuda_12.6.3_560.35.05_linux.run --override --silent --driver --toolkit
```

## Build

```bash

# clone
git clone <https://github.com/ggml-org/llama.cpp>
# cd to the directory
cd llama.cpp

# confgure for CUDA and half precision
cmake -B build -DGGML_CUDA=ON -DGGML_CUDA_F16=ON
cmake --build build --config Release
```

### Install build binaries

```bash
sudo mkdir /usr/local/bin/llama
sudo cp build/* /usr/local/bin/llama
chown -R antti:antti /usr/local/bin/llama
```

### Service file (/etc/systemd/system/llama-server.service)

```ini
# copy: /etc/systemd/system/llama-server.service

# install
# sudo systemctl daemon-reload
# sudo systemctl enable llama-server.service
# sudo systemctl start llama-server.service

# removal
# sudo systemctl stop llama-server.service
# sudo systemctl disable llama-server.service
# remove the service file
# reload daemon

# full log you can see with
# journalctl -u llama.service

[Unit]
Description=llama-server
After=network.target

[Service]
Type=simple
Restart=always
User=antti

# Environment setup for cuda
Environment="PATH=/home/antti/bin:/usr/local/bin:/usr/bin:/bin"
Environment="LD_LIBRARY_PATH=/usr/local/cuda/lib64"

# Note working directory is a must
# otherwiser process can't find resources -> odd errors
WorkingDirectory=/usr/local/llama
ExecStart=/home/antti/bin/llama-server

StandardOutput=journal
StandardError=journal
SyslogIdentifier=llama-server

[Install]
WantedBy=multi-user.target

```

##### Script to start the service (/home/antti/bin/llama-server)

```bash
#!/bin/bash

# define models
model_0="mistral-7b-openorca.Q8_0.gguf" # template:chatml, old one used in aje analyzer
model_1="FuseO1-DeepSeekR1-QwQ-32B-Preview-Q5_K_M.gguf"
model_2="deepseek-r1-qwen-2.5-32B-ablated-Q5_K_L.gguf"
model_3="Qwen2.5-32B-DeepSeek-R1-Instruct.Q5_K_M.gguf"
model_4="deepseek-coder-33b-instruct-Q5_K_M.gguf"

# select model
model=$model_2

# select chat template
chat_template=""

# Current llama.cpp supported chat templates, it can also read it from models metadata
# (update this, as it is been developed) Last update 2025-02-03
W
# chatglm3, chatglm4, chatml, command-r, deepseek, deepseek2, deepseek3,
# exaone3, falcon3, gemma, gigachat, granite, llama2, llama2-sys,
# llama2-sys-bos, llama2-sys-strip, llama3, megrez, minicpm, mistral-v1,
# mistral-v3, mistral-v3-tekken, mistral-v7, monarch, openchat, orion,
# phi3, phi4, rwkv-world, vicuna, vicuna-orca, zephyr

#locations
models_dir="/home/models/"
# server path (compile and copy binaries)
llama_server="/usr/local/llama/llama-server"

#hots settings
hostname=$(hostname)
port=8080

#model settings
thread_cpu=11
thread_gpu=128
context_size=10240 # too big most likely to old models?

# set extra_params
extra_params=""

# set chat_template_param
if [ -n "$chat_template" ]; then
   echo -e "\e[32m#### Using chat template: $chat_template \e[0m"
   extra_params+=" --chat-template=$chat_template"
fi

# show selected model
echo -e "\e[32m#### Selected model: $model \e[0m"

# crate full path to model
model_full_path=$models_dir
model_full_path+=$model

# startup checks and execute
if [ ! -d $models_dir ]; then
  # no models_dir
  echo -e "\e[31m#### Models dir: $models_dir, does not exist! \e[0m"
elif [ ! -f $model_full_path ]; then
  # no model in models_dir
  echo -e "\e[31m#### Model file in: $model_full_path, does not exist! \e[0m"
else
  # start server
  echo -e "\e[34m#### Starting server http://$hostname:$port \e[0m"
  sleep 3
  $llama_server \
    --host 0.0.0.0 --port 8080 \
    -t $thread_cpu -ngl $thread_gpu \
    -c $context_size \
    -m $model_full_path \
    $extra_params
fi
```

# VSCodium + llama-vscode extension

One of laptop I have VSCodium installed, and I for fun installed llama-vscode extension to it. To my suprsise, it works just by setting the end point into my own llama.cpp server running on zeus. I am currently
sitting here next to the server, and it is working. I can hear the fans of the server spinning. Almost all this text is generated by the model.