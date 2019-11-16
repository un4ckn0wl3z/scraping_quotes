import logging


class LogConfig:
    FORMAT = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
    DATE_FORMAT = '%d-%m-%Y %H:%M:%S'
    LEVEL = logging.INFO
    FILE_NAME = 'logs.txt'
