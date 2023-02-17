# KDE
Notes about issue or things aboud KDE, currently running the latest Plasma.

## Issues

### Locale issue
It seems that KDE/QT supports locales that are not compatible with the rest of the OS (Debian11). There is a nice locale en_FI.UTF-8 which would be using english language but finnish in date, currency... other formats.

This is nice but this breaks everything without setting them separately outside KDE, so it just seems much easier to not use them.

KDE-Plasma locale configuration are found in ~/.config/plasma-localerc

There is also GUI to set these up
