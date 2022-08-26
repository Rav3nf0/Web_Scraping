import requests,sys,os,bs4

url='http://imgur.com/search?q='
os.makedirs('imgur_img', exist_ok=True)

print('downloading page %s...' % url)
##headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'} 

res=requests.get(url + ' '.join(sys.argv[1:])) #takes the search keyword from the command line
res.raise_for_status
print(res.text)
soup=bs4.BeautifulSoup(res.text, "html.parser")

images = soup.select('.image-list-link img')
print('total number of images:',len(images))

for img in images[:15]: #here we only download the first 15 images
    img_links = 'https:'+img.get('src') 
    print('Downloading image %s...' %img_links )
    res2= requests.get(img_links)

    imageFile =open(os.path.join('imgur_img', os.path.basename(img_links)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

print('Done!!!')