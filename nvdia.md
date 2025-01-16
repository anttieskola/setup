
# Simple installation notes
- Downloading latest cuda driver `cuda_12.3.1_545.23.08_linux.run`
- Downloading latest cuDNN `cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz`
    - Extract into cudnn folder
- There is no TensorRT for Cuda 12.3 atm

## Own install cmd
```bash
sudo ~/cuda_12.6.3/cuda_12.6.3_560.35.05_linux.run --silent --driver --toolkit --override
```

## Cuda installer options
- [Cuda installer docs](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/)

Silent Installation

--silent

Required for any silent installation. Performs an installation with no further user-input and minimal command-line output based on the options provided below. Silent installations are useful for scripting the installation of CUDA. Using this option implies acceptance of the EULA. The following flags can be used to customize the actions taken during installation. At least one of --driver, --uninstall, and --toolkit must be passed if running with non-root permissions.

--driver

Install the CUDA Driver.

--toolkit

Install the CUDA Toolkit.

--toolkitpath=<path>

Install the CUDA Toolkit to the <path> directory. If not provided, the default path of /usr/local/cuda-12.6 is used.

--defaultroot=<path>

Install libraries to the <path> directory. If the <path> is not provided, then the default path of your distribution is used. This only applies to the libraries installed outside of the CUDA Toolkit path.

Extraction

--extract=<path>

Extracts to the <path> the following: the driver runfile, the raw files of the toolkit to <path>.

This is especially useful when one wants to install the driver using one or more of the command-line options provided by the driver installer which are not exposed in this installer.

Overriding Installation Checks

--override

Ignores compiler, third-party library, and toolkit detection checks which would prevent the CUDA Toolkit from installing.

No OpenGL Libraries

--no-opengl-libs

Prevents the driver installation from installing NVIDIA’s GL libraries. Useful for systems where the display is driven by a non-NVIDIA GPU. In such systems, NVIDIA’s GL libraries could prevent X from loading properly.

No man pages

--no-man-page

Do not install the man pages under /usr/share/man.

Overriding Kernel Source

--kernel-source-path=<path>

Tells the driver installation to use <path> as the kernel source directory when building the NVIDIA kernel module. Required for systems where the kernel source is installed to a non-standard location.

Running nvidia-xconfig

--run-nvidia-xconfig

Tells the driver installation to run nvidia-xconfig to update the system X configuration file so that the NVIDIA X driver is used. The pre-existing X configuration file will be backed up.

No nvidia-drm kernel module

--no-drm

Do not install the nvidia-drm kernel module. This option should only be used to work around failures to build or install the nvidia-drm kernel module on systems that do not need the provided features.

Custom Temporary Directory Selection

--tmpdir=<path>

Performs any temporary actions within <path> instead of /tmp. Useful in cases where /tmp cannot be used (doesn’t exist, is full, is mounted with ‘noexec’, etc.).

Kernel Module Build Directory

--kernel-module-build-directory=<kernel|kernel-open>

Tells the driver installation to use legacy or open flavor of kernel source when building the NVIDIA kernel module. The kernel-open flavor is only supported on Turing GPUs and newer.

-m=kernel

Tells the driver installation to use legacy flavor of kernel source when building the NVIDIA kernel module. Shorthand for --kernel-module-build-directory=kernel

m=kernel-open

Tells the driver installation to use open flavor of kernel source when building the NVIDIA kernel module. The kernel-open flavor is only supported on Turing GPUs and newer. Shorthand for --kernel-module-build-directory=kernel-open

## Cuda installer - uninstaller

```bash
sudo /usr/local/cuda-12.6/bin/cuda-uninstaller
```

## Bug
- https://lists.debian.org/debian-stable-announce/2024/02/msg00002.html

Gotta update sources.list
```
deb http://deb.debian.org/debian/ bookworm-updates main non-free contrib non-free-firmware
deb-src http://deb.debian.org/debian/ bookworm-updates main non-free contrib non-free-firmware
```
Then can install latest kernel so compilation works

## Underclocking gpu
- using powerlevel, for example RTX 3060 is xW / 170W
```bash
sudo cp cudnn/include/cudnn* /usr/local/cuda/include
sudo cp cudnn/lib/libcudnn* /usr/local/cuda/lib64/
sudo chmod a+r /usr/local/cuda/include/cudnn* /usr/local/cuda/lib64/libcudnn*
```

## TensorRT (latest 8.6.1.6)
Most likely will not work (as no support for latest Cuda)
```bash
tar xfvz TensorRT-8.6.1.6.Linux.x86_64-gnu.cuda-12.0.tar.gz
sudo cp -R TensorRT-8.6.1.6 /usr/local/
sudo ln -s /usr/local/TensorRT-8.6.0.12/ /usr/local/TensorRT
sudo chmod a+r /usr/local/TensorRT/bin/* /usr/local/TensorRT/include/* /usr/local/TensorRT/lib/*
```

## Library paths
Current set these in .bash_aliases
```bash
# nvidia -Cuda, -cuDNN, -TensorRT libs/binaries
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64/:/usr/local/TensorRT/lib
export PATH=$PATH:/usr/local/cuda/bin:/usr/local/TensorRT/bin

```

# Underclocking gpu

## RTX 4060TI is x / 165W
```bash
nvidia-smi --power-limit=120
```

## RTX 3060 is xW / 170W
```bash
nvidia-smi --power-limit=120
```

# Old Installation notes
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