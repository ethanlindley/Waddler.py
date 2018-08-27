from core.logger import Logger


class DataHandler(object):
    def __init__(self, server):
        self.logger = Logger("DataHandler")

        self.server = server

    def handle_xml(self, data):
        # TODO
        pass

    def handle_raw(self, data):
        # TODO
        pass