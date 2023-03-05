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

# Basic stuuf
```bash
sudo apt install git make gcc tcl libssl-dev libsystemd-dev libc6 libgcc-s1 libstdc++6 zlib1g ca-certificates apt-transport-https libfreeimage3 libfreeimage-dev
```

# AMD
- use isenkram to install any missing firmware
```bash
sudo apt install isenkram
sudo isenkram-autoinstall-firmware
```

# Nvidia
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

## Cuda & cuDNN
(This requires developer account)
- [Cuda toolkit](https://developer.nvidia.com/cuda-toolkit-archive)
- [Cudnn](https://developer.nvidia.com/cudnn)
  - [Nvidia instructions](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)

Using 11.8 at the moment (pytorch)

```bash
sudo dpkg -i cuda-repo-debian11-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo cp /var/cuda-repo-debian11-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/

sudo dpkg -i cudnn-local-repo-debian11-8.8.0.121_1.0-1_amd64.deb
sudo cp /var/cudnn-local-repo-debian11-8.8.0.121/cudnn-local-*-keyring.gpg /usr/share/keyrings/

sudo apt update

sudo apt install cuda libcudnn8 libcudnn8-dev libcudnn8-samples

# Run the sample to verify all works
```

## TensorRT
Someday maybe when can fullfill its python dependency, which is odd as I can have conda environent different python, think I just don't understand how to use this...
- [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/archives/index.html#trt_7)


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
# Steam
Has lot's of dependencies which be installed in progress, especially if no gnome installed from distro, but still there will be packages for sure.

Download: https://store.steampowered.com/about/download

```bash
# steam requires 32-bit libraries
sudo dpkg --add-architecture i386
# it should not remove any existing ones...
sudo dpkg -i steam_latest.deb
sudo apt --fix-broken install
# run steam from cmd line should run steamdeps with sudo
# for some reason the dependant packages want to uninstall
# my installed cuda libraries...
# so one post in SO says if you install it using the installer
# instead .deb package it should work...
# guess i could try, just uninstall them and try installing
# using installer...
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
