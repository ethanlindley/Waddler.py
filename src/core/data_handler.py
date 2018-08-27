from src.logger import Logger
import xml.etree.ElementTree as ET


class DataHandler(object):
    def __init__(self, server):
        self.logger = Logger("DataHandler")

        self.server = server

    def handle_xml(self, penguin, data):
        if data == "<policy-file-request/>":
            penguin.send("<cross-domain-policy><allow-access-from domain='*' to-ports='*' /></cross-domain-policy>")
        else:
            self.logger.warning("don't know how to handle packet - {}".format(data))

    def handle_raw(self, penguin, data):
        # TODO
        pass
