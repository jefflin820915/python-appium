import unittest
from script.common.driver import get_driver
from time import sleep
class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
    
        self.driver = get_driver()

	@classmethod
	def tearDownClass(self):
        self.driver.quit()

	def test_inpiut_meg(self):
       
        el14 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_play")
        el14.click()

        sleep(3)

		el15 = self.driver.find_element_by_id("com.tolka.multimediachat:id/text_login")
        el15.click()
		
        sleep(3)

		el16 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_country_code")
		el16.click()

		sleep(3)

        el17 = self.driver.find_element_by_id("com.tolka.multimediachat:id/button_search")
		el17.click()
		sleep(3)

		el18 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_search")
		el18.click()
		el18.send_keys("886")

		sleep(3)

		el19 = self.driver.find_element_by_id("com.tolka.multimediachat:id/tv_item_country_body_name")
		el19.click()

		sleep(3)

		el20 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_phone")
		el20.click()
		el20.send_keys("0999333444")
		
		sleep(3)
		
		el21 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_next")
		el21.click()
		
		sleep(3)

		el22 = self.driver.find_element_by_id("android:id/button1")
		el22.click()
		
		sleep(3)

		el23 = self.driver.find_element_by_id("com.tolka.multimediachat:id/edit_password")
		el23.click()
		el23.send_keys("12345678")
		sleep(3)

		el24 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_banner_next")
		el24.click()

        sleep(10)

        el25 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]/android.widget.RelativeLayout/android.widget.ImageView")
        el25.click()

        sleep(3)

        el26 = self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout")
        el26.click()

        sleep(3)

        el27 = self.driver.find_element_by_id("com.tolka.multimediachat:id/input_text")
        el27.click()
        for el27 in range(0, 500, 1):
         print('500')
        
        sleep(10)
        
        el28 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
        el28.click()

        el29 = self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout")
        is_displayed = el28.is_displayed
        self.assertTrue(is_displayed)
        if is_displayed:
            self.driver.find_element_by_id("com.tolka.multimediachat:id/contact_item_layout").click()
        


def suite():
    tests = [
		'test_input_meg',
    ]
    return unittest.TestSuite(map(LoginTest, tests))
