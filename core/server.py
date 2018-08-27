from core.logger import Logger
from core.data_handler import DataHandler
import socket
import sys


class Server(object):
    def __init__(self, config):
        self.logger = Logger("Server")

        if not config:
            self.logger.warning("Unable to find server configuration")
            sys.exit()

        self.type = config["type"]
        self.port = config["port"]
        self.max_penguins = config["max_penguins"] if self.type is "world" else 150

        self.penguins = []

        self.data_handler = DataHandler(self)

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("127.0.0.1", self.port))
        
        self.logger.info("{0} server listening on port {1}".format(self.type, self.port))
        server.listen(10000)

        while True:
            client, addr = server.accept()
            if len(self.penguins) >= self.max_penguins:
                client.close()
            self.logger.debug("new connection from {}".format(addr))
            try:
                data = client.recv(4096).decode("utf-8")
                if data[0] == "<":
                    self.logger.debug("received XML packet - {}".format(data))
                    self.data_handler.handle_xml(data)
                elif data[0] == "%":
                    self.logger.debug("received RAW packet - {}".format(data))
                    self.data_handler.handle_raw(data)
                else:
                    self.logger.debug("received rogue packet - {}".format(data))
            finally:
                client.close()
