from gevent.server import StreamServer
from gevent.hub import get_hub

import gevent

class EchoServer(StreamServer):
    def do_handle(self, *args):
        return self._handle(*args)

def read_connection(socket):
    data = socket.recv(100000)
    socket.sendall(data)

def accept_connection(socket, address):
    print('New connection from %s:%s' % address)
    try:
        socket.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
    except (OSError, NameError):
        pass
    loop = get_hub().loop
    watcher = loop.io(socket.fileno(), 1)
    watcher.start(read_connection, socket)

if __name__ == '__main__':
    server = EchoServer(('0.0.0.0', 25000), accept_connection, spawn=gevent.spawn)
    server.serve_forever()
