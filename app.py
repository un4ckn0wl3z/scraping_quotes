from manager.quote_manager import QuoteManager

# total_page = 10
quote_manager = QuoteManager()

for quote in quote_manager.quotes:
    print(quote)