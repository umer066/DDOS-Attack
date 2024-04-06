import socket
import random
import time

# Define the address and port of the server
OMNET_SERVER = ('127.0.0.1', 8080)

def generate_packet():
    src_ip = f'10.0.0.{random.randint(1, 255)}'
    dst_ip = f'10.0.0.{random.randint(1, 255)}'
    src_port = random.randint(1024, 65535)
    dst_port = random.randint(1024, 65535)
    protocol = random.choice(['TCP', 'UDP'])
    timestamp = '2024-04-07T12:00:00'
    packet = f'{src_ip},{dst_ip},{src_port},{dst_port},{protocol},{timestamp}\n'
    return packet.encode()

def send_packets(num_packets):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(OMNET_SERVER)
            for _ in range(num_packets):
                packet = generate_packet()
                s.sendall(packet)
                time.sleep(0.01)  # Sleep for a small duration between packets
            print('Packets sent successfully')
        except Exception as e:
            print(f'Error sending packets: {e}')

if __name__ == '__main__':
    num_packets = 10000
    send_packets(num_packets)
