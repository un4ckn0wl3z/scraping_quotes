from manager.quote_manager import QuoteManager
from logger.app_logger import ApplicationLogger

try:
    ApplicationLogger.inject(__name__).info('Application starting...')
    quote_manager = QuoteManager()
    for quote in quote_manager.quotes:
        print(quote)
except Exception as e:
    print(e)
