import requests
from bs4 import BeautifulSoup as S

c = input('Enter Your Country :')
url = f'https://www.google.com/search?q=meteo+{c}&csrf=ALii subUC5stegGm-aJnhConeyU75zGtw%3A1670592863548&ei=XzmTY-mNIY2NhbIPz_Cr6AU&ved=0ahUKVespucci0-z7AhWNRkAHU_4Cl0Q4dBAUD&act=5&oq=meteo+{c}&gs_lcp=bend3Mtd2l6delfcnAQAzIOCCMQJxBDEJ0CEESQgAIyBQgAEILTMgUIABCABDIFCAAQgAQyBQgAEILTMgUIABCABDIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEILTMgCUIABADoKCALRxDW BBCwAzoFAAQkQI6BwgAERIALAo6CAgAERIALMsBOgwCABBINGAhAKE6DAgjECcQnQIQRhCAAjoECCE0oYANCEYEoFEYYAZ4WLMnYParaAFwAXgAgAGQAogBmg6SAQYwLjExLjGIGYACgASHIAQjAARE&client=gws-wiz-serp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = S(r.content, 'html.parser')
print(f'meteo Now in {c}')
x = soup.find(id="wob_loc")
print(x.string, (soup.find(id="wob_tm").string + 'C'))
print('Precipitation: ', soup.find(id="wob_pp").string)
print('Humidity : ', soup.find(id="wob_hm").string)
print('Wind: ', soup.find(id="wob_ws").string)
print('day and time: ', soup.find(id="wob_dts").string)
print('Weather situation: ', soup.find(id="wob_dc").string)
