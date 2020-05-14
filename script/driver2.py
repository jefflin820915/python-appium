from selenium import webdriver
driver = webdriver.Firefox()

# 需下載 driver 才能用 http://www.seleniumhq.org/download/ 
# 若 geckodriver 有在 PATH 中， firefox 可不帶路徑參數
driver = webdriver.Firefox(executable_path=r'.\driver\geckodriver.exe')
driver = webdriver.Chrome('/path/to/chromedriver')
driver = webdriver.Ie('/path/to/Iedriver')

# 可更改 firefox 的 profile
profile = webdriver.FirefoxProfile()
profile.native_events_enabled = True
driver = webdriver.Firefox(profile)

# 目前網址
driver.current_url

# 截圖
driver.save_screenshot('/Screenshots/foo.png')

# 原始碼 driver.page_source
with open('test.html','wb') as f:
    f.write(driver.page_source.encode('utf-8'))

# 標題
driver.title

# 重新整理
driver.refresh()

# 關閉目前視窗
driver.close()

# 結束全部視窗
driver.quit()