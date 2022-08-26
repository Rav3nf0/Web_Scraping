# Command Line Emailer
# Write a program that takes an email address and string of text on the command line and then,
# using selenium, logs in to your email account and sends an email of the string to the provided address.


import os,requests,time,bs4,sys
from selenium import webdriver
browser=webdriver.Firefox()
from selenium.webdriver.common.keys import Keys
import pyinputplus as pyip

print(type(browser))

#if len(sys.argv) >1: #the first arfument is the command itself we take the index position 
# starting from 1 as the gmail address
mail = ' '.join(sys.argv[1:])
password=pyip.inputPassword(prompt='Enter the password:')#secure prompt for password

browser=webdriver.Firefox()
#print(type(browser))
browser.implicitly_wait(15)
url='https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
browser.get(url)

userElem = browser.find_element('id' ,'identifierId')
userElem.send_keys(mail)
nextElem = browser.find_element('id' ,'identifierNext')
nextElem.click()
time.sleep(3)

passElem =browser.find_element('id','password')
passElem.send_keys(password)
nextElem =browser.find_element('id','passwordNext')
nextElem.click()
time.sleep(3)

htmlElem=browser.find_element_by_tag_name('html')
htmlElem.send_keys('c')
htmlElem.send_keys('recipients') #we could also make separate variables for recipient, body and subject 
htmlElem.send_keys(Keys.TAB)
htmlElem.send_keys('subject is...')
htmlElem.send_keys(Keys.TAB)
htmlElem.send_keys('THe body of the email...')
htmlElem.send_keys(Keys.TAB)
htmlElem.send_keys(Keys.ENTER)
