import scraper
from parser import detikcom

def run():
  url = 'https://news.detik.com/berita/d-5007699/influencer-ini-bagikan-tips-tetap-produktif-saat-pandemi-covid-19'

  html = ''
  if detikcom.isexists(url):
    html = detikcom.get(url)
  else:
    html = scraper.get(url)

  data = detikcom.parse(html)
  print(data)

if __name__ == '__main__':
  run()
