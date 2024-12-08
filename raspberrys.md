# Get OS
- https://www.raspberrypi.com/software/

Currently using the 64-bit versions as both later ones are version 4

Write the OS image using DD
```bash
sudo dd if=2024-11-19-raspios-bookworm-arm64-lite.img of=/dev/sdd status=progress && sync
umount /dev/sdd # for safety
```

Then just bootup

# SSHD
sudo raspi-config
- Setup hostname
- Enable SSH

# Setting static network
```bash
sudo nmcli c mod "Wired connection 1" ipv4.addresses 192.168.1.1/24 ipv4.method manual
sudo nmcli c mod "Wired connection 1" ipv4.gateway 192.168.1.254
sudo nmcli c mod "Wired connection 1" ipv4.dns "9.9.9.9,8.8.8.8"
```


# Rename device
```bash
sudo nmcli connection modify "Wired connection 1" connection.id "eth0"
sudo nmcli connection modify "Local" connection.id "lo"
```
