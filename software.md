# Software I use
Note that you can install Flatpak applications for user only or all users.
They are available many times thru many different routes. Some have APT packages, some don't. Some have flatpak, some AppImages or eveything.

I want to use stabile versions, but with some you have to choose the correct distribution format to get the best version to use.

Only use VLC as APT.

All software I use usually is only open source.

## Remove all wrong source installs
```bash
# Openshot, Gimp, Blender, PrusaSlicer
sudo apt remove --purge openshot-qt -y && \
sudo apt remove --purge gimp -y && \
sudo apt remove --purge blender -y && \
sudo apt remove --purge prusa-slicer -y
```

## VLC - Video player
```bash
sudo apt install vlc -y
```

## Install flatpak and flathub
```bash
sudo apt update
sudo apt install flatpak -y
sudo flatpak --system remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

### Install all apps from flathub
```bash
sudo flatpak install flathub org.blender.Blender -y && \
sudo flatpak install flathub org.gimp.GIMP -y && \
sudo flatpak install flathub org.prusa-labs.PrusaSlicer -y
```
## Blender - 3D modeling
[homepage](https://www.blender.org/)

## GIMP - Image editor
[Homepage](https://www.gimp.org/)

## PrusaSlicer - 3D printer slicer
[Homepage](https://www.prusa3d.com/prusaslicer/)

## OpenShot - Video editor
[Homepage](https://www.openshot.org/)
Use only **AppImage**, never install APT/Flatpak package, as it is so old version.
- Download AppImage from [OpenShot](https://www.openshot.org/download/)
