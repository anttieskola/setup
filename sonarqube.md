# SonarQube downloading

1. [Download community edition](https://www.sonarsource.com/products/sonarqube/downloads/)

- Firewall

```bash
sudo ufw allow 5432/tcp
sudo ufw allow 9000/tcp
sudo ufw allow 9001/tcp
sudo ufw reload
```

## Setup

1. Set SONAR_HOME to the installation directory
2. Set PATH to include SONAR_HOME/bin

```bash
# add into .bash_aliases

# export java home
 Add/modify SONAR_HOME and PATH
export SONAR_HOME=/usr/local/sonarqube
export PATH=$PATH:$SONAR_HOME/bin/linux-x86-64
```

### Configuration database

Current postgresql 17 configure file location `/etc/postgresql/17/main/`
These default settings (not sure did I add them or not) in `pg_hba.conf` seems to allow local system users to login without password (peer authentication).

```ini
# Sonarqube
local   sonarqube   sonaruser   md5

# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   all             all                                     peer
```

```bash
# restart postgresql
sudo systemctl restart postgresql
```

```bash
psql
# create user and database
CREATE ROLE <your_postgres_username> WITH LOGIN PASSWORD '<your_postgres_password>';
CREATE DATABASE sonarqube OWNER <your_postgres_username>;
# test
psql -U <your_postgres_username> -d <your_database_name>
```

```bash
# test sonarqube user login with tcp
psql -U sonaruser -d sonarqube -h localhost -W
```

```bash
# adding password if config was wrong
sudo -u postgres psql
# list users
\du

```

Then edit the file `sonar.properties` in `conf` directory.

```properties
sonar.jdbc.username=<your_postgres_username>
sonar.jdbc.password=<your_postgres_password>
sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
```

Then there are two parts that run JVM, for these I doubled the memory sizes.

Then there is extra feature called `vm.max_map_count` is strictly about the count of memory mappings, not their size. Its value is simply an integer representing the maximum number of virtual memory areas (VMAs) a process can have, regardless of how much memory each mapping consumes.

Elastic search what sonarqube uses, requires this to be set to 262144. Default is 65,535. On Debian default is 65530.

```bash
# check current value
sudo sysctl vm.max_map_count

# set it temporarily
sudo sysctl -w vm.max_map_count=262144

# permanent setting
sudo nano /etc/sysctl.conf

# Amount of memory maps for thread (Elastic search requires)
vm.max_map_count=262144

# same place we have this for dotnet
# DotNet requires lot of these as it has lot of change followers
fs.inotify.max_user_instances = 1024
```

#### Systemd

```bash
sudo nano /etc/systemd/system/sonarqube.service
```

```ini
# /etc/systemd/system/sonarqube.service

# install
# sudo systemctl daemon-reload
# sudo systemctl enable sonarqube.service
# sudo systemctl start sonarqube.service

# removal
# sudo systemctl stop sonarqube.service
# sudo systemctl disable sonarqube.service
# remove the service file
# reload daemon

# full log you can see with
# journalctl -u sonarqube.service

[Unit]
Description=sonarqube.service
After=network.target

[Unit]
Description=SonarQube Service
After=network.target

[Service]
Type=forking
Restart=always
WorkingDirectory=/usr/local/sonarqube/bin/linux-x86-64
ExecStart=/usr/local/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/usr/local/sonarqube/bin/linux-x86-64/sonar.sh stop
User=antti
Group=antti

# Environment setup for Sonar
Environment="SONAR_JAVA_PATH=/usr/local/java/bin/java"
Environment="SONAR_HOME=/usr/local/bin/sonarqube"
Environment="PATH=/usr/local/java/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/sonarqube/bin/linux-x86-64"

TimeoutStartSec=300
TimeoutStopSec=120

SyslogIdentifier=sonarqube.service
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable sonarqube.service
sudo systemctl start sonarqube.service
```
