import logging

from config.log_config import LogConfig

logging.basicConfig(
    format=LogConfig.FORMAT,
    datefmt=LogConfig.DATE_FORMAT,
    level=LogConfig.LEVEL,
    filename=LogConfig.FILE_NAME
)


class ApplicationLogger:
    """
    logger
    """

    @staticmethod
    def info(context, message):
        logging.getLogger(context)
        logging.info(message)
