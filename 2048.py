# 2048

# 2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys.
# You can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over and over again. 
# Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and left keystrokes to automatically play the game.


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
