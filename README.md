# Network Attack Simulation

This project consists of two Python scripts, `attack.py` and `app.py`, designed for network attack simulation and packet sending using different approaches.

## Prerequisites

- Python 3.x
- aiohttp library (`pip install aiohttp`)
- Flask library (`pip install Flask`)

## `attack.py`

The `attack.py` script uses the `socket` module to simulate a network attack by generating and sending packets to a specified server.

### Usage

1. Clone this repository or download the `attack.py` file.
2. Open a terminal and navigate to the directory containing `attack.py`.
3. Run the script
4. Adjust the `num_packets` variable in `attack.py` to change the number of packets sent.

## `app.py`

The `app.py` script uses asyncio and aiohttp libraries to asynchronously generate and send network packets to a specified server via HTTP requests.

### Usage

1. Clone this repository or download the `app.py` file.
2. Install the required libraries using pip:
3. Open a terminal and navigate to the directory containing `app.py`.
4. Start the Flask server by running:
5. Once the server is running, send a POST request to `http://127.0.0.1:5000/send_packets` with a JSON payload containing the number of packets to send.

### Endpoint

- `POST /send_packets`: Initiates the process of sending packets. Expects a JSON payload with the `num_packets` field specifying the number of packets to send.

### Configuration

- Modify the `OMNET_SERVER` variable in `app.py` to specify the address and port of the server where packets will be sent.

## Disclaimer

These scripts are for educational and testing purposes only. Do not use them for any malicious activities or against unauthorized systems.
