# IPV6
- What is ipv6? It's a protocol for sending packets over the internet.
- How it different from ipv4? It's newer and has more addresses.
- Why do we disable it? Because it's not compatible with our use case.

## Disable ipv6

```bash
sudo nano /etc/sysctl.conf
```

```ini
# Add these lines into the end
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```
