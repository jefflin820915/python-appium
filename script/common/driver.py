import os   #導入OS模組

from appium import webdriver    #導入python版的appium(webdriver)模組

server_url = 'http://127.0.0.1:4723/wd/hub'

config = {  #定義驅動參數
    'platformName': 'Android',  #OS系統
    'deviceName': 'emulator-5554',  #裝置名
    'platformVersion': '6.0.1', #OS版本
    'app': os.path.abspath('Tolkachat_dev_1.4.3.apk'),  #APP
    'appWaitActivity': 'com.tolka.multimediachat.activity.UnloginMainActivity', #APP啟動Activity
    'noRest': False,  #每次打開APP,開啟/關閉重置
    'autoGrantPermissions': True,
}

def get_driver():
	return webdriver.Remote(server_url, config)