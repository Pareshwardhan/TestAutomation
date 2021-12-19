import configparser


class Configuration:

    def getconfig(self):
        config=configparser.ConfigParser()
        config.read('../Utilities/properties.ini')
        return config