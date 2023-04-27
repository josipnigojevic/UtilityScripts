from scapy.all import *
 
# Define the interface to capture packets on
iface = 'Rimac-MAC'
 
# Create an L3 socket on the specified interface
s = conf.L3socket(iface=iface)
 
# Define a function to handle incoming packets
def packet_handler(packet):
    if packet is not None:
        packet.show()
 
# Start capturing packets and pass them to the packet_handler function
while True:
    packet = s.recv(MTU)
    packet_handler(packet)
