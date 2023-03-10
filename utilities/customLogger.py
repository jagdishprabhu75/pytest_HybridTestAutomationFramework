import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='..//logs//automation.log', level=logging.INFO, force=True,
                            format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m%d%Y %I:%M:%S %p')

        logger = logging.getLogger()
        return logger
