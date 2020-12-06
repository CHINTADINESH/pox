#! /usr/bin/python

from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI

class Simple13Switch(Topo):
    """Simple topology example."""

    def __init__(self, **opts):
        """Create custom topo."""

        # Initialize topology
        # It uses the constructor for the Topo cloass
        super(Simple13Switch, self).__init__(**opts)

        # Adding hosts (name, ip)
        h0 = self.addHost('h0',ip='10.10.0.1')
        h1 = self.addHost('h1',ip='10.10.0.2')
        #h2 = self.addHost('h2',ip='10.10.0.3')
        #h3 = self.addHost('h3',ip='10.10.0.4')
        #h4 = self.addHost('h4',ip='10.10.0.5')
        #h5 = self.addHost('h5',ip='10.10.0.6')
        #h6 = self.addHost('h6',ip='10.10.0.7')
        #h7 = self.addHost('h7',ip='10.10.0.8')

        # Adding switches (name, datapath-id, OF version, ovs type system/user)
        s0 = self.addSwitch('s0', dpid="1000000000000000", protocols='OpenFlow13', datapath='user')
        s1 = self.addSwitch('s1', dpid="0100000000000000", protocols='OpenFlow13', datapath='user')
        s2 = self.addSwitch('s2', dpid="0010000000000000", protocols='OpenFlow13', datapath='user')

        # Add host to device links (src name, dst name)
        self.addLink(h0, s0)

        self.addLink(s0, s1)
        self.addLink(s1, s2)

        self.addLink(s2, h1)
        #self.addLink(h2, s0)
        #self.addLink(h3, s0)
        #self.addLink(h4, s0)
        #self.addLink(h5, s0)
        #self.addLink(h6, s0)
        #self.addLink(h7, s0)

#Define the IP address of the controller
def run():
    c = RemoteController('c', '127.0.0.1')
    net = Mininet(topo=Simple13Switch(), host=CPULimitedHost, controller=None, switch=OVSSwitch)
    net.addController(c)
    net.start()

    CLI(net)
    net.stop()

# Create a dictonory of topologies to enable instantiating the topologies
# from mininet commandline
# % mn --custom ./my_topology.py --topo=dictionary_key
topos = { 'simple_13_switch' : ( lambda: Simple13Switch())}

# if the script is run directly (sudo custom/optical.py):
if __name__ == '__main__':
    setLogLevel('info')
    run()
