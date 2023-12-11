# Using

## Underclocking gpu
- using powerlevel, for example RTX 3060 is xW / 170W
```bash
nvidia-smi --power-limit=150
```

# Installation
These requires NVidia developer account

- [Cuda toolkit](https://developer.nvidia.com/cuda-toolkit-archive)
- [Cudnn](https://developer.nvidia.com/cudnn)
    - [Nvidia instructions](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)

- Installer will fail if nouveau module loaded, but it will blaclist it and requires reboot after that. This would be nice to do in the OS setup directly.
- Installer also fails if any nvidia apt package is installed so all have to purged if any installed.

```bash
# packages that installer requires
sudo apt install build-essential libglvnd-dev pkg-config
sudo apt install linux-image-amd64 linux-source linux-headers-X.X.X
```

Using cuda 12.1 at the moment

```bash
# Installer(s)
# override cause gcc is too new (sample worked with deb packages)
# just select cuda, samples + docs (no driver as older, kernel-fs does not install/work)
sudo ./cuda_11.7.1_515.65.01_linux.run --override

# pytorch acceleration should work after cuda install

# download cudnn tar and extract to cudnn folder
# copy files and set permissions
sudo cp cudnn/include/cudnn* /usr/local/cuda/include
sudo cp cudnn/lib/libcudnn* /usr/local/cuda/lib64/
sudo chmod a+r /usr/local/cuda/include/cudnn* /usr/local/cuda/lib64/libcudnn*

# need to setup LD_LIBRARY_PATH to contain that folder we just copied libraries into
# (added to .bash_aliases)
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64/

# nvidia cudnn samples should work (need overrides to compile with new gcc)
```

## TensorRT
Someday maybe when can fullfill its python dependency, which is odd as I can have conda environent different python, think I just don't understand how to use this...
- [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/archives/index.html#trt_7)

## NVidia issues

### Regular system updates (apt)
Today I ran normal update and upgrade, after that nvidia-driver + cuda broke. This is bit odd
as I don't have any nvidia package installed via apt. But this was resolved by reinstalling cuda
using the same nvidia installer.

### Cuda
nvidia-smi might fail if theres is a mismatch between driver and library versions
this happens if newer driver is installed and the libraries are older. Something has
updated my nvidia driver so it is now incompatible with the installed cuda... (my fault ofc)

To check driver version
```bash
cat /proc/driver/nvidia/version
NVRM version: NVIDIA UNIX x86_64 Kernel Module  525.89.02  Wed Feb  1 23:23:25 UTC 2023
```

I first checked whats available on nvidia sites. Downloaded:
- cuda_12.1.0_530.30.02_linux.run
- cudnn-linux-x86_64-8.8.1.3_cuda12-archive.tar.xz

Next ran `/usr/local/cuda-11.7/bin/cuda-uninstaller`

`Successfully uninstalled`

Lets try installing the new one now again `cuda_12.1.0_530.30.02_linux.run`

Still complained about the persistence daemon, I might have to nuke the whole driver that is installed
by apt to use the driver which is part the cuda package, or test cuda without installing the driver
if it works with the current one. Driver I have installed is most likely too old to work so I am kinda
fucked.

Lets try just uninstalling `nvidia-driver nvidia-driver-bin nvidia-persistenced`

Running cuda installer again

```
The NVIDIA driver appears to have been installed previously using a different installer. To prevent potential conflicts, it is recommended either to update the existing installation using the same mechanism by which it was originally installed, or to uninstall the existing installation before installing this driver.
```

Basically I tried to uninstall just some packages with the name `nvidia` on em, tried keeping the i386 architecture
libraries to prevent Steam to break. But cuda installer won't install driver before all packages were removed from system
so basically easiest is to nuke all installed packages with `nvidia` in the name...

Then cuda installer runs thru
```
===========
= Summary =
===========

Driver:   Installed
Toolkit:  Installed in /usr/local/cuda-12.1/

Please make sure that
 -   PATH includes /usr/local/cuda-12.1/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-12.1/lib64, or, add /usr/local/cuda-12.1/lib64 to /etc/ld.so.conf and run ldconfig as root

To uninstall the CUDA Toolkit, run cuda-uninstaller in /usr/local/cuda-12.1/bin
To uninstall the NVIDIA Driver, run nvidia-uninstall
Logfile is /var/log/cuda-installer.log
```
I have already LD_LIBRARY_PATH set and installer makes symbolic link to it so its ok.

nvidia-smi works now again
```
Wed Mar 29 19:14:44 2023
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 530.30.02              Driver Version: 530.30.02    CUDA Version: 12.1     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                  Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf            Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3060         Off| 00000000:01:00.0 Off |                  N/A |
| 49%   45C    P0               36W / 170W|      0MiB / 12288MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
```

### cuDNN
So the cuda uninstaller removed old libraries so we can just copy new ones same way in place

```bash
sudo cp cudnn/include/cudnn* /usr/local/cuda/include
sudo cp cudnn/lib/libcudnn* /usr/local/cuda/lib64/
sudo chmod a+r /usr/local/cuda/include/cudnn* /usr/local/cuda/lib64/libcudnn*
# add lib path to LD_LIBRARY_PATH env variable (.bash_aliases)
```

### Tensor RT

```bash
tar xfvz TensorRT-8.6.0.12.Linux.x86_64-gnu.cuda-12.0.tar.gz
sudo cp -R TensorRT-8.6.0.12 /usr/local/
sudo ln -s /usr/local/TensorRT-8.6.0.12/ /usr/local/TensorRT
sudo chmod a+r /usr/local/TensorRT/bin/* /usr/local/TensorRT/include/* /usr/local/TensorRT/lib/*
# add lib path to LD_LIBRARY_PATH env variable (.bash_aliases) remember to restart shell -> conda

# Installation could be done just to home folder
# C++ samples seem to require some libs I don't have
# Should first to to run python samples in conda environment
```

#### Tensor RT to conda environment
cpXX == python version (current using 3.9)

In conda environment (tf)
```bash
python3 -m pip install /usr/local/TensorRT/python/tensorrt-8.6.0-cp39-none-linux_x86_64.whl
python3 -m pip install /usr/local/TensorRT/python/tensorrt_lean-8.6.0-cp39-none-linux_x86_64.whl
python3 -m pip install /usr/local/TensorRT/python/tensorrt_dispatch-8.6.0-cp39-none-linux_x86_64.whl

python3 -m pip install /usr/local/TensorRT/uff/uff-0.6.9-py2.py3-none-any.whl

python3 -m pip install /usr/local/TensorRT/graphsurgeon/graphsurgeon-0.4.6-py2.py3-none-any.whl
python3 -m pip install /usr/local/TensorRT/onnx_graphsurgeon/onnx_graphsurgeon-0.3.12-py2.py3-none-any.whl
```

### Shell setup
Using .bash_aliases setup atm
```bash
# nvidia -Cuda, -cuDNN, -TensorRT libs/binaries
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64/:/usr/local/TensorRT/lib
export PATH=$PATH:/usr/local/cuda/bin:/usr/local/TensorRT/bin
```

### Testing cuDNN
- Sample compiled and worked

### Testing PyTorch
Ran test in my earlier made conda environment
```python
import torch
print("is available: "+str(torch.cuda.is_available()))
print("device count: "+str(torch.cuda.device_count()))
print("current device: "+str(torch.cuda.current_device()))
print("device 0: "+str(torch.cuda.device(0)))
print("device(0) name: "+torch.cuda.get_device_name(0))
print("device(0) capability: "+str(torch.cuda.get_device_capability(0)))
print("device(0) properties: "+str(torch.cuda.get_device_properties(0)))
print("device(0) memory_allocated: "+str(torch.cuda.memory_allocated()))
print("device(0) memory_reserved: "+str(torch.cuda.memory_reserved()))

```
It works, im happy :D

### Testing Tensorflow
Recreated my tf environment again and it also works
```python
import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")
```
It works, im happy :D