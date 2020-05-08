from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.FirefoxOptions()
options.headless = True

web = webdriver.Firefox(options=options)
web.get('https://news.detik.com/berita/d-5007699/influencer-ini-bagikan-tips-tetap-produktif-saat-pandemi-covid-19')
html = web.page_source
export = open("berita/d-5007699_influencer-ini-bagikan-tips-tetap-produktif-saat-pandemi-covid-19.html", "a")
export.write(html)
export.close()
web.quit()