import unittest	#導入單元測試框架
from script.common.driver import get_driver
from time import sleep	#從time模組裡面導入sleep函數
from appium.webdriver.common.touch_action import TouchAction	#導入Touch模組
class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):	#所有用例執行前,執行一次,	def,define,用來聲明函數
		self.driver = get_driver()
	
	@classmethod	
	def tearDownClass(self):	#所有用例執行後,執行一次
		self.driver.quit()

	def test_setting_to_about(self):	#setting頁面到about頁面
		
		el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.RelativeLayout/android.widget.ImageView")
		el1.click()	#點擊Setting
		el2 = self.driver.find_element_by_id("com.tolka.multimediachat:id/about")
		el2.click()	#點擊about
		
		sleep(3)
		
		el3 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el3.click()	#點擊上一頁
		
		sleep(3)
	
		el4 = self.driver.find_element_by_id("com.tolka.multimediachat:id/get_more_features")
		el4.click()	#點擊get_more_features
		
		sleep(3)
		
		el5 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		is_displayed = el5.is_displayed
	
		self.assertTrue(is_displayed)
		if is_displayed:	#設定目標看到上一頁按鈕,已經證明有到上一頁
			self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back").click()
		
		sleep(3)

	def test_push_playbutton(self):
		el6 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_play")
		el6.click()	#點擊撥放鍵
		
		sleep(3)
		
		el7 = self.driver.find_element_by_id("com.tolka.multimediachat:id/logo")
		is_displayed = el7.is_displayed()
		self.assertTrue(is_displayed)
		
		if is_displayed:	#設定目標為LOGO,證明已經按了撥放器
			self.driver.find_element_by_id("com.tolka.multimediachat:id/logo").click()
		
		sleep(3)
	
	def test_login(self):	#登入頁面測試

		el14 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_play")
		el14.click()	#點擊撥放鍵

		el15 = self.driver.find_element_by_id("com.tolka.multimediachat:id/text_login")
		is_displayed= el15.is_displayed	#點擊播放清單頁面的get_more_features
		self.assertTrue(is_displayed)

		if is_displayed:	#目標設為登入的下一頁按鈕,證明有點擊撥放鍵
			self.driver.find_element_by_id("com.tolka.multimediachat:id/text_login").click()

		sleep(3)

	def test_input_number(self):	#輸入號碼

		el16 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_country_code")
		el16.click()	#點擊選國碼按鈕

		sleep(3)

		el17 = self.driver.find_element_by_id("com.tolka.multimediachat:id/button_search")
		el17.click()	#點擊搜尋國碼
		sleep(3)

		el18 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_search")
		el18.click()	#點擊搜尋框框
		el18.send_keys("886")	#輸入國碼
	
		sleep(3)
	
		el19 = self.driver.find_element_by_id("com.tolka.multimediachat:id/tv_item_country_body_name")
		el19.click()	#點擊找到的國碼

		sleep(3)

		el20 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_phone")
		el20.click()	#點擊輸入手機框框
		el20.send_keys("0999333444")	#輸入手機
		
		sleep(3)
		
		el21 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_next")
		el21.click()	#點擊下一頁
		
		sleep(3)

		el22 = self.driver.find_element_by_id("android:id/button1")
		el22.click()	#點擊notification message "確定"
		
		sleep(3)

		el23 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_password")
		el23.click()	#點擊輸入密碼框框
		el23.send_keys("12345678")	#輸入密碼
		sleep(3)

		el24 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_banner_next")
		el24.click()	#點擊下一頁

		sleep(15)
		
		TouchAction(self.driver)   .press(x=6, y=524)   .move_to(x=188, y=521)   .release()   .perform()
		#滑出播放清單
		el25 = self.driver.find_element_by_id("com.tolka.multimediachat:id/image_head")
		is_displayed = el25.is_displayed
		self.assertTrue(is_displayed)

		if is_displayed:	#設定目標為大頭貼,證明有滑出清單
			self.driver.find_element_by_id("com.tolka.multimediachat:id/image_head").click
		sleep(10)

	def test_push_group(self):	#點擊群組
		TouchAction(self.driver)   .press(x=588, y=499)   .move_to(x=563, y=499)   .release()   .perform()
		#關閉播放清單
		sleep(15)

		el26 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView[1]")
		el26.click()	#點擊第一個群組

		sleep(15)

		el29 = self.driver.find_element_by_id("com.tolka.multimediachat:id/chat")
		el29.click()	#點擊聊天按鈕
		
		sleep(15)

		el27 = self.driver.find_element_by_id("com.tolka.multimediachat:id/input_text")
		el27.click()	#點擊聊天輸入框框
		el27.send_keys("123213sfdads^$#@$#^(")	#輸入文字
		
		sleep(15)

		el30 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_sticker")
		el30.click()	#點擊貼圖按鈕

		sleep(15)

		el31 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.ImageView")
		el31.click()	#點擊貼圖

		sleep(15)

		el31.click()
		is_displayed = el31.is_displayed
		self.assertTrue(is_displayed)
		
		if is_displayed:	#目標設為提醒開關按鈕,證明在群組聊天室
			self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_notification")
	
	def test_auto_serch_input_number_serch_QR_CODE(self):	#邀請好友三種方式
		
		sleep(10)
		
		el32 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el32.click()	#點擊上一頁

		sleep(10)

		el33 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_sidemenu")
		el33.click()	#點擊humberger bar

		sleep(5)

		el34 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]")
		el34.click()	#點擊好友邀請

		sleep(5)

		el35 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_auto_invite")
		el35.click()	#點擊自動邀請

		sleep(5)

		el36 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_search_id")
		el36.click()	#點擊搜尋電話號碼

		sleep(5)

		el37 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_search_id")
		el37.click()	#點擊輸入號碼框框
		el37.send_keys("0999333444")	#輸入號碼
		
		sleep(10)

		el38 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_search")
		el38.click()	#點擊搜尋按鈕
		
		sleep(15)

		el42 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el42.click()	#點擊上一頁

		sleep(10)
		
		el39 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_qrcode")
		el39.click()	#點擊QR CODE

		sleep(15)

		el40 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_scan")
		el40.click()	#點擊QR CODE READER
		
		sleep(15)

		el41 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el41.click()	#點擊上一頁
		
		sleep(15)
		is_displayed = el41.is_displayed
		self.assertTrue(is_displayed)
		
		if is_displayed:	#目標設為QR CODE,證明回到上一頁QR CODE頁
			self.driver.find_element_by_id("com.tolka.multimediachat:id/image_qrcode")

	def group_icon_camera(self):	

		el43 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el43.click()	#點擊上一頁

		sleep(10)

		el44 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el44.click()	#點擊上一頁

		sleep(10)

		el45 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_sidemenu")
		el45.click()	#點擊humberger bar

		sleep(10)

		el46 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
		el46.click()	#點擊創建Group

		sleep(10)

		el47 = self.driver.find_element_by_id("com.tolka.multimediachat:id/image")
		el47.click()	#點擊大頭貼

		sleep(5)

		el48 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]")
		el48.click()	#點擊相機

		sleep(10)

		el49 = self.driver.find_element_by_id("com.asus.camera:id/button_capture")
		el49.click()	#點擊拍照

		sleep(15)

		el50 = self.driver.find_element_by_id("com.asus.camera:id/button_retake")
		el50.click() #點擊取消

		sleep(10)
		is_displayed = el50.is_displayed
		self.assertTrue(is_displayed)

		if is_displayed:	#目標設為拍照鍵,證明拍照完回到拍照模式
			self.driver.find_element_by_id("com.asus.camera:id/button_capture")
	
	def group_icon_phto(self):

		self.driver.back()

		sleep(10)

		el51 = self.driver.find_element_by_id("com.tolka.multimediachat:id/image")
		el51.click()

		sleep(10)

		el52 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]")
		el52.click()

		sleep(10)

		el53 = self.driver.find_element_by_id("com.android.documentsui:id/icon_mime")
		el53.click()

		sleep(10)

		el54 = self.driver.find_element_by_id("com.tolka.multimediachat:id/tv_use_photo")
		el54.click()

		sleep(10)
 
		is_displayed = el54.is_displayed
		self.assertTrue(is_displayed)
		
		if is_displayed :
			self.driver.find_element_by_id("com.tolka.multimediachat:id/image")

	def test_group(self):
		
		sleep(5)
		
		el39 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.ImageView[1]")
		el39.click()
		sleep(2)
		el40 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView[1]")
		el40.click
		sleep(2)
		el41 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.ImageView[1]")
		el41.click
		sleep(2)
		el42 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.ImageView[1]")
		el42.click
		sleep(2)
		el43 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.ImageView[1]")
		el43.click
		
		sleep(2)
		el44 = self.driver.find_element_by_id("com.tolka.multimediachat:id/et_groupname").click
		el44.send_keys("331zsfada###$sasd11#@@@")
		sleep(2)
		
		el45 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_clear")
		el45.click
		sleep(3)
		
		el46 = self.driver.find_element_by_id("com.tolka.multimediachat:id/et_groupname")
		el46.click
		el46.send_keys("331zsfada###$sasd11#@@@")
		sleep(3)

		el47 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_ok")
		el47.click
		is_displayed = el47.is_displayed
		self.assertTrue(is_displayed)
		
		if is_displayed:
			self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_play")


def suite():	#	Testsuite:多項測試用例集合在一起

    tests = [
		'test_setting_to_about',
		'test_push_playbutton',
		'test_login',
		'test_input_number',
		'test_push_group',
		'test_auto_serch_input_number_serch_QR_CODE',
		'group_icon_camera',
		'group_icon_phto',
		'test_group',
		]	
    return unittest.TestSuite(map(LoginTest, tests))