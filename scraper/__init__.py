from selenium import webdriver

def get(url):
  # Firefox setting
  options = webdriver.FirefoxOptions()
  options.headless = True

  # Website opening
  web = webdriver.Firefox(options=options)
  web.get(url)
  html = web.page_source
  web.quit()

  return html
