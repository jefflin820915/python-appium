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
	
	def test_is_in_unlogin_main_palsge(self):
		self.driver.wait_activity("com.tolka.multimediachat.activity.UnloginMainActivity", 10)
		el1 = self.driver.find_element_by_id("com.tolka.multimediachat:id/text1")
		self.assertTrue(el1.is_displayed())

	def test_contact_to_login(self):
		el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[1]/android.widget.RelativeLayout/android.widget.ImageView")
		el1.click()

		el2 = self.driver.find_element_by_id("com.tolka.multimediachat:id/door")
		el2.click()

		el3 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_country_code")
		is_displayed = el3.is_displayed()
		self.assertTrue(is_displayed)

		if is_displayed:
			self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back").click()

	def test_sidebar_to_login(self):
		TouchAction(self.driver)   .press(x=13, y=711)   .move_to(x=700, y=706)   .release()   .perform()
	
		el1 = self.driver.find_element_by_id("com.tolka.multimediachat:id/text_login")
		el1.click()

		el2 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_country_code")
		is_displayed = el2.is_displayed()
		self.assertTrue(is_displayed)

		if is_displayed:
			self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back").click()

def suite():
    tests = [
		'test_is_in_unlogin_main_page',
		'test_contact_to_login',
		'test_sidebar_to_login',
    ]
    return unittest.TestSuite(map(LoginTest, tests))
