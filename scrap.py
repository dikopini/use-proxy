import requests
from bs4 import BeautifulSoup


url = 'https://www.kogan.com/au/c/bed-frames/'

r = requests.get(url)
s = BeautifulSoup(r.text, 'html.parser')

barang = s.find('div', {'class':'_3dbuB _2TkM7 _1tVxb tVqMg'})
nama_barang = s.find('div', {'class':'_2_1T4 _3NIzE'})
print(s)

