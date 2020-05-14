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

	def test_setting_to_about(self):
		
		el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.RelativeLayout/android.widget.ImageView")
		el1.click()
		el2 = self.driver.find_element_by_id("com.tolka.multimediachat:id/about")
		el2.click()
		
		sleep(3)
		
		el3 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el3.click()
		
		sleep(3)
		
		el4 = self.driver.find_element_by_id("com.tolka.multimediachat:id/get_more_features")
		el4.click()
		
		sleep(3)
		
		el5 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_back")
		el5.click()
		
		sleep(3)
		
		el6 = self.driver.find_element_by_id("com.tolka.multimediachat:id/btn_play")
		el6.click()
		
		sleep(3)
		el7 = self.driver.find_element_by_id("com.tolka.multimediachat:id/iv_item_group_toggle")
		el7.click()
		
		sleep(3)
		
		el8 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ImageView")
		el8.click()
		
		sleep(3)

		el9 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.ImageView")
		el9.click()
		
		sleep(3)
		
		el10 = self.driver.find_element_by_id("com.tolka.multimediachat:id/iv_item_group_toggle")
		el10.click()
		
		sleep(3)
		
		el11 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")
		el11.click()
		
		sleep(3)
		
		el12 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")
		el12.click()
		
		sleep(3)
		
		el13 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.ImageView")
		el13.click()
		
		sleep(3)
		
		el14 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.ImageView")
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

		sleep(30)

		el25 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout")
		self.assertTrue(el25.is_displayed())

def suite():
    tests = [
		'test_setting_to_about',
    ]
    return unittest.TestSuite(map(LoginTest, tests))
