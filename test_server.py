import pytest
import socket
import threading
import time
import os
from client.py import handle_client, search_string_in_file, read_file_contents

# Test file paths
TEST_CONFIG_FILE_PATH = 'test_config.txt'
TEST_SSL_CERTIFICATE = 'SSL_CERTIFICATE\server.crt'
TEST_SSL_KEY = 'SSL_KEY\server.key'

# Test data
TEST_FILE_CONTENTS = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n",
    "Line 4\n",
    "Line 5\n"
]

@pytest.fixture(scope="session")
def setup_test_files(request):
    # Create a test configuration file with test contents
    with open(TEST_CONFIG_FILE_PATH, 'w') as file:
        file.writelines(TEST_FILE_CONTENTS)

    # Provide cleanup after all tests are completed
    def cleanup():
        os.remove(TEST_CONFIG_FILE_PATH)
    
    request.addfinalizer(cleanup)

@pytest.fixture
def mock_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def test_search_string_in_file(setup_test_files):
    # Test search for an existing string in the test file
    assert search_string_in_file(TEST_CONFIG_FILE_PATH, "Line 3\n") == True

    # Test search for a non-existing string in the test file
    assert search_string_in_file(TEST_CONFIG_FILE_PATH, "Line 6\n") == False

def test_read_file_contents(setup_test_files):
    # Test reading the file contents
    contents = read_file_contents(TEST_CONFIG_FILE_PATH)
    assert contents == TEST_FILE_CONTENTS

def test_handle_client(mock_socket, setup_test_files):
    # Mock the necessary data for testing
    mock_socket.recv.side_effect = ["Line 1\n", "Line 2\n", "Line 6\n", ""]
    mock_socket.sendall = lambda data: None
    mock_socket.close = lambda: None

    # Call the function being tested
    handle_client(mock_socket)

    # Perform the necessary assertions
    mock_socket.sendall.assert_any_call(b"STRING EXISTS\n")
    mock_socket.sendall.assert_any_call(b"STRING NOT FOUND\n")
    assert mock_socket.close.called

def test_speed_testing():
    # Perform speed testing with different file sizes and number of queries per second
    QUERY = 'test_query'  

    # Number of queries per second to send
    QUERIES_PER_SECOND = 10000

    # Number of seconds to run the test
    TEST_DURATION = 10

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Start time of the test
    start_time = time.time()

    # Send queries for the specified duration
    num_queries_sent = 0
    end_time = start_time + TEST_DURATION
    while time.time() < end_time:
         
         
         # Send a query
         client_socket.sendall(QUERY.encode())

         # Receive the response
         response = client_socket.recv(1024)
         # Process the response if needed

         num_queries_sent += 1

         # Calculate the execution time and queries per second
         execution_time = time.time() - start_time
         queries_per_second = num_queries_sent / execution_time

         # Print the results
         print(f"Execution time: {execution_time:.2f} seconds")
         print(f"Queries per second: {queries_per_second:.2f}")

         # Close the client socket
         client_socket.close()

def test_correct_workflow():
    # Test the correct workflow in all paths and cases
    # Global variable to store the received queries
    received_queries = []

def handle_client(sock):
    while True:
        try:
            # Receive data from the client
            data = sock.recv(1024).decode().strip()

            if not data:
                # No data received, client has disconnected
                sock.close()
                return

            # Process the received data
            received_queries.append(data)

            # Send a response back to the client
            response = "RESPONSE"
            sock.sendall(response.encode())
        except Exception as e:
            print(f"Error occurred while handling client {sock.getpeername()}: {str(e)}")
            sock.close()
            return

def test_correct_workflow():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified host and port
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    # Enable listening for incoming connections
    server_socket.listen()

    # Start a thread to handle the server
    server_thread = threading.Thread(target=lambda: server_socket.accept())
    server_thread.start()

    # Create a client socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Send a query to the server
    query = "TEST_QUERY"
    client_socket.sendall(query.encode())

    # Receive the response from the server
    response = client_socket.recv(1024).decode().strip()

    # Close the client socket and server socket
    client_socket.close()
    server_socket.close()

    # Perform assertions to test the correct workflow
    assert response == "RESPONSE"
    assert len(received_queries) == 1
    assert received_queries[0] == query

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])


