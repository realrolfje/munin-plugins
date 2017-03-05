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
  
If you'd like to build a mikrotik plugin, start with inspecting the snmp values available.
You can find these with `snmpwalk -v 1 -c public 192.168.88.1` (for a default mikrotik).

**SNMP Trouble:** The scripts seem to fail on some systems where MIB files are missing to
translate the SNMP MIB strings to OiDs (snmp talk for: We can't translate cryptic MIB::id
strings into even more cryptic iso.2.3.1.2.3.5.3.2.1.4.1 notation).