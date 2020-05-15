from .scraper import get_index, get_berita
from .parser import detikcom as parser

def get_and_parse_index(**opts):
  html_index = get_index(date=opts['date'], page=opts['page'])
  parsed_index = parser.parse_index(html_index)
  return parsed_index

def get_and_parse_berita(url):
  html_berita = get_berita(url)
  parsed_berita = parser.parse_berita(html_berita)
  return parsed_berita
