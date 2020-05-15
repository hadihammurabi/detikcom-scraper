from selenium import webdriver

def get_index(**opts):
  options = webdriver.FirefoxOptions()
  options.headless = True

  # Website opening
  web = webdriver.Firefox(options=options)

  if not opts['page'] or opts['page'] < 1:
    opts['page'] = 1
  
  if opts['page'] and opts['page'] > 24:
    opts['page'] = 24

  web.get("https://news.detik.com/indeks/{}?date={}".format(opts['page'], opts['date']))
  html = web.page_source
  web.quit()

  return html

def get_berita(url):
  # Firefox setting
  options = webdriver.FirefoxOptions()
  options.headless = True

  # Website opening
  web = webdriver.Firefox(options=options)
  web.get(url)
  html = web.page_source
  web.quit()

  return html
