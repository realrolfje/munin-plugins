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
- Install snmpget with `sudo apt-get install snmp`
- Install the MIB downloader with `sudo apt-get install snmp-mibs-downloader`. You need
  this to make the snmpget tool in the scripts able to translate the human-readable MIB
  strings into those awful snmp v2 iso OiD strings.
- Add your MikroTik to the `/etc/hosts` file so you can refer to it with a nice name:
  `192.168.88.1 mymikrotik`
- Add the network name of the MikroTik to your symlink, like so:
  `ln -s <githubrepo>/plugins/mikrotikcpu_ /etc/munin/plugins/mikrotikcpu_mymikrotik`
  
If you'd like to build a mikrotik plugin, start with inspecting the snmp values available.
You can find these with `snmpwalk -v 1 -c public 192.168.88.1` (for a default mikrotik).


Mattermost
----------
Mattermost plugins provide more information about your local mattermost installation than
the provided mattermost statistics page. Stuff you really want to know, like number of
posts per second, number of users, number of channels.

To make these plugins work, you need the following configuration in the
`/etc/munin/plugin-conf.d/munin-node` configuration file:

```
[mattermost*]
user root
```

This can probably be changed to the `mattermost` user (or whichever user has access
to your postgresql database, but that requires rework of the plugins.