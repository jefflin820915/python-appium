import unittest
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome('chromedriver.exe')
browser.get('http://www.google.com.tw/')


el1 = browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
el1.send_keys('1234567')

sleep(1)

el2 = browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center[1]/input[1]")
el2.click()

sleep(1)

el3 = browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]")
el3.send_keys(Keys.CONTROL+'a')
el3.send_keys(Keys.DELETE)
el3.send_keys('18c8')
el3.send_keys(Keys.ENTER)

sleep(1)

el4 = browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]")
el4.send_keys(Keys.CONTROL+'a')
el4.send_keys(Keys.DELETE)
el4.send_keys('asasasas')
el4.send_keys(Keys.ENTER)

sleep(1)

el5 = browser.find_element_by_xpath("//*[@id='tsf']/div[2/dov[1]/div[2]/div[1]/div[1]/input[1]")
