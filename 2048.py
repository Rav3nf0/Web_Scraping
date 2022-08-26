from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url='https://gabrielecirulli.github.io/2048/'
browser=webdriver.Firefox()
browser.get(url)
browser.implicitly_wait(15)

htmlElem= browser.find_element('tag name','html')
while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)