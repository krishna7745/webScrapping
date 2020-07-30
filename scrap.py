import re
import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.javatpoint.com')
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')
a=[];b='\n'
href =soup.find_all(href=re.compile('[a-z,A-z,-,0-9]+'))
for i in href:
    a.append(str(i['href']))
b=b.join(a)
c=re.findall('^https:\/\/.*',b,re.M)
b='\n'
b=b.join(c)
print(b)
with open(r'C:\Users\User\Desktop\filescrap.txt','w') as f:
    f.write(b)
