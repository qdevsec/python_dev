import struct
import socket
from concurrent.futures import ThreadPoolExecutor

# other helpful supporting modules
# threading --> parallel scanning
# concurrent.futures --> cleaner threading
# select --> async I/O
# struct --> parsing binary data (important for NetFlow)
# datatime --> timestamps
# argparse --> CLI tool

# What pros use
# scapy --> packet crafting / sniffing (very powerful)
# asyncio --> high-performance async scanners
# dpkt / pyshark --> packet parsing
# socketserver --> structured servers

# port scanner (TCP)
def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"[+] Port {port} is open")
        
        sock.close()
    except Exception as e:
        print(f"Error: {e}")


def call_scan_port():
    # use threads for faster scanning
    with ThreadPoolExecutor(max_workers=100) as executor:
        target = "127.0.0.1"
        for port in range(20, 1025):
            executor.submit(scan_port, target, port)

# socket listener (simple TCP server)
# socket listener waits for incoming network connections or data on a specifi IP and port
# 1. creates a socket
# 2. binds it to an IP + port
# 3. Listens for incoming connections (TCP) or packets (UDP)
# 4. Accepts or receives data
# 5. Processes or responds
# Every server runs a listener 
# log collectors, siem ingestion, netflow collectors, honeyports
# listener on udp 2055 collects NetFlow data from routers
def start_listener(host="0.0.0.0", port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[+] Listening on {host}:{port}")

    while True:
        client, addr = server.accept()
        print(f"[+] Connection from {addr}")

        data = client.recv(1024)
        print(f"Received: {data.decode()}")

        client.send(b"ACK\n")
        client.close()

# NetFlow Processing
# NetFlow is binary UDP data
# use socket (UDP) and struct (to unpack binary packets)
def udp_listener(port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", port))

    print(f"[+] Listening for UDP on port {port}")

    while True:
        data, addr = sock.recvfrom(4096)
        print(f"Packet from {addr}, size: {len(data)} bytes")

# parsing NetFlow
# Example: unpack first bytes of a NetFlow v5 header
def parse_netflow_header(data):
    version, count = struct.unpack("!HH", data[:4])
    print(f"Version: {version}, Flow count: {count}")

def start():
    ans = input("🌍🔗💻👋Handy python network tool, here are the options: \n"
                "pscan - tcp port scanning \n" \
                "slisten - socket listener, tcp server \n" \
                "netflow - netflow processing, netflow is udp data \n" \
                "pnetflow - parsing netflow header data \n" \
                "your choice? ")
    
    if ans == 'pscan':
        call_scan_port()
    elif ans == 'slisten':
        start_listener(port=int(input("What port? ")))
    elif ans == 'netflow':
        udp_listener(port=int(input("What port? ")))
    elif ans == 'pnetflow':
        parse_netflow_header(data=input("data? "))

# start the program
start()