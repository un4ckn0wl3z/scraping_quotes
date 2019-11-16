from manager.quote_manager import QuoteManager
from logger.app_logger import ApplicationLogger


ApplicationLogger.info(__name__, 'Application starting...')
quote_manager = QuoteManager()


for quote in quote_manager.quotes:
    print(quote)
