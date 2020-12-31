# UPS_Battery_Monitor
Python module for py3status to monitor my UPS battery status

## Dependencies
This module requires that you have already setup your UPS, and just want to get the status.
It also assumes that you've named it "battery". If you've named it something else you can 
change it in the module itself.

## Usage
Add the module to your list of configured py3status modules

*~/.config/i3status.conf
```bash
...
order += "arch_updates"
order += "battery_status"
order += "volume_status"
...

```
And then just restart your i3 session.
