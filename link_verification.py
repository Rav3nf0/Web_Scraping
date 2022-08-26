import requests,os,bs4
from selenium import webdriver

url='https://automatetheboringstuff.com/chapter11/'

print('downloading the page...%s...' %url )
res=requests.get(url)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text,'html.parser')
new_links=soup.select('a[href]')
ctr=0
mtr=0

for links in new_links:
    
    print('Downloading %s...' %links)
    url2=links.get('href')
    
    try:
        m=requests.get(url2)
        m.raise_for_status()
    
    except Exception as exc:
        print('Error occured')
        mtr+=1
    ctr+=1

print('The program has gone through a total of %s linked pages.' %ctr)
print('The no of broken pages : %s ' %mtr )