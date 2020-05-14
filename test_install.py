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

    def test_setting_install(self):
        
        self.driver.back()
        
        el1 = self.driver.find_element_by_accessibility_id("Apps")
        el1.click()
        
        TouchAction(self.driver)   .press(x=712, y=529)   .move_to(x=406, y=524)   .release()   .perform()
        
        TouchAction(self.driver)   .press(x=703, y=541)   .move_to(x=398, y=527)   .release()   .perform()

        TouchAction(self.driver)   .press(x=3, y=529)   .move_to(x=252, y=572)   .release()   .perform()
        
        TouchAction(self.driver)   .press(x=11, y=588)   .move_to(x=451, y=555)   .release()   .perform()

        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[8]")
        el2.click()

        TouchAction(self.driver)   .press(x=367, y=1028)   .move_to(x=367, y=958)   .release()   .perform()

        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout[5]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout")
        el3.click()

        el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout")
        is_displayed = el4.is_displayed()
        self.assertTrue(is_displayed)

        if is_displayed:
            self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
def suite():
    tests = [
        'test_install,'
    ]
    return unittest.TestSuite(map(LoginTest, tests))
        