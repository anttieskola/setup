# DistroHop / Fresh install
Notes for myself when installing or updating some nix box.
Current environment bookworm beta2.

## General
- Use LVM if unsure on sizes

## Partitioning used
- 512MB EFI (bootable)
- 512MB EXT2 /boot
- swap if used
- / (root) 16GB...128GB
  - space requirement depends whats required to run and other partitions
- /var (nginx, postgresql)
- /home (mostly everything is here)

## Swap
- For hibernation 1,5 x RAM
  - i.e. 1,5 * 64GB = 96GB
- No swap if running Redis
  - Any amount can mess it up
- TODO: Heard there is some benefit having 1GB swap on large ram systems, can't remember about it

## Encryption
This setup seemed pretty good I managed to make on debian 11
- /dev/sda1 512MB EFI (bootable)
- /dev/sda2 512MB /boot ext2
- /dev/sda3 dm-crypt
- /dev/sda3 crypto
  - LVM Volume group on sda3_crypt, volumes
    - /
    - swap
    - /home

I made this because it required to have EFI & /boot unencrypted. There I guess is a way to store them also inside the dm-crypt device.

- TODO: Figure out how to store LUKS headers and what else to open device in different machine
- TODO: Figure out how you could reinstall diff distro on encrypted setup
- TODO: Figure out best encryption setup for laptop

# User: antti
Should have
- id: 1000
- gid: 1000

# Login/Boot method
Console login
```bash
sudo systemctl set-default multi-user.target
sudo systemctl reboot
```

Graphical login
```bash
sudo systemctl set-default graphical.target
sudo systemctl reboot
```

# Basic stuff
```bash
sudo apt install git make gcc tcl libssl-dev libsystemd-dev libc6 libgcc-s1 libstdc++6 zlib1g ca-certificates apt-transport-https libfreeimage3 libfreeimage-dev
```

# Kernel stuff
```bash
sudo apt install linux-image-amd64 linux-headers-amd64 linux-source
```

# AMD
- use isenkram to install any missing firmware
```bash
sudo apt install isenkram
sudo isenkram-autoinstall-firmware
```

# Nvidia driver only (rest after steam)
Just need to blacklist nouveau (driver installer does this, but would be nice to blacklist it during installation). Then without installing anything can run cuda installer.

Helper tools
```bash
sudo apt install nvidia-detect inxi
```

Driver is easiest to install from debian repo, just add/check: contrib non-free are present in /etc/apt/sources.list installation source distro

```bash
sudo apt update
sudo apt install linux-image-amd64 nvidia-driver firmware-misc-nonfree
```

Harder way is from downloading from NVidia directly, it worked out of the box
in bullseye but not in bookworm.

```bash
sudo apt install build-essential libglvnd-dev pkg-config 
sudo apt install linux-image-amd64 linux-source linux-headers-X.X.X
sudo ./NVidi....
```

It nvidia-smi works then good to go.
(Remember CUDA version is just what the driver supports)

# Steam
Has lot's of dependencies which be installed in progress, especially if no gnome installed from distro, but still there will be packages for sure.

