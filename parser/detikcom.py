import os.path
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def parse_index(html):
  doc = BeautifulSoup(html, features='lxml')
  items = doc.find_all('article', { 'class': 'list-content__item'})
  data = []
  for item in items:
    title = item.find('h3', {'class': 'media__title'}).find('a', {'class': 'media__link'})
    data.append({
      'title': title.getText(),
      'url': title['href'],
    })
  return data

def parse_berita(html):
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

def get_path(url):
  path = urlparse(url).path
  directory = [x for x in path.split('/') if x]
  if len(directory) > 1:
    path = "{}/{}.html".format(directory[0], '_'.join(directory[1:]))
  else:
    path = '{}.html'.format(''.join(directory))
  return path

def isexists(url):
  return os.path.isfile(get_path(url))

def get(url):
  f = open(get_path(url), 'r')
  content = f.read()
  f.close()
  return content
