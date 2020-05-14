import unittest
from script.common.driver import get_driver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

class LoginTest(unittest.TestCase):

	@classmethod	
	def setUpClass(self):
		self.driver = get_driver()
	
	@classmethod	
	def tearDownClass(self):
		self.driver.quit()

	def Login_Test(self):

		el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.RelativeLayout/android.widget.ImageView")
		el1.click()
		
		sleep(2)

		el2 = self.driver.find_element_by_id("com.tolka.multimediachat:id/transfer_code")
		el2.click()
		
		sleep(3)
		
		el3 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_country_code")
		el3.click()
		
		sleep(3)

		el4 = self.driver.find_element_by_id("com.tolka.multimediachat:id/button_search")
		el4.click()
		
		sleep(2)
		
		el5 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_search")
		el5.click()
		el5.send_keys("886")

		sleep(3)	

		el6 = self.driver.find_element_by_id("com.tolka.multimediachat:id/tv_item_country_body_name")
		el6.click()
		
		sleep(2)

		el7 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_phone")
		el7.click()
		el7.send_keys("0999333444")

		sleep(3)
	
		el8 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_next")
		el8.click()

		sleep(3)

		el10 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_password")
		el10.click()
		el10.send_keys("12345678")

		sleep(3)

		el11 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_banner_next")
		el11.click()

		sleep(15)

		el12 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.RelativeLayout/android.widget.ImageView")
		el12.click()

		sleep(5)
		
		el13 = self.driver.find_element_by_id("com.tolka.multimediachat:id/user_id")
		is_displayed = el13.is_displayed
		self.assertTrue(is_displayed)

		if is_displayed:
			self.driver.find_element_by_id("com.tolka.multimediachat:id/user_id")

		sleep(3)

	def Add_friend_Auto_add(self):
		
		el21 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[1]/android.widget.RelativeLayout/android.widget.ImageView")
		el21.click()

		sleep(2)

		el14 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_sidemenu")
		el14.click()

		sleep(2)
		
		try:
			el22 = self.driver.find_element_by_xpath("//*[@text='邀請朋友']")
			el22.click()
		except:
			el78 = self.driver.find_element_by_xpath("//*[@text='Invite friend']")
			el78.click()
		
		sleep(2)

		el15 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_auto_invite")
		el15.click()

		sleep(2)
		
		self.driver.back()

		el16 = self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout")
		is_displayed = el16.is_displayed
		self.assertTrue(is_displayed)
		
		if is_displayed:
			self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout")
	
	def Add_friend_Number_add(self):
		
		el17 = self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout")

		TouchAction(self.driver).long_press(el17).perform()
		
		sleep(5)

		el18 = self.driver.find_element_by_id("com.tolka.multimediachat:id/delete")
		el18.click()
		
		sleep(5)

		el19 = self.driver.find_element_by_id("android:id/button1")
		el19.click()
		
		sleep(3)

		el20 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_sidemenu")
		el20.click()

		sleep(2)
		
		try:
			el21 = self.driver.find_element_by_xpath("//*[@text='邀請朋友']")
			el21.click()
		except:
			el79 = self.driver.find_element_by_xpath("//*[@text='Invite friend']")
			el79.click()

		sleep(2)

		el24 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_search_id")
		el24.click()

		sleep(2)

		el25 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_country_code")
		el25.click()

		sleep(2)

		el26 = self.driver.	find_element_by_id("com.tolka.multimediachat:id/button_search")
		el26.click()

		sleep(2)

		el27 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_search")
		el27.click()
		el27.send_keys("886")

		sleep(2)

		el28 = self.driver.find_element_by_id("com.tolka.multimediachat:id/tv_item_country_body_name")
		el28.click()

		sleep(2)

		el29 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_search_id")
		el29.click()
		el29.send_keys("0900466264")
		
		sleep(2)

		el30 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_clear")
		el30.click()

		sleep(2)
		
		el31 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_search_id")
		el31.click()
		el31.send_keys("0900466264")
		
		sleep(3)

		el32 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_search")
		el32.click()

		sleep(3)

		el33 = self.driver.find_element_by_id("com.tolka.multimediachat:id/info_text")
		el33.click()

		sleep(3)

		el34 = self.driver.find_element_by_id("com.tolka.multimediachat:id/invite")
		el34.click()

		sleep(3)

		el35 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el35.click()

		sleep(3)
		
		el36 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el36.click()

		sleep(3)

		el37 = self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout")
		is_displayed = el37.is_displayed
		self.assertTrue(is_displayed)

		if is_displayed:
			self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout")
		
		sleep(2)

	def create_group(self):
		
		el38 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_sidemenu")
		el38.click()

		sleep(5)
		
		try:
			el39 = self.driver.find_element_by_xpath("//*[@text='建立群組']")
			el39.click()
		except:
			el80 = self.driver.find_element_by_xpath("//*[@text='Create group']")
			el80.click()

		sleep(5)


		el41 = self.driver.find_element_by_id("com.tolka.multimediachat:id/et_groupname")
		el41.click()
		el41.send_keys("tolkaqa")
		
		sleep(5)

		el42 = self.driver.find_element_by_id("com.tolka.multimediachat:id/image")
		el42.click()

		sleep(5)

		el43 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]")
		el43.click()

		sleep(10)

		el44 = self.driver.find_element_by_id("com.asus.camera:id/button_capture")
		el44.click()

		sleep(5)

		el45 = self.driver.find_element_by_id("com.asus.camera:id/button_used")
		el45.click()

		sleep(5)

		el46 = self.driver.find_element_by_id("com.tolka.multimediachat:id/tv_use_photo")
		el46.click()

		sleep(5)

		el47 = self.driver.find_element_by_id("com.tolka.multimediachat:id/iv_contact_selected")
		el47.click()

		sleep(5)

		el48 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_ok")
		el48.click()

		sleep(5)

		el49 = self.driver.find_element_by_xpath("//*[@text='tolkaqa']")
		is_displayed = el49.is_displayed
		self.assertTrue(is_displayed)
		
		if is_displayed:
			self.driver.find_element_by_xpath("//*[@text='tolkaqa']")

		sleep(3)
	
	def edit_nickname(self):
		
		try:
			el50 = self.driver.find_element_by_xpath("//*[@text='設定']")
			el50.click()
		except:
			el81 = self.driver.find_element_by_xpath("//*[@text='Setting']")
			el81.click()
		
		sleep(2)

		el51 = self.driver.find_element_by_id("com.tolka.multimediachat:id/user_nickname")
		el51.click()

		sleep(3)

		el52 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_input")
		el52.click()
		el52.send_keys("1234@@@@+saddad71****%&&&")

		sleep(3)

		el53 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_clear")
		el53.click()

		sleep(3)

		el54 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_input")
		el54.click()
		el54.send_keys("1234@@@@+saddad71****%&&&")

		sleep(3)
		
		el55 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_save")
		el55.click()

		sleep(3)

		el56 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el56.click()

		sleep(3)

		el57 = self.driver.find_element_by_xpath("//*[@text='1234@@@@+saddad71****%&&&']")
		is_displayed = el57.is_displayed
		self.assertTrue(is_displayed)

		if is_displayed:
			self.driver.find_element_by_xpath("//*[@text='1234@@@@+saddad71****%&&&']")

		sleep(3)

	def logout_login(self):
		
		TouchAction(self.driver)   .press(x=555, y=1107)   .move_to(x=594, y=754)   .release()   .perform()

		sleep(5)

		el58 = self.driver.find_element_by_id("com.tolka.multimediachat:id/logout")
		el58.click()

		sleep(5)

		el59 = self.driver.find_element_by_id("android:id/button1")
		el59.click()

		sleep(15)	

		el60 = self.driver.find_element_by_id("com.tolka.multimediachat:id/door")
		el60.click()

		sleep(5)

		el61 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_country_code")
		el61.click()

		sleep(5)

		el62 = self.driver.find_element_by_id("com.tolka.multimediachat:id/button_search")
		el62.click()

		sleep(5)

		el63 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_search")
		el63.click()
		el63.send_keys("886")

		sleep(5)

		el64 = self.driver.find_element_by_id("com.tolka.multimediachat:id/tv_item_country_body_name")
		el64.click()

		sleep(5)

		el65 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_phone")
		el65.click()
		el65.send_keys("0999333444")

		sleep(8)		

		el66 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_next")
		el66.click()
		
		sleep(10)
 
		el68 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_password")
		el68.click()
		el68.send_keys("12345678")

		sleep(5)

		el69 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_banner_next")
		el69.click()

		sleep(12)
		
		el70 = self.driver.find_element_by_xpath("//*[@text='tolkaqa']")

		TouchAction(self.driver).long_press(el70).perform()

		sleep(5)

		el71 = self.driver.find_element_by_id("com.tolka.multimediachat:id/leave")
		el71.click()

		sleep(5)

		el72 = self.driver.find_element_by_id("android:id/button1")
		el72.click()
		
		sleep(5)

		el73 = self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout")

		TouchAction(self.driver).long_press(el73).perform()

		sleep(5)

		el74 = self.driver.find_element_by_id("com.tolka.multimediachat:id/delete")
		el74.click()

		sleep(5)

		el75 = self.driver.find_element_by_id("android:id/button1")
		el75.click()

		sleep(5)

		el76 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.RelativeLayout")
		el76.click()

		sleep(5)

		TouchAction(self.driver)   .press(x=555, y=1107)   .move_to(x=594, y=754)   .release()   .perform()

		sleep(5)

		el77 = self.driver.find_element_by_xpath("//*[@text='+886999333444']")
		is_displayed = el77.is_displayed
		self.assertTrue(is_displayed)

		if is_displayed:
			self.driver.find_element_by_xpath("//*[@text='+886999333444']")
	
def suite():

    tests = [
		'Login_Test',
		'Add_friend_Auto_add',
		'Add_friend_Number_add',
		'create_group',
		'edit_nickname',
		'logout_login',
		]
    return unittest.TestSuite(map(LoginTest, tests))