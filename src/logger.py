class Logger(object):
    def __init__(self, name):
        self.name = name

    def debug(self, msg):
        print('::{0}(debug):: {1}'.format(self.name, msg))

    def info(self, msg):
        print('::{0}:: {1}'.format(self.name, msg))

    def warning(self, msg):
        print('::{0}(warning):: {1}'.format(self.name, msg))
