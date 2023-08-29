import socket
import select
import threading
import time
import datetime
import ssl

# Configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8082
CONFIG_FILE_PATH = 'config.txt'
REREAD_ON_QUERY = True
MAX_PAYLOAD_SIZE = 1024
DEBUG_MODE = True
SSL_ENABLED = False
SSL_CERTIFICATE = 'SSL_CERTIFICATE\server.crt'
SSL_KEY = 'SSL_KEY\server.key'
linux_path = input("Enter the file path: ")


def search_string_in_file(file_path, search_string):
    with open(file_path, "r") as file:
        for line in file:
            if line.strip() == search_string:
                return True
    return False


def read_file_contents(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def handle_client(sock):
    while True:
        try:
            # Receive data from the client
            data = sock.recv(MAX_PAYLOAD_SIZE).decode().strip('\x00')[:MAX_PAYLOAD_SIZE]

            if not data:
                # No data received, client has disconnected
                print(f"Client {sock.getpeername()} disconnected")
                sock.close()
                client_sockets.remove(sock)
                return

            # Process the received data
            if DEBUG_MODE:
                print(f"DEBUG: Received data from {sock.getpeername()}: {data}")

            # Search for the string in the file
            start_time = time.time()
            if REREAD_ON_QUERY:
                file_contents = read_file_contents(CONFIG_FILE_PATH)
            result = search_string_in_file(CONFIG_FILE_PATH, data)
            end_time = time.time()
            execution_time = end_time - start_time

            # Send a response back to the client
            response = "STRING EXISTS\n" if result else "STRING NOT FOUND\n"
            sock.sendall(response.encode())

            # Log the debug information
            if DEBUG_MODE:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                debug_info = f"DEBUG: Query: {data}, IP: {sock.getpeername()}, Execution Time: {execution_time:.6f}s, Timestamp: {timestamp}"
                print(debug_info)
        except Exception as e:
            print(f"Error occurred while handling client {sock.getpeername()}: {str(e)}")
            sock.close()
            client_sockets.remove(sock)
            return


# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Enable listening for incoming connections
server_socket.listen()

# Wrap the socket with SSL/TLS if enabled
if SSL_ENABLED:
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(SSL_CERTIFICATE, SSL_KEY)
    server_socket = ssl_context.wrap_socket(server_socket, server_side=True)

print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

# List to keep track of connected client sockets
client_sockets = [server_socket]

# Main server loop
while True:
    # Wait for a client socket to be ready for processing
    print("Client Sockets:", client_sockets)
    ready_sockets, _, _ = select.select(client_sockets, [], [])

    for sock in ready_sockets:
        if sock == server_socket:
            # New connection request received
            client_socket, client_address = server_socket.accept()
            client_sockets.append(client_socket)
            print(f"New connection from {client_address[0]}:{client_address[1]}")

            # Start a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
