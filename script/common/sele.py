from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys 

import time 
import os 

browser = webdriver.Chrome('chromedriver.exe') 

browser.get('http://www.google.com.tw/') 

elem = browser.find_element_by_id("tsf").click()
elem.send_keys('1234567')

time.sleep(1) 

browser.close()
