# Homepage
- https://github.com/pi-hole/pi-hole

# Local network
- See in bitwarden

# Filters
- nelonenmedia-pmd-ads-spotgate.nm-stream.nelonenmedia.fi
- nelonenmedia-pmd-ads-manual.nm-stream.nelonenmedia.fi
- playback2.a2d.tv
- a-fds.youborafds01.com
- mask.icloud.com
  - Think this broke icloud apps
- log.core.cloud.vewd.com
- (\.|^)ingest\.sentry\.io$
- (\.|^)events\.data\.microsoft\.com$
- (\.|^)in\.applicationinsights\.azure\.com$
- optimizationguide-pa.googleapis.com
- (\.|^)exp-tas\.com$
- (\.|^)gstatic\.com$
  - This breaks google sign in
- (\.|^)fsapi\.com$
- (\.|^)hotjar\.com$

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
