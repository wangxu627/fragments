import socketserver
import socket

client_socks = []
    
class MyTCPHandler(socketserver.BaseRequestHandler):
    
          
    def handle(self):
        print("111111111111111111111111")
        client_socks.append(self.request)
        while True:
          data = self.request.recv(1024).strip()
          if not data:
              break
          print(f"Received data from {self.client_address[0]}: {data}")
          response = "Server received: " + data.decode()
          self.request.sendall(response.encode())

if __name__ == "__main__":
    host, port = "0.0.0.0", 8890

    server = socketserver.TCPServer((host, port), MyTCPHandler)
    server.allow_reuse_address = True
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print(f"Server listening on {host}:{port}")
    server.serve_forever()