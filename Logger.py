import logging


class LogGen:

    @staticmethod
    def loggen():

        logging.basicConfig(filename=".//Logs//autommation.log",format="%(asctime)s;%(levelname)s;%(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger