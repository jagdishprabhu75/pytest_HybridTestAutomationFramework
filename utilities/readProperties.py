import configparser

config = configparser.RawConfigParser()
config.read("..\\configurations\\config.ini")


class read_Config:
    @staticmethod
    def get_url():
        return config.get('Common', 'base_url')