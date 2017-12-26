JSON alerts for Munin
=====================

To get munin to send json to your alert script:

Copy `alerts.conf` to `/etc/munin/munin-conf.d/alerts.conf`.
Copy `alert.py` to `/etc/munin/scripts/alert.py`. 

Make sure both files are owned by the `munin` user and `alert.py` is executable.

Test `alert.py` with: `sudo -u munin /usr/share/munin/munin-limits --force`. You should
see output which looks like:

```
WARNING: monitor.local Logged in users: pts=4.00
OK: monitor.local Inode usage in percent
OK: monitor.local eth0 errors
OK: monitor.local File table usage
OK: monitor.local Disk usage in percent
OK: monitor.local routerboard CPU usage
OK: monitor.local Disk latency per device :: Average latency for /dev/mmcblk0
```

Step one is complete. You now have access to munin alerts inside a proper python script.
Alerts can be sent from there.
