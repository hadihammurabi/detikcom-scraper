import scraper
import parser.detikcom as parser

def run():
  html_index = scraper.get_index(date="05/15/2020", page=1)
  indexes = parser.parse_index(html_index)
  print(indexes)

  with open('output', 'a') as f:
    f.write(str(indexes))
    f.close()

  for index in indexes:
    html_berita = scraper.get_berita(index['url'])
    data = parser.parse_berita(html_berita)
    print(data)
    with open('output', 'a') as f:
      f.write(str(data))
      f.close()

if __name__ == '__main__':
  run()