```bash
# steam requires 32-bit libraries
sudo dpkg --add-architecture i386

# install some steam dependencies first
sudo apt install gcc-12-base:i386 i965-va-driver:i386 intel-media-va-driver:i386 libaom3:i386 libasound2:i386 libasound2-plugins:i386 libasyncns0:i386 libatomic1:i386 libavcodec59:i386 libavutil57:i386 libblkid1:i386 libbrotli1:i386 libbsd0:i386 libcairo-gobject2:i386 libcairo2:i386 libcap2:i386 libcodec2-1.0:i386 libcrypt1:i386 libcuda1:i386 libdatrie1:i386 libdav1d6:i386 libdb5.3:i386 libdbus-1-3:i386 libdecor-0-0:i386 libdecor-0-plugin-1-cairo:i386 libdeflate0:i386 libdrm-amdgpu1:i386 libdrm-intel1:i386 libdrm-nouveau2:i386 libdrm-radeon1:i386 libdrm2:i386 libedit2:i386 libegl-mesa0:i386 libegl-nvidia0:i386 libelf1:i386 libexpat1:i386 libffi8:i386 libflac12:i386 libfontconfig1:i386 libfreetype6:i386 libfribidi0:i386 libgcc-s1:i386 libgcrypt20:i386 libgdk-pixbuf-2.0-0:i386 libgl1-nvidia-glvnd-glx:i386 libglapi-mesa:i386 libgles-nvidia1:i386 libgles-nvidia2:i386 libgles1:i386 libgles2:i386 libglib2.0-0:i386 libglvnd0:i386 libglx-mesa0:i386 libglx-nvidia0:i386 libglx0:i386 libgmp10:i386 libgnutls30:i386 libgomp1:i386 libgpg-error-l10n libgpg-error0:i386 libgraphite2-3:i386 libgsm1:i386 libharfbuzz0b:i386 libhogweed6:i386 libhwy1:i386 libicu72:i386 libidn2-0:i386 libigdgmm12:i386 libjack-jackd2-0:i386 libjbig0:i386 libjpeg62-turbo:i386 libjxl0.7:i386 liblcms2-2:i386 liblerc4:i386 libllvm15:i386 liblz4-1:i386 liblzma5:i386 libmd0:i386 libmount1:i386 libmp3lame0:i386 libmpg123-0:i386 libnettle8:i386 libnm0:i386 libnuma1:i386 libnvcuvid1:i386 libnvidia-allocator1:i386 libnvidia-egl-gbm1:i386 libnvidia-eglcore:i386 libnvidia-encode1:i386 libnvidia-glcore:i386 libnvidia-glvkspirv:i386 libnvidia-ptxjitcompiler1:i386 libogg0:i386 libopengl0:i386 libopenjp2-7:i386 libopus0:i386 libp11-kit0:i386 libpango-1.0-0:i386 libpangocairo-1.0-0:i386 libpangoft2-1.0-0:i386 libpciaccess0:i386 libpcre2-8-0:i386 libpixman-1-0:i386 libpng16-16:i386 libpulse0:i386 librav1e0:i386 librsvg2-2:i386 librsvg2-common:i386 libsamplerate0:i386 libsdl2-2.0-0:i386 libselinux1:i386 libsensors5:i386 libshine3:i386 libsnappy1v5:i386 libsndfile1:i386 libsoxr0:i386 libspeex1:i386 libspeexdsp1:i386 libstdc++6:i386 libsvtav1enc1:i386 libswresample4:i386 libsystemd0:i386 libtasn1-6:i386 libthai0:i386 libtheora0:i386 libtiff6:i386 libtinfo6:i386 libtwolame0:i386 libudev1:i386 libunistring2:i386 libutempter0 libva-drm2:i386 libva-glx2 libva-glx2:i386 libva-x11-2:i386 libva2:i386 libvdpau-va-gl1:i386 libvdpau1:i386 libvorbis0a:i386 libvorbisenc2:i386 libvpx7:i386 libvulkan1:i386 libwayland-client0:i386 libwayland-cursor0:i386 libwayland-egl1:i386 libwayland-server0:i386 libwebp7:i386 libwebpmux3:i386 libx11-6 libx11-6:i386 libx11-data libx11-dev libx11-xcb1 libx11-xcb1:i386 libx264-164:i386 libx265-199:i386 libxau6:i386 libxcb-dri2-0:i386 libxcb-dri3-0:i386 libxcb-glx0:i386 libxcb-present0:i386 libxcb-randr0:i386 libxcb-render0:i386 libxcb-shm0:i386 libxcb-sync1:i386 libxcb-xfixes0:i386 libxcb1:i386 libxcursor1:i386 libxdamage1:i386 libxdmcp6:i386 libxext6:i386 libxfixes3:i386 libxi6:i386 libxinerama1:i386 libxkbcommon0:i386 libxml2:i386 libxrandr2:i386 libxrender1:i386 libxshmfence1:i386 libxss1:i386 libxvidcore4:i386 libxxf86vm1:i386 libz3-4:i386 libzstd1:i386 libzvbi0:i386 mesa-va-drivers:i386 mesa-vdpau-drivers:i386 mesa-vulkan-drivers:i386 nvidia-egl-icd:i386 nvidia-vulkan-icd:i386 ocl-icd-libopencl1 ocl-icd-libopencl1:i386 steam-devices steam-libs:i386 va-driver-all:i386 vdpau-driver-all:i386 zlib1g:i386

# Download installer https://store.steampowered.com/about/download

sudo dpkg -i steam_latest.deb

# might need to fix install
sudo apt --fix-broken install

# run steam, should install if something still needed
# after this you can install nvidia cuda, cudnn & tensort...
```

