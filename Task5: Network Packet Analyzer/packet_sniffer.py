from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

# Function to handle captured packets
def packet_handler(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\nPacket captured: {packet.summary()}")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        
        # Check if the packet has a transport layer (TCP/UDP/ICMP)
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"Protocol: TCP")
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
            print(f"Payload: {bytes(tcp_layer.payload)}")
            
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"Protocol: UDP")
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
            print(f"Payload: {bytes(udp_layer.payload)}")
            
        elif ICMP in packet:
            print(f"Protocol: ICMP")
            icmp_layer = packet[ICMP]
            print(f"Type: {icmp_layer.type}")
            print(f"Code: {icmp_layer.code}")
            print(f"Payload: {bytes(icmp_layer.payload)}")
            
        else:
            print(f"Other Protocol")
            print(f"Payload: {bytes(ip_layer.payload)}")
    else:
        print("Non-IP packet captured")

# Main function to start sniffing on a specified network interface
def start_packet_sniffer(interface):
    print(f"Starting packet sniffer on interface: {interface}")
    # Sniff packets on the specified interface and pass them to the handler
    sniff(iface=interface, prn=packet_handler)

# Run the packet sniffer (make sure you have the appropriate permissions)
if __name__ == "__main__":
    interface = input("Enter the network interface to sniff on (e.g., 'eth0', 'wlan0'): ")
    start_packet_sniffer(interface)
