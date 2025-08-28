# Kernel related notes

## Grud defaults

/etc/default/grub

```ini
GRUB_CMDLINE_LINUX_DEFAULT="modprobe.blacklist=nouveau net.ifnames=0 bios.devname=0"
```

- prevent nouveau from loading, so can use nvidia drivers
- disable stupid new network interface names
  - to fix dhcp modify /etc/network/interfaces, restart networking (sudo systemctl restart networking)

## Debian 13 - issues

- Have not succeeded to use nvidia driver with kernel, bookworm kernel still works

## GTX 5060 issues

- Need grub options 'acpi=off' to boot