# NVidia Cuda & cuDNN
These requires developer account, after steam install most likely
.deb packages won't work but use the installers instead.

- [Cuda toolkit](https://developer.nvidia.com/cuda-toolkit-archive)
- [Cudnn](https://developer.nvidia.com/cudnn)
  - [Nvidia instructions](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)

** USE THE INSTALLER AND TAR PACKAGES NOT DEB(s) **
** CUDA INSTALLER HAS DRIVER ALSO, BETTER TO USE THAT (remove OS one) **
** STEAM ACTUALLY RUNS EVEN THO UNINSTALLED ALL NVIDIA PACKAGES **

Using 12.1 at the moment
~~Using 11.8 at the moment (pytorch)~~

```bash
# Deb(s)
sudo dpkg -i cuda-repo-debian11-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo cp /var/cuda-repo-debian11-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/

sudo dpkg -i cudnn-local-repo-debian11-8.8.0.121_1.0-1_amd64.deb
sudo cp /var/cudnn-local-repo-debian11-8.8.0.121/cudnn-local-*-keyring.gpg /usr/share/keyrings/

sudo apt update

sudo apt install cuda libcudnn8 libcudnn8-dev libcudnn8-samples

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

# System state - disable all but hibernate
```bash
sudo systemctl mask sleep.target suspend.target hybrid-sleep.target
```
# System state - disable all
```bash
# keep hibernate.target
sudo systemctl mask sleep.target suspend.target  hybrid-sleep.target
```

# Bluetooth
```bash
sudo apt install bluez bluetooth
```
# Sensors
```bash
sudo apt install lm-sensors psensor
```

# Keyring
```bash
sudo apt install gnome-keyring libqt5keychain1
```

# Rust
No need if using home backup where it is installed
```bash
curl --proto '=https' --tlsv1.3 -sSf https://sh.rustup.rs | sh
```

# C#
Installed in home/path (backup), just recreate symlink dotnet -> dotnetX

# Python
```bash
# not found in bookworm anymore
# sudo apt autoremove python2
```

```bash
sudo apt install python3 python3-pip
sudo apt install python3-numpy python3-torch
```

# Bitwarden
Download: https://bitwarden.com/download/
```bash
sudo dpkg -i Bitwarden-XXX-amd64.deb
```

# Microsoft signing key
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/
rm microsoft.gpg
```

## VSCode
Set package source
```bash
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
```
Install either
```bash
sudo apt install code
```
```bash
sudo apt install code-insiders
```

## Edge
Set package source
```bash
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-beta.list'
```

Beta updates every 4 weeks, dev every week.
Install either
```bash
sudo apt install microsoft-edge-beta
```
```bash
sudo apt install microsoft-edge-dev
```

# Spotify
Current version has no font scaling so its kinda useless, better to use browser at the moment.

Signing key
```bash
curl -sS https://download.spotify.com/debian/pubkey_7A3A762FAFD4A51F.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg
```

Package source
```bash
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
```

```bash
sudo apt install spotify-client
```

# RSync
Use rsync to copy/move stuff between hosts
```bash
# a == archive mode; equals -rlptgoD
# v == verbose
# r == recursive
rsync -av Downloads/* antti@god:~/Downloads/
```