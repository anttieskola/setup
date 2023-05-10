# Nginx

## Installation
```bash
sudo apt install nginx-full
```

## Redirect http to https
Configure to the site (running only one site atm)

```
server {
        listen 80 default_server;
        server_name _;
        return 301 https://$host$request_uri;
}
```

## Gzip
Configured gzip compression for x-javascript and assembly in `nginx.conf`
```
##
        # Gzip Settings
        ##

        gzip on;
        gzip_vary on;
        gzip_proxied any;
        gzip_comp_level 6;
        gzip_buffers 16 8k;
        gzip_http_version 1.1;
        gzip_types text/plain text/css application/json application/javascript application/x-javascript text/xml application/wasm application/xml application/xml+rss text/javascript;
```
This reduces webassembly sizes up to half of original :)
