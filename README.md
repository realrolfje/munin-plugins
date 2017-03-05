munin-plugins
=============

Munin Plugins for stuff I use.


MikroTik
--------
The MikroTik plugins are based on the ones listed on the
[MikroTik wiki](https://wiki.mikrotik.com/wiki/Munin_Monitoring). The ones on the MikroTik
wiki use perl, which makes them too slow and resource hungry for the raspberry pi. My
versions use bash, awk and snmpget, which all run fast on the pi.

*To get the MikroTik plugins working:*
- Install snpget with `sudo apt-get install snmp`
- Add your MikroTik to the `/etc/hosts` file so you can refer to it with a nice name:
  `192.168.88.1 mymikrotik`
- Add the network name of the MikroTik to your symlink, like so:
  `ln -s <githubrepo>/plugins/mikrotikcpu_ /etc/munin/plugins/mikrotikcpu_mymikrotik`