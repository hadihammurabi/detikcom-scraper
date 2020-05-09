from bs4 import BeautifulSoup

def parse(html):
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

  return data
