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
  - Note, Cuda + TensorRT uses 16GB+ space (more than base system + kde)
- /var (nginx, postgresql)
- /home (mostly everything is here)

## Swap
- For hibernation 1,5 x RAM
  - i.e. 1,5 * 64GB = 96GB
- No swap if running Redis
  - Any amount can mess it up
- TODO: Heard there is some benefit having 1GB swap on large ram systems, can't remember about it

## Encryption (laptop)
- /dev/sda1 512MB EFI (bootable)
- /dev/sda2 512MB /boot ext2
- /dev/sda3 dm-crypt (physical device for encryption)
  - LVM Volume group on sda3_crypt, volumes
    - /
    - swap
    - /home

I made this because it required to have EFI & /boot unencrypted. There I guess is a way to store them also inside the dm-crypt device.

- TODO: Figure out how to store LUKS headers and what else to open device in different machine
- TODO: Figure out how you could reinstall diff distro on encrypted setup

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
sudo apt install git git-lfs make gcc tcl libssl-dev libsystemd-dev libc6 libgcc-s1 libstdc++6 zlib1g ca-certificates apt-transport-https libfreeimage3 libfreeimage-dev curl
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

# ONLY NVidia driver
Install directly from debian repo
```bash
sudo apt update
sudo apt install linux-image-amd64 nvidia-driver firmware-misc-nonfree
```

If nvidia-smi works then good to go.

# NVidia driver & Cuda & cuDNN
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

# Nginx
```bash
sudo apt install nginx-full
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
## Teams
Set package source
```bash
# this seems to be the correct one
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/ms-teams stable main" > /etc/apt/sources.list.d/teams.list'

# but all sources are zero so it has been used but somehow wiped content...
# 13-Nov-2023 16:08 all files from repo have been wiped
sudo apt update
sudo apt install teams
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

# iPhone
```bash
# required tools
sudo apt install libimobiledevice6 libimobiledevice-utils ifuse

# mounting device
# make folder
sudo mkdir /media/iPhone
chown -R antti:antti /media/iPhone
ifuse /media/iPhone
```

# Bose quietcomfort 35
## Getting mic to work with bluetooth
- modify file `/etc/pulse/default.pa`
```conf
# modify line
load-module module-bluetooth-policy
# to
load-module module-bluetooth-policy auto_switch=2
```
- restart pulseaudio & xServer

# Webcam
```bash
sudo apt install cheese
```

# Sound Blaster
- Most likely package: `firmware-misc-nonfree` has to be installed
    - sound blaster has dsp
- I also downloaded [latest alsa-firmware](https://www.alsa-project.org/)
    - configure, compile, install
    - most likely useless and system already has this installed
- Install `alsa-utils` to get alsamixer where you can see devices and configure them
- Install `pavucontrol` to configure pulseaudio in kde, pulseaudio runs on top of alsa

## Pavucontrol / Pulse audio control
Configuration tab should include the device, when here you select profile it resets all settings
which you can see in alsamixer (So after you get it working selecting new profile will break it).

![Pulse audio configuration tab](./pavucontrol.png)

## Alsamixer
This is the tricky part as by default, I guess only optical is on as I did not hear any sound before accidentally hitting settings that made sound come out of the headphone/lineout jack.

Pressing `m` you can enable/disable settings. When you see green `00` letters it means its on, `MM` means it's off. Here is a screenshot of the working settings (with all sound FX disabled).

![Alsamixer settings](./alsamixer.png)

# Node/npm
```bash
sudo apt install nodejs npm
```

# Steam
***STEAM ACTUALLY RUNS EVEN THO UNINSTALLED ALL NVIDIA PACKAGES*** so on other machine installed debian nvidia driver, dependencies and got steam running. Purged all nvidia packages (including driver) to install driver using cuda installer, steam still runs after that.

Has lot's of dependencies which be installed in progress, especially if no gnome installed from distro, but still there will be packages for sure.

```bash
# steam requires 32-bit libraries
sudo dpkg --add-architecture i386

# Download installer https://store.steampowered.com/about/download

sudo dpkg -i steam_latest.deb

# might need to fix install
sudo apt --fix-broken install

# run steam, should install if something still needed
# after this you can install nvidia cuda, cudnn & tensort...
```
