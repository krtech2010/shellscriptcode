#!/usr/bin/env python
import os
import time
import sys
m = os.popen('''sar -q -o cpuusage.file 1 60 > /dev/null 2>&1''')
m.close()
n = os.popen('''sar -f cpuusage.file | grep -vEi "CPU|reboot|average" | awk NR{'print int($4+$5+$6+$7+$8)'} | paste -s -d"+" | bc''')
n1 = n.read()
n.close()
o = os.popen('''rm -f cpuusage.file''')
o.close()
k = int(n1) / 60
cpuusage = int(k)
sa = "%"
if cpuusage < 85 :
        print "OK : Average CPU Usage is %d%s" %(cpuusage, sa)
        sys.exit(0)
if cpuusage >= 85 and cpuusage < 95 :
        print "WARNING : Average CPU Usage is %d%s" %(cpuusage, sa)
        sys.exit(1)
if cpuusage >= 95 :
        print "CRITICAL : Average CPU Usage is %d%s" %(cpuusage, sa)
        sys.exit(2)
