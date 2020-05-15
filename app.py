from engine import get_and_parse_index, get_and_parse_berita

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
