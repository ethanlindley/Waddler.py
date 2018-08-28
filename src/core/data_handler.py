from src.logger import Logger


class DataHandler(object):
    def __init__(self, server):
        self.logger = Logger("DataHandler")

        self.server = server

    def handle_xml(self, penguin, data):
        if "policy-file-request" in data:
            penguin.send("<cross-domain-policy><allow-access-from domain='*' to-ports='*' /></cross-domain-policy>")
        elif "verChk" in data and "v='153'" in data:
            penguin.send("<msg t='sys'><body action='apiOK' r='0'></body></msg>")
        else:
            self.logger.warning("don't know how to handle packet - {}".format(data))

    def handle_raw(self, penguin, data):
        # TODO
        pass
