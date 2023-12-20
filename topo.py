#!/usr/bin/env python
from subprocess import call

from mininet.cli import CLI
from mininet.link import Intf
from mininet.link import TCLink
from mininet.log import info
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import Controller
from mininet.node import CPULimitedHost
from mininet.node import Host
from mininet.node import IVSSwitch
from mininet.node import Node
from mininet.node import OVSController
from mininet.node import OVSKernelSwitch
from mininet.node import RemoteController
from mininet.node import UserSwitch


def myNetwork():
    """ """
    net = Mininet(topo=None, build=False, ipBase="10.0.0.0/8")

    info("*** Adding controller\n")
    c0 = net.addController(name="c0",
                           controller=Controller,
                           protocol="tcp",
                           port=6633)

    info("*** Add Switch\n")
    s1 = net.addSwitch("s1", cls=OVSKernelSwitch)


    info("*** Add Hosts\n")
    
    h1 = net.addHost("Server_1", cls=Host, ip="10.0.0.1", defaultRoute=None,cpu=0.1)
    h2 = net.addHost("Server_2", cls=Host, ip="10.0.0.2", defaultRoute=None,cpu=0.1)
    h3 = net.addHost("Server_3", cls=Host, ip="10.0.0.3", defaultRoute=None,cpu=0.1)
    lb = net.addHost("Balancer", cls=Host, ip="10.0.0.254", defaultRoute=None,cpu=0.3)
    
    info("*** Add Clients\n")
    c1 = net.addHost("Client_1", cls=Host, ip="10.0.0.4", defaultRoute=None,cpu=0.2)
    c2 = net.addHost("Client_2", cls=Host, ip="10.0.0.5", defaultRoute=None,cpu=0.2)

    info("*** Add links\n")
    net.addLink(h1, s1, bw=1)
    net.addLink(h2, s1, bw=1)
    net.addLink(h3, s1, bw=1)
    net.addLink(lb, s1, bw=1)
    net.addLink(c1, s1, bw=1)
    net.addLink(c2, s1, bw=1)



    info("*** Starting HTTP server and Logging on every host\n")

    h1.cmd("python3 Server/server1.py &")
    h2.cmd("python3 Server/server2.py &")
    h3.cmd("python3 Server/server3.py &")
    lb.cmd("python3 LoadBalancer/lb.py &")

    

    info("*** Starting network\n")
    net.build()
    info("*** Starting controllers\n")
    for controller in net.controllers:
        controller.start()

    info("*** Starting switches\n")
    net.get("s1").start([c0])

    info("*** Post configure switches and hosts\n")
    net.pingAll()


    CLI(net)
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    myNetwork()
