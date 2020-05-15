import scraper
import parser.detikcom as parser

def get_and_parse_index(**opts):
  html_index = scraper.get_index(date=opts['date'], page=opts['page'])
  parsed_index = parser.parse_index(html_index)
  return parsed_index

def get_and_parse_berita(url):
  html_berita = scraper.get_berita(url)
  parsed_berita = parser.parse_berita(html_berita)
  return parsed_berita

def run():
  indexes = get_and_parse_index(date="05/15/2020", page=1)
  print(indexes)

  with open('output', 'a') as f:
    f.write(str(indexes))
    f.close()

  for index in indexes:
    data = get_and_parse_berita(index['url'])
    print(data)
    with open('output', 'a') as f:
      f.write(str(data))
      f.close()

if __name__ == '__main__':
  run()
