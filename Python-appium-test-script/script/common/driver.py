import os

from appium import webdriver

server_url = 'http://127.0.0.1:4723/wd/hub'

config = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'platformVersion': '8.0.0',
    'app': os.path.abspath('VHomeTV_phone_20200506_v0.5.4.apk'),
    #dev的activity : 'com.tolka.woctv.activity.s'
    'appWaitActivity': 'com.tolka.woctv.activity.t',
    'unicodeKeyboard': 'false',
    'resetKeyboard': 'false',
    'automationName': 'uiautomator2',
    'newCommandTimeout': '60000',
}

def get_driver():
	return webdriver.Remote(server_url, config)
