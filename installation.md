# DistroHop / Fresh install
- Notes for myself when installing or updating some nix box
- Current environment bookworm on Debian & Raspberry Pi OS

# Table of Contents
- [DistroHop / Fresh install](#distrohop--fresh-install)
  - [General](#general)
  - [Partitioning used](#partitioning-used)
  - [Swap](#swap)
  - [Encryption (laptop)](#encryption-laptop)
- [User: antti](#user-antti)
- [Login/Boot method](#loginboot-method)
  - [Console login](#console-login)
  - [Graphical login](#graphical-login)
- [Basic stuff](#basic-stuff)
- [Kernel stuff](#kernel-stuff)
- [AMD](#amd)
- [ONLY NVidia driver](#only-nvidia-driver)
- [flatpak](#flatpak)
- [System state - disable all but hibernate](#system-state---disable-all-but-hibernate)
- [System state - disable all](#system-state---disable-all)
- [Bluetooth](#bluetooth)
- [Sensors](#sensors)
- [Keyring](#keyring)
- [Nginx](#nginx)
- [Rust](#rust)
- [C#](#c)
  - [INotify](#inotify)
- [Python](#python)
- [Bitwarden](#bitwarden)
- [Microsoft signing key](#microsoft-signing-key)
  - [VSCode](#vscode)
  - [Edge](#edge)
  - [Teams](#teams)
- [Spotify](#spotify)
- [RSync](#rsync)
- [iPhone](#iphone)
- [Bose quietcomfort 35](#bose-quietcomfort-35)
  - [Getting mic to work with bluetooth](#getting-mic-to-work-with-bluetooth)
- [Pulseaudio](#pulseaudio)
- [Webcam](#webcam)
- [Sound Blaster](#sound-blaster)
  - [Pavucontrol / Pulse audio control](#pavucontrol--pulse-audio-control)
  - [Alsamixer](#alsamixer)
- [Node/npm](#nodenpm)
- [Steam](#steam)
- [Must have apps](#must-have-apps)
  - [VLC](#vlc)
  - [Screenshots](#screenshots)
  - [OBS Recording/Streaming](#obs-recordingstreaming)
  - [Gimp (image editor)](#gimp-image-editor)
  - [Blender](#blender)
  - [PrusaSlicer](#prusaslicer)
  - [Openshot (video editor)](#openshot-video-editor)
  - [Tor Browser](#tor-browser)
  - [Kleopatra (GPG)](#kleopatra-gpg)

# Other notes
- [cpu.md](./cpu.md)
- [crypt.md](./crypt.md)
- [crypt_fs.md](./crypt_fs.md)
- [firewall.md](./firewall.md)
- [git.md](./git.md)
- [kde.md](./kde.md)
- [kubernetes.md](./kubernetes.md)
- [letsencrypt.md](./letsencrypt.md)
- [nginx.md](./nginx.md)
- [nmcli.md](./nmcli.md)
- [nvdia.md](./nvdia.md)
- [other/moving_boot.md](./other/moving_boot.md)
- [other/networkmanager.md](./other/networkmanager.md)
- [other/new_zeus.md](./other/new_zeus.md)
- [pihole.md](./pihole.md)
- [postgresql.md](./postgresql.md)
- [raspberrys.md](./raspberrys.md)
- [README.md](./README.md)
- [redis.md](./redis.md)
- [samba.md](./samba.md)
- [ssh.md](./ssh.md)
- [utilities.md](./utilities.md)
- [wordpress.md](./wordpress.md)
- [neofetch.md](./neofetch.md)

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
sudo apt install git git-lfs make gcc tcl libssl-dev libsystemd-dev libc6 libgcc-s1 libstdc++6 zlib1g ca-certificates apt-transport-https libfreeimage3 libfreeimage-dev curl cpulimit neofetch smartmontools
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
- [See these instructions for AI/Cuda stuff](./nvidia.md)

Installation directly from debian repo (won't work with AI/Cuda stuff)
```bash
sudo apt update
sudo apt install linux-image-amd64 nvidia-driver firmware-misc-nonfree
```

# flatpak
- Lot of software is available in flatpak
```bash
# install flatpak
sudo apt install flatpak
# add flathub repo
flatpak --user remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

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

## INotify
Can add the following to `.bash_aliases` to prevent all config file watching
```bash
export DOTNET_USE_POLLING_FILE_WATCHER=true
```

Can add the following to `/etc/sysctl.conf` increase the limit of amount files to be watched
```bash
fs.inotify.max_user_watches=524288
```

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
Client is now better than browser, but check always first instructions from below.
- Check [instructions(https://www.spotify.com/nl/download/linux/)]

Signing key
```bash
curl -sS https://download.spotify.com/debian/pubkey_C85668DF69375001.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg
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
sudo mkdir /media/iphone
chown -R antti:antti /media/iphone
ifuse /media/iphone

# unmount
fusermount -u /media/iphone
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

# Pulseaudio
- [Pulseaudio systemtray](https://github.com/christophgysin/pasystray)
- List available sources
```bash
pactl list sources
```

Example
```
Source #8
        State: IDLE
        Name: bluez_sink.2C_41_A1_07_F9_20.a2dp_sink.monitor
        Description: Monitor of Bose QC Antti
        Driver: module-bluez5-device.c
        Sample Specification: s16le 2ch 44100Hz
        Channel Map: front-left,front-right
        Owner Module: 25
        Mute: no
        Volume: front-left: 65536 / 100% / 0.00 dB,   front-right: 65536 / 100% / 0.00 dB
                balance 0.00
        Base Volume: 65536 / 100% / 0.00 dB
        Monitor of Sink: bluez_sink.2C_41_A1_07_F9_20.a2dp_sink
        Latency: 0 usec, configured 39512 usec
        Flags: DECIBEL_VOLUME LATENCY
        Properties:
                device.description = "Monitor of Bose QC Antti"
                device.class = "monitor"
                device.string = "2C:41:A1:07:F9:20"
                device.api = "bluez"
                device.bus = "bluetooth"
                device.form_factor = "headphone"
                bluez.path = "/org/bluez/hci0/dev_2C_41_A1_07_F9_20"
                bluez.class = "0x240418"
                bluez.alias = "Bose QC Antti"
                device.icon_name = "audio-headphones-bluetooth"
        Formats:
                pcm
```



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

# Must have apps

## VLC
```bash
sudo apt install vlc
```

## Screenshots
```bash
sudo apt install kde-spectacle
```

## OBS Recording/Streaming
```bash
sudo apt install obs-studio
```

## Gimp (image editor)
This will fix issues with heif files with the latest iPhone

1. Remove GIMP if installed from apt
````bash
sudo apt remove gimp
sudo apt autoremove
````

2. Install latest from flatpak
````bash
flatpak install https://flathub.org/repo/appstream/org.gimp.GIMP.flatpakref
````

3. Install backport (updated version of libheif)
````bash
sudo apt install -t bookworm-backports libheif1
````

## Blender
```bash
flatpak install flathub org.blender.Blender
```

## PrusaSlicer
```bash
flatpak install flathub com.prusa3d.PrusaSlicer
```

## Openshot (video editor)
```bash
sudo apt install openshot-qt
```

## Tor Browser
```bash
sudo apt install torbrowser-launcher
```

## Kleopatra (GPG)
```bash
sudo apt install kleopatra
```
