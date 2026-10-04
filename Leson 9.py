import requests
from bs4 import BeautifulSoup


res = requests.get("https://coinmarketcap.com/")
coin_list = []
# responce_text = res.text.split('<span>')
# for elem in responce_text:
#     if elem.startswith('$'):
#         for elem2 in elem.split('</span>'):
#             if elem2.startswith('$'):
#                 coin_list.append(elem2.replace('$', '').replace(',', ''))
#
# print(coin_list[8])

soup = BeautifulSoup(res.text, features='html.parser')
soup_list = soup.find_all("div", {"class", "sc-664711f9-0"})
for el in soup_list:
    coin_list.append(float(str(el).split('<span>')[1].split('</span>')[0].replace('$', '').replace(',', '')))

print(coin_list[1])