This is what the program does:

1] Gets search keywords from the clipboard using clipboard
2] Retrieves the search results page
3] Opens a browser tab for each result



import bs4,requests,webbrowser,pyperclip

print('seraching....')
res =requests.get('https://www.google.com/search?q=' 'https://pypi.org/search/?q=' + pyperclip.paste())#' '.join(sys.argv[1:]))

res.raise_for_status()

soup =bs4.BeautifulSoup(res.text, 'html parser')
linkElems=soup.select('.package-snippet')
print(linkElems)

numopen = min(5, len(linkElems))
for i in range(numopen):
    urltoOpen ='https://pypi.org' + linkElems[i].get('href')
    print('Opening', urltoOpen)
    webbrowser.open(urltoOpen)
