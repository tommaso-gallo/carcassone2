import socket

HOST = "0.0.0.0"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}...")

    while True:  # Loop to accept multiple clients
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            conn.sendall(b"Hello from Raspberry Pi!\n")
            # Optional: receive data from client
            data = conn.recv(1024)
            if data:
                print(f"Received: {data.decode().strip()}")
