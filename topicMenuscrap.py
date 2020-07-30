import requests
import re
import urllib3
from bs4 import BeautifulSoup
with open('filescrap.txt','r') as f:
    for l in f:
        print(l)
        page =requests.get(l)
        soup = BeautifulSoup(page.content,'html.parser')
        #print(soup.prettify())
        a=[];b='\n'
        href =soup.find_all("div",id="menu")
        for i in href:
            print(i)
            a.append(str(i))
        b=b.join(a)
        print(soup.find_all("div").prettify())
        filename=l
        filename=filename.split("/")[-1].strip('\n')
        filename= 'C:\\Users\\User\Desktop\\topicList\\'+filename+'.txt'
        with open(filename,'w')as file:
            file.write(b)
