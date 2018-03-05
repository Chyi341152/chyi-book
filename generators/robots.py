# robots.py
#
# Find out who has been hitting robots.txt

from linesdir import *
from apachelog import *

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

addrs = set(r['host'] for r in log
            if 'robots.txt' in r['request'])

import socket
for addr in addrs:
    try:
        # Return a triple (hostname, aliaslist, ipaddrlists) where hostname is the primary host name
        print(socket.gethostbyaddr(addr))
    except socket.herror:
        #print(addr)
        pass
