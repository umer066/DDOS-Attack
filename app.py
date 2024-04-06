import asyncio
import aiohttp
from aiohttp import ClientSession
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define the address and port of the server
OMNET_SERVER = 'http://127.0.0.1:8080'

async def send_packet(session, packet):
    async with session.post(f'{OMNET_SERVER}/receive_packet', json=packet) as response:
        if response.status != 200:
            print(f'Failed to send packet: {packet}')

def generate_packet():
    src_ip = f'10.0.0.{random.randint(1, 255)}'
    dst_ip = f'10.0.0.{random.randint(1, 255)}'
    src_port = random.randint(1024, 65535)
    dst_port = random.randint(1024, 65535)
    protocol = random.choice(['TCP', 'UDP'])
    timestamp = '2024-04-07T12:00:00'
    packet = {
        'src_ip': src_ip,
        'dst_ip': dst_ip,
        'src_port': src_port,
        'dst_port': dst_port,
        'protocol': protocol,
        'timestamp': timestamp
    }
    return packet

@app.route('/send_packets', methods=['POST'])
async def send_packets():
    try:
        # Get the number of packets from the request
        num_packets = 100000

        # Create a ClientSession for async requests
        async with ClientSession() as session:
            # Create a list to hold asyncio tasks
            tasks = []
            # Generate and send each packet asynchronously
            for _ in range(num_packets):
                packet = generate_packet()
                task = asyncio.ensure_future(send_packet(session, packet))
                tasks.append(task)
            # Run all tasks concurrently
            asyncio.get_event_loop().run_until_complete(asyncio.gather(*tasks))

        return jsonify({'message': 'Packets sent successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
