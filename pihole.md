# Sites
- [Homepage](https://github.com/pi-hole/pi-hole)
- [Repo](https://github.com/pi-hole/pi-hole/#one-step-automated-install)

# Install
```bash
git clone --depth 1 https://github.com/pi-hole/pi-hole.git Pi-hole
cd "Pi-hole/automated install/"
sudo bash basic-install.sh
```

# config.txt
- Comment/disable audio
- Comment arm boost, so it won't overclock itself

# If using LAN
- You can disable services
  - wpa_supplicant.service
  - ...

```bash
# use to see what services are on
sudo systemctl status
# use top, then Shift+M to see what is using memory
top
# system should use under 1GB of memory when running...
```
# Local network
- See in bitwarden

# Teleporter
- Use settings Teleporter to backup and restore settings.

## Blacklist
- nelonenmedia-pmd-ads-spotgate.nm-stream.nelonenmedia.fi
- nelonenmedia-pmd-ads-manual.nm-stream.nelonenmedia.fi
- playback2.a2d.tv
- a-fds.youborafds01.com
- log.core.cloud.vewd.com
- optimizationguide-pa.googleapis.com

## Blacklist regex
- (\.|^)ingest\.sentry\.io$
- (\.|^)events\.data\.microsoft\.com$
- (\.|^)in\.applicationinsights\.azure\.com$
- (\.|^)exp-tas\.com$
- (\.|^)fsapi\.com$
- (\.|^)hotjar\.com$

## Whitelist regex
- (\.|^)mask\.icloud\.com$

# Set nmcli use myself as dns
```bash
nmcli connection modify eth0 ipv4.dns "127.0.0.1 9.9.9.9"
```

# Max DB days
```bash
sudo nano /etc/pihole/pihole-FTL.conf
# Add it
MAXDBDAYS=7
# Save and restart
sudo systemctl restart pihole-FTL.service
```
