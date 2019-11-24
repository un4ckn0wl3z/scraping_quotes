from selenium import webdriver

author = input("Enter the author you'd like quotes from: ")
tag = input("Enter your tag: ")


from pages.quotes_page import QuotesPage
chrome = webdriver.Chrome(executable_path="./chromedriver.exe")
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

print(page.search_for_quotes(author, tag))













