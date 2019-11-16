import logging

from config.log_config import LogConfig

try:
    logging.basicConfig(
        format=LogConfig.FORMAT,
        datefmt=LogConfig.DATE_FORMAT,
        level=LogConfig.LEVEL,
        filename=LogConfig.FILE_NAME
    )
except FileNotFoundError:
    print('Looking for log folder but not found, Application will automate create this folder, please run application '
          'again.')
    import os

    os.makedirs('log')
    exit(1)


class ApplicationLogger:
    """
    logger
    """

    @staticmethod
    def inject(context):
        logging.getLogger(context)
        return logging
