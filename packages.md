# Partitioning (if not done ofc...)
- /dev/sda1 500MB EFI
- /dev/sda2 500MB EXT2 /boot
- /dev/sda3 crypt (dm-crypt)
  - LVM Volume group (lvmg1)
    - swap: <swap> 124GB (for possible hibernation...)
    - root: ext4 / 124GB
    - home: ext4 /home *

# User should be
id: 1000
gid: 1000

# AMD Firmware
For firmware use: isenkram

# Nvidia driver
First need to add: contrib non-free
To /etc/apt/sources.list installation source (deb)

update
nvidia-driver firmware-misc-nonfree

# Disable sleep, suspend...
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target

# Bluetooth
bluez bluetooth

# Sensors
hddtemp hddtempd lm-sensors psensor

# Samba
Configuration: /etc/samba/smb.conf
Set passwords for users using: smbpasswd

# C/C++ and dependencies to rest
make gcc tcl libssl-dev libsystemd-dev libc6 libgcc1 libgssapi-krb5-2 libicu67 libssl1.1 libstdc++6 zlib1g ca-certificates apt-transport-https

# Rust
curl --proto '=https' --tlsv1.3 -sSf https://sh.rustup.rs | sh

# C#
installed in home/path

# Python
autoremove python2
python3 python3-pip

# MS Key
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/
sudo rm microsoft.gpg

## VSCode
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'

update
code # or code-insiders

## Edge beta (every 4 week)
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-beta.list'

update
microsoft-edge-beta

## Edge dev (every week)
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list'

update
microsoft-edge-dev

# Spotify...no font scaling :(
curl -sS https://download.spotify.com/debian/pubkey_7A3A762FAFD4A51F.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg

echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list

update
spotify-client

# Steam
download latest package
dpkg -i steam_latest.deb
