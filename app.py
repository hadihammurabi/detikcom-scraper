from selenium import webdriver
from bs4 import BeautifulSoup

# Firefox setting
options = webdriver.FirefoxOptions()
options.headless = True

# Website opening
web = webdriver.Firefox(options=options)
web.get('https://news.detik.com/berita/d-5007699/influencer-ini-bagikan-tips-tetap-produktif-saat-pandemi-covid-19')
html = web.page_source
web.quit()

# Website document processing
doc = BeautifulSoup(html, features='lxml')

# Get information/data
title = doc.find('h1', { 'class': 'detail__title' }).getText()
contents = doc.find('div', { 'class': 'detail__body-text' }).findAll('p')

# Clean and save
data = {
  'title': title.replace('\n', '').strip(),
}

data['body'] = ''
for content in contents:
  data['body'] += content.getText()

print(data)
