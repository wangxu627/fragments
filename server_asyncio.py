import asyncio
import base64

PORT = 20000
client_socks = []
client_writers = []



# async def handle_read_data(reader, writer):
#     # loop = asyncio.get_event_loop()
#     # data = await reader.read()
#     client_sock = writer.get_extra_info('socket')
#     client_socks.append(client_sock)
#     client_writers.append(writer)

#     print("Accept")
#     while True:
#         data = await reader.read(64)
#         print(data)
#         if(not data):
#             break
#         # r = base64.b64encode(data)
#         # r = base64.b64decode(r)
#         print("LLLLLLLL :: ", len(client_writers))
#         for writer in client_writers:
#             writer.write(data)
#             await writer.drain()

class MyProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        client_sock = transport.get_extra_info('socket')
        client_socks.append(client_sock)
        self.transport = transport

    def data_received(self, data):
        self.transport.write(data)

async def create_server(address, port):
    server = await asyncio.start_server(MyProtocol, address, port)
    return server


def run_server():
    loop = asyncio.get_event_loop()
    server = loop.run_until_complete(create_server("0.0.0.0", PORT))
    host = server.sockets[0].getsockname()  
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))  
    try:
        loop.run_forever()  
    except KeyboardInterrupt:  
        pass
    print('Server shutting down.')
    server.close()
    loop.run_until_complete(server.wait_closed())  
    loop.close()  


if __name__ == "__main__":
    run_server()