from curio import run, spawn
from curio.socket import *

async def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    print('Server listening at', address)
    async with sock:
        while True:
            client, addr = await sock.accept()
            await spawn(echo_client(client, addr))

async def echo_client(client, addr):
    print('Connection from', addr)
    client.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
    async with client:
         while True:
             data = await client.recv(102400)
             if not data:
                 break
             await client.sendall(data)
    print('Connection closed')

if __name__ == '__main__':
    run(echo_server(('',25000)))
