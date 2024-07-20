# Prerequisites
- nginx installed and works

# Akonadi fix (prevents mariadb installation on debian 12+)

## stop
```
akonadictl stop
rm -Rf $XDG_CONFIG_HOME/akonadi
rm -Rf $XDG_DATA_HOME/akonadi
rm -Rf $XDG_CONFIG_HOME/akonadi*
rm -Rf $XDG_DATA_HOME/akonadi*
```

## edit config
nano $HOME/.config/akonadi/akonadiserverrc

```
[%General]
Driver=QMYSQL
To:

[%General]
Driver=QSQLITE
```

## start
```
akonadictl start
```

# Install packages
```
sudo apt install php-fpm
sudo apt install php-curl php-gd php-intl php-mbstring php-soap php-xml php-xmlrpc php-zip
# mariadb
sudo apt install mariadb-server
# mysql
sudo apt install php-mysql
```

# Restart php service
```
sudo systemctl status php* | grep fpm.service
sudo systemctl restart php8.2-fpm
```

# Nginx config
```
server {
    listen 80;
    server_name wp.zeus.com;
    root /var/www/wp;
    index index.php;
    location / {
        try_files $uri $uri/ =404;
    }
    location = /favicon.ico {
        log_not_found off; access_log off;
    }
    location = /robots.txt {
        log_not_found off; access_log off; allow all;
    }
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php-fpm.sock;
    }
    location ~* \.(css|gif|ico|jpeg|jpg|js|png)$ {
        expires max;
        log_not_found off;
    }
}
```

# Test PHP on nginx
- Use this script as info.php
```php
<?php
phpinfo();
?>
```

# Maria DB configuration
```
sudo mysql_secure_installation

# Setup root password
# Access all questions using default values
# Remove anonymous users
# Disallow root login remotely
# Remove test database
# Reload privilege tables
```

## Create user and database
```
sudo mariadb
```

```sql
CREATE DATABASE wordpress DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

CREATE USER 'USER_NAME_HERE'@'localhost' IDENTIFIED BY 'PASSWORD_HERE';
GRANT ALL ON wordpress.* TO 'USER_NAME_HERE'@'localhost';
FLUSH PRIVILEGES;
```

# Wordpress installation
- Download wordpress
```
curl -o wordpress-6.5.3.tar.gz https://wordpress.org/wordpress-6.5.3.tar.gz
```
- Extract to x and copy content from wordpress folder to webroot

- Copy example config
```
cp wp-config-sample.php wp-config.php
```

# Configuration
Creating secrets for instance
```
curl -s https://api.wordpress.org/secret-key/1.1/salt/
```

- replace content in wp-config.php with the output
- set database name, user and password
- add

```php
/** Direct file access.... */
define('FS_METHOD', 'direct');
```

# Max file upload size
- nginx `/etc/nginx/sites-available/default`
    - in server block `client_max_body_size 500M;`

- php.ini `/etc/php/8.2/fpm/php.ini`
    - `post_max_size = 500M`
    - `upload_max_filesize = 500M`

- wordpress `wp-config.php`
    - `define('WP_MEMORY_LIMIT', '256M');`

# Permissions
- Direct file access so that wordpress can update itself
```
sudo chown -R www-data:www-data *
```

# Plugin to export/install/backup whole site
- [All in one WP migration](https://fi.wordpress.org/plugins/all-in-one-wp-migration/)
