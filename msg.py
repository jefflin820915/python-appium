import unittest
from script.common.driver import get_driver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
class msg_Test(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.driver = get_driver()
	
	@classmethod	
	def tearDownClass(self):
		self.driver.quit()

	def msg_Test(self):

		el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.RelativeLayout/android.widget.ImageView")
		el1.click()
    el1.send.keys("123")

def suite():

    tests = [
		'msg_Test',
		]
    return unittest.TestSuite(map(msg_Test, tests))