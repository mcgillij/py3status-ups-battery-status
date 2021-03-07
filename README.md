# py3status-ups-battery-status
Python module for py3status to monitor my UPS battery status

## Screenshot
![py3status-ups-batter-status](https://raw.githubusercontent.com/mcgillij/py3status-ups-battery-status/main/images/ups_battery_status.png)

## Installation

### From Git
``` bash
git clone https://github.com/mcgillij/py3status-ups-battery-status.git
mkdir -p ~/.i3/py3status && cd ~/.i3/py3status
ln -s <PATH_TO_CLONED_REPO>/src/py3status-ups-battery-status/ups-battery-status.py ./
```

### Building From AUR (Arch)
``` bash
git clone https://aur.archlinux.org/py3status-ups-battery-status.git
cd py3status-ups-battery-status
makechrootpkg -c -r $HOME/$CHROOT
```

### Installing Arch package
``` bash
sudo pacman -U --asdeps py3status-ups-battery-status-*-any.pkg.tar.zst
```

## Dependencies

This module depends on the Network UPS Tools(nut) package. And having already configured your battery with it.
It assumes that you've named your battery *battery*. If you've named it something else you can change it in the module itself.

Dependency installation on Arch:
``` bash
pacman -S nut
```

Dependency installation on Debian:
``` bash
apt install nut
```

## Usage
Add the module to your list of configured py3status modules

*~/.config/i3status.conf*
``` bash
...
order += "arch_updates"
order += "volume_status"
order += "ups_battery_status"
...

```

And then just restart your i3 session.
