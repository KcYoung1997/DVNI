#!/usr/bin/python
from mininet.clean import cleanup
from mininet.cli import CLI
from mininet.log import info, setLogLevel
from mininet.net import Containernet
from mininet.node import Controller

from container.ftpd import Ftpd
from container.nginx import Nginx

setLogLevel('debug')

info('*** Running Cleanup\n')
cleanup()
net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')
info('*** Adding ftp\n')
nginx = net.addDocker('ftp',
                      cls=Ftpd,
                      ip='10.10.10.1/24')
info('*** Adding host\n')
h1 = net.addHost('h1',
                 ip='10.10.10.2/24')
info('*** Adding switch\n')
s1 = net.addSwitch('s1')
info('*** Creating links\n')
net.addLink(h1, s1)
net.addLink(nginx, s1)
info('*** Starting network\n')
net.start()
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()
