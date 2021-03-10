import yaml
import os
import logging.config


class Logger:

    @staticmethod
    def load():
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + '/log_dev.yml', 'r') as f_conf:
            dict_conf = yaml.load(f_conf)
            logging.config.dictConfig(dict_conf)


gather_logger = logging.getLogger("gather")
gather_logger.setLevel(logging.DEBUG)

broadcast_logger = logging.getLogger("broadcast")
broadcast_logger.setLevel(logging.DEBUG)

sign_logger = logging.getLogger("sign")
sign_logger.setLevel(logging.DEBUG)