from mininet.topo import Topo  
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink

class tree(Topo):
	def __init__(self):
		Topo.__init__(self)

		Internet = self.addHost( 'h1-int',ip='172.16.0.1/24', mac='00:00:00:00:00:01' )
		Internet2 = self.addHost( 'h14-int',ip='172.16.0.14/24', mac='00:00:00:00:00:0E' )
		Host2 = self.addHost( 'h2-1',ip='172.16.0.2/24', mac='00:00:00:00:00:02' )
		Host3 = self.addHost( 'h3-1',ip='172.16.0.3/24', mac='00:00:00:00:00:03' )
		Host4 = self.addHost( 'h4-1',ip='172.16.0.4/24', mac='00:00:00:00:00:04' )
		Host5 = self.addHost( 'h5-2',ip='172.16.0.5/24', mac='00:00:00:00:00:05' )
		Host6 = self.addHost( 'h6-2' ,ip='172.16.0.6/24', mac='00:00:00:00:00:06' )
		Host7 = self.addHost( 'h7-2' ,ip='172.16.0.7/24', mac='00:00:00:00:00:07' )
		Host8 = self.addHost( 'h8-3' ,ip='172.16.0.8/24', mac='00:00:00:00:00:08' )
		Host9 = self.addHost( 'h9-3' ,ip='172.16.0.9/24', mac='00:00:00:00:00:09' )
		Host10 = self.addHost( 'h10-3',ip='172.16.0.10/24', mac='00:00:00:00:00:0A' )
		Host11 = self.addHost( 'h11-4' ,ip='172.16.0.11/24', mac='00:00:00:00:00:0B' )
		Host12 = self.addHost( 'h12-4' ,ip='172.16.0.12/24', mac='00:00:00:00:00:0C' )
		Host13 = self.addHost( 'h13-4' ,ip='172.16.0.13/24', mac='00:00:00:00:00:0D' )
		Switch1 =self.addSwitch('s1',ip='172.16.0.15/24', mac='00:00:00:00:00:0F' )
		Switch2 =self.addSwitch('s2',ip='172.16.0.16/24', mac='00:00:00:00:00:11' )
		Switch3 =self.addSwitch('s3',ip='172.16.0.17/24', mac='00:00:00:00:00:12' )
		Switch4 =self.addSwitch('s4',ip='172.16.0.18/24', mac='00:00:00:00:00:13' )

		# Add links
		self.addLink( Internet, Switch1, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host2, 	Switch1, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host3, 	Switch1, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host4, 	Switch1, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		
		self.addLink( Switch1, 	Switch2, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host5, 	Switch2, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host6, 	Switch2, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host7,	Switch2, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Switch2, 	Switch3, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host8, 	Switch3, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host9, 	Switch3, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host10, 	Switch3, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Switch3, 	Switch4, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host11, 	Switch4, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host12, 	Switch4, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Host13, 	Switch4, bw=100, delay='1ms', loss=3, max_queue_size=1000 )
		self.addLink( Internet2,Switch4, bw=100, delay='1ms', loss=3, max_queue_size=1000 )

topos={'tree':(lambda:tree())}




def start_basic():
	top = tree()
	net = Mininet(topo=top,link=TCLink)
	net.start()
	


	#Retrieve Net Objects	
	internet = net.get('h1-int')
	internet2 = net.get('h14-int')
	h2 = net.get( 'h2-1' )
	# Launch iperf server
	internet.popen('sudo iperf -s -p 5566 -i 1 -w 4000')
	internet2.popen('sudo iperf -s -p 5566 -i 1 -w 4000')
	#Launch iperf client
	h2.popen('iperf -c 172.16.0.14 -p 5566 -t 90 -w 2000')

	#Retrieve Object
  	
        h3 = net.get( 'h3-1' )
        h4 = net.get( 'h4-1' )
        h5 = net.get( 'h5-2' )
        h6 = net.get( 'h6-2' )
        h7 = net.get( 'h7-2' )
        h8 = net.get( 'h8-3' )
        h9 =  net.get( 'h9-3' )
        h10 = net.get( 'h10-3' )
        h11 = net.get( 'h11-4' )
        h12 = net.get( 'h12-4' )
        h13 = net.get( 'h13-4' )

	#Launch iperf client
	
	h2.popen('iperf -c 172.16.0.14 -p 5566 -t 90 -w 2000')
        h3.popen('iperf -c 172.16.0.14 -p 5566 -t 90 -w 2000')
        h4.popen('iperf -c 172.16.0.14 -p 5566 -t 90 -w 2000')
        h5.popen('iperf -c 172.16.0.14 -p 5566 -t 90 -w 2000')
        h6.popen('iperf -c 172.16.0.14 -p 5566 -t 90 -w 2000')
        h7.popen('iperf -c 172.16.0.14 -p 5566 -t 90 -w 2000')
        h8.popen('iperf -c 172.16.0.1 -p 5566 -t 90 -w 2000')
        h9.popen('iperf -c 172.16.0.1 -p 5566 -t 90 -w 2000')
        h10.popen('iperf -c 172.16.0.1 -p 5566 -t 90 -w 2000')
        h11.popen('iperf -c 172.16.0.1 -p 5566 -t 90 -w 2000')
        h12.popen('iperf -c 172.16.0.1 -p 5566 -t 90 -w 2000')
        h13.popen('iperf -c 172.16.0.1 -p 5566 -t 90 -w 2000')
	


	CLI(net)
	net.stop()



if __name__ == '__main__':
    setLogLevel('info')
    start_basic()
