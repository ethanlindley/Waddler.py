from src.logger import Logger


class Penguin(object):
    def __init__(self, server, socket):
        self.logger = Logger("Penguin")

        self.server = server
        self.socket = socket

    def send(self, data):
        if self.socket:
            self.socket.sendall(data + "\0")
