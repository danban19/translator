import requests

from bs4 import BeautifulSoup

input_array = [input() for i in range(2)]
act = input_array[0]
page = input_array[1]
r = requests.get(f'{page}')
soup = BeautifulSoup(r.content, 'html.parser')
link = soup.find('a', text=f'ACT {act}').get('href')
print(link)
