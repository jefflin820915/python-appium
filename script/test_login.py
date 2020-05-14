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

	def test_contact_to_login(self):
		TouchAction(self.driver).press(x=2, y=493).move_to(x=356, y=486).release().perform()
		sleep(3)
		TouchAction(self.driver).press(x=356, y=486).move_to(x=2, y=493).release().perform()
		sleep(3)
		

		el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[1]/android.widget.RelativeLayout/android.widget.ImageView")
		el1.click() # 元素
		
		el2 = self.driver.find_element_by_id("com.tolka.multimediachat:id/door")
		el2.click() # 點門圖示
		
		sleep(3)
		
		el3 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_country_code")
		self.assertTrue(el3.is_displayed()) # 點門圖示進去看裡面有甚麼能證明進去,國家碼

def suite():
    tests = [
		'test_contact_to_login',
    ]
    return unittest.TestSuite(map(LoginTest, tests))
