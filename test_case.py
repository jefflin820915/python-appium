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
		el5.click
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

		el9 = self.driver.find_element_by_id("android:id/button1")
		el9.click()

		sleep(3)

		el10 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_password")
		el10.click()
		el10.send_keys("12345678")

		sleep(3)

		el11 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_banner_next")
		el11.click()

		sleep(10)

		el12 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.RelativeLayout/android.widget.ImageView")
		el12.click()

		sleep(5)
		
		el13 = self.driver.find_element_by_id("com.tolka.multimediachat:id/user_id")
		is_displayed = el13.is_displayed
		self.assertTrue(is_displayed)

		if is_displayed:
			self.driver.find_element_by_id("com.tolka.multimediachat:id/user_id").click

		sleep(2)

	def Add_friend_Auto_add(self):
		
		el21 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[1]/android.widget.RelativeLayout/android.widget.ImageView")
		el21.click()

		sleep(2)

		el14 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_sidemenu")
		el14.click()

		sleep(2)
		
		el22 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]")
		el22.click()

		sleep(2)

		el15 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_auto_invite")
		el15.click()

		sleep(2)
		
		self.driver.back()

		el16 = self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout")
		is_displayed = el16.is_displayed
		self.assertTrue(is_displayed)
		
		if is_displayed:
			self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout").click
	
	def Add_friend_Number_add(self):
		
		el17 = self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout")

		TouchAction(self.driver).long_press(el17).perform()
		
		sleep(3)

		el18 = self.driver.find_element_by_id("com.tolka.multimediachat:id/delete")
		el18.click()
		
		sleep(3)

		el19 = self.driver.find_element_by_id("android:id/button1")
		el19.click()
		
		sleep(3)

		el20 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_sidemenu")
		el20.click()		
		
def suite():

    tests = [
		'Login_Test',
		'Add_friend_Auto_add',
		'Add_friend_Number_add',
		]	
    return unittest.TestSuite(map(LoginTest, tests))