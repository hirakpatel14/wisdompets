import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)

# print (response)
# if(str(response).find('200')):
#     print('Successful Response')
# else:
#     print('Page not found')

parsedContent = BeautifulSoup(response.text, 'html.parser')
print(len(parsedContent.findAll('a')))
# for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
# for i in range(36,len(parsedContent.findAll('a'))):
one_a_tag = parsedContent.findAll('a')[36]
print(one_a_tag)
link = one_a_tag['href']
download_url = 'http://web.mta.info/developers/'+ link
# urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])