import unittest
from script.common.driver import get_driver
from time import sleep
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
import uiautomator2 as u2



class GAAutoTestLogin(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = get_driver()
	
	# @classmethod
	# def tearDownClass(cls):
	# 	cls.driver.quit()
	
	
	def testLogin(self):

		sleep(7)

		gologinBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_log_in")
		gologinBtn.click()

		sleep(5)
	
		tvTerms = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_terms")
		tvTerms.click()
	
		sleep(4)
	
		phoneBack = self.driver.back()
	
		sleep(3)
	
		mailEditView = self.driver.find_element_by_id("tv.tolka.vhometv:id/edit_id")
		mailEditView.click()
		mailEditView.send_keys("zgg71935@bcaoo.com")
	
		sleep(3)
	
		passwordEditView = self.driver.find_element_by_id("tv.tolka.vhometv:id/edit_password")
		passwordEditView.click()
		passwordEditView.send_keys("aaa123")
	
		sleep(3)
	
		phoneBack = self.driver.back()
	
		sleep(3)
	
		loginBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_original")
		loginBtn.click()
	
		sleep(7)
	
		clickAvatar = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_avatar")
		clickAvatar.click()
	
		sleep(60)
	
		settingBackBtn = BackBtn(self)
	
		sleep(2)
	
		commnetLater = self.driver.find_element_by_id("android:id/button2")
		commnetLater.click()
	
		sleep(2)
	
		clickAvatar = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_avatar")
		clickAvatar.click()
	
		sleep(60)
	
		settingBackBtn = BackBtn(self)
	
		sleep(2)
	
		goComment = self.driver.find_element_by_id("android:id/button1")
		goComment.click()
	
		sleep(2)
	
		searchBar = self.driver.find_element_by_id("tv.tolka.vhometv:id/edit_search_bar")
		searchBar.click()
	
		sleep(3)
	
		searchBar.send_keys("東森")
	
		sleep(4)
	
		TouchAction(self.driver).tap(x=988, y=1811).perform()
	
		sleep(4)
	
	
		searchBarBack = BackBtn(self)
	
		sleep(6)
	
		allCatrgoryBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/ll_all_category_area")
	
		allCatrgoryBtn.click()
	
		sleep(3)
	
		atrgoryOne = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView")
		atrgoryOne.click()
	
		sleep(3)
	
		atrgoryOneBackBtn = BackBtn(self)
	
		sleep(3)
	
		atrgoryTwo = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView")
		atrgoryTwo.click()
	
		sleep(3)
	
		atrgoryTwoBackBtn = BackBtn(self)
	
		sleep(3)
	
		atrgoryThree = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.TextView")
		atrgoryThree.click()
	
		sleep(3)
	
		atrgoryThreeBackBtn = BackBtn(self)
	
		sleep(3)
	
		atrgoryFour = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.TextView")
		atrgoryFour.click()
	
		sleep(3)
	
		atrgoryFourBackBtn = BackBtn(self)
	
		sleep(3)
	
		allCatrgoryBackBtn = BackBtn(self)
	
		sleep(6)
	
		catrgoryVideoOne = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
		catrgoryVideoOne.click()
	
		sleep(3)
	
		catrgoryVideoOneBackBtn = BackBtn(self)
	
		sleep(3)
	
		catrgoryVideoTwo = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
		catrgoryVideoTwo.click()
	
		sleep(3)
	
		catrgoryVideoTwoBackBtn = BackBtn(self)
	
		sleep(4)
	
		SwipeUp(self,n=6)
	
		sleep(3)
	
		catrgoryVideoThree = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
		catrgoryVideoThree.click()
	
		sleep(3)
	
		catrgoryVideoThreeBackBtn = BackBtn(self)
	
		sleep(4)
	
		catrgoryVideoFour = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
		catrgoryVideoFour.click()
	
		sleep(3)
	
		catrgoryVideoFourBackBtn = BackBtn(self)
	
		sleep(3)
	
		SwipeDown(self,n=6)
	
		sleep(3)
	
		SwipeUp(self,n=6)
	
		sleep(3)
	
		SwipeDown(self,n=6)
	
		sleep(3)
	
		catrgoryVideoOne = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
		catrgoryVideoOne.click()
	
		sleep(7)
	
		favoriteBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/pt_img_fav")
		favoriteBtn.click()
	
		sleep(3)
	
		fullScreenBtn = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView")
		fullScreenBtn.click()
	
		sleep(6)
	
		screenTap = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View")
		screenTap.click()
	
		sleep(0.3)
	
		TouchAction(self.driver).tap(x=1362, y=95).perform()
	
		sleep(3)
	
		screenTap = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View")
		screenTap.click()
	
		sleep(0.3)
	
		TouchAction(self.driver).tap(x=1507, y=95).perform()
	
		sleep(3)
	
		favoriteBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/pt_img_fav")
		favoriteBtn.click()
	
		sleep(3)
	
		fullScreenBtn = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView")
		fullScreenBtn.click()
	
		sleep(2)
	
		TouchAction(self.driver).tap(x=1752, y=136).perform()
	
		sleep(3)
	
		noResumeDiaLogCheckBox = self.driver.find_element_by_id("tv.tolka.vhometv:id/checkbox")
		noResumeDiaLogCheckBox.click()
	
		sleep(2)
	
		closePlayerOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/text_ok")
		closePlayerOkBtn.click()
	
		sleep(2)
	
		catrgoryVideoOne = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
		catrgoryVideoOne.click()
	
		sleep(7)
	
		closePlayer = self.driver.back()
	
		sleep(3)
	
		myFavorite = self.driver.find_element_by_id("tv.tolka.vhometv:id/ll_favorite_area")
		myFavorite.click()
		
		sleep(3)
	
		favoriteManage = self.driver.find_element_by_id("tv.tolka.vhometv:id/text_manage")
		favoriteManage.click()
	
		sleep(3)
	
		favoriteCheckBox = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.CheckBox")
		favoriteCheckBox.click()
	
		sleep(2)
	
		favoriteAllCheckBox = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.CheckBox")
		favoriteAllCheckBox.click()
	
		sleep(2)
	
		favoriteDelChannel = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
		favoriteDelChannel.click()
	
		sleep(3)
	
		favoriteFinishBtn = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.TextView")
		favoriteFinishBtn.click()
	
		sleep(3)
	
		favoriteBackBtn = BackBtn(self)
	
		sleep(6)
	
		EpgBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/ll_epg_area")
		EpgBtn.click()
	
		sleep(3)
	
		epgSearch = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_search")
		epgSearch.click()
	
		sleep(3)
	
		pgSearchEidtView = self.driver.find_element_by_id("tv.tolka.vhometv:id/et_input")
		pgSearchEidtView.click()
		pgSearchEidtView.send_keys("新聞")	
		sleep(3)
	
		honeBack = self.driver.back()	
		
		sleep(3)	
		
		pgSearchOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/text_ok")
		
		pgSearchOkBtn.click()	
		
		sleep(2)	
		
		epgBackBtn = BackBtn(self)	
		
		sleep(6)	
		
		watchHistory = self.driver.find_element_by_id("tv.tolka.vhometv:id/ll_history_area")
		
		watchHistory.click()	
		
		sleep(3)	
		
		watchHistoryManage = self.driver.find_element_by_id("tv.tolka.vhometv:id/text_manage")
		
		watchHistoryManage.click()	
		
		sleep(3)	
		
		watchHistoryCheckBox = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.CheckBox")
		
		watchHistoryCheckBox.click()	
		
		sleep(2)	
		
		watchHistoryAllCheckBox = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.CheckBox")
		
		watchHistoryAllCheckBox.click()	
		
		sleep(2)	
		
		watchHistoryDelChannel = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
		
		watchHistoryDelChannel.click()	
		
		sleep(6)	
		
		watchHistoryFinishBtn = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.TextView")
		
		watchHistoryFinishBtn.click()	
		
		sleep(3)	
		
		watchHistoryBackBtn = BackBtn(self)	
		
		sleep(6)	
		
		clickAvatar = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_avatar")
		
		clickAvatar.click()	
		
		sleep(3)	
		
		shareApp = self.driver.find_element_by_id("tv.tolka.vhometv:id/share_app_title")
		
		shareApp.click()	
		
		sleep(2)	
		
		phoneBack = self.driver.back()	
		
		sleep(2)	
		
		goComment = self.driver.find_element_by_id("tv.tolka.vhometv:id/go_comment_title")
		
		goComment.click()	
		
		sleep(3)	
		
		phoneBack = self.driver.back()	
		
		sleep(2)	
		
		goFaceBook = self.driver.find_element_by_id("tv.tolka.vhometv:id/go_fb_title")
		
		goFaceBook.click()	
		
		sleep(3)	
		
		phoneBack = self.driver.back()	
		
		sleep(2)	
		
		goTwitter = self.driver.find_element_by_id("tv.tolka.vhometv:id/go_twitter_title")
		
		goTwitter.click()	
		
		sleep(3)	
		
		phoneBack = self.driver.back()	
		
		sleep(2)	
		
		goInstagram = self.driver.find_element_by_id("tv.tolka.vhometv:id/go_ig_title")
		
		goInstagram.click()	
		
		sleep(3)	
		
		phoneBack = self.driver.back()	
		
		sleep(2)	
		
		TouchAction(self.driver)   .press(x=584, y=1412)   .move_to(x=529, y=988)   .release()   .perform()	
		
		sleep(2)	
		
		supportBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/support_title")
		
		supportBtn.click()	
		
		sleep(2)	
		
		phoneBack = self.driver.back()	
		
		sleep(2)	
		
		phoneBack = self.driver.back()	
		
		sleep(2)	
		
		aboutBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/about_title")
		
		aboutBtn.click()	
		
		sleep(2)	
		
		aboutBackBtn = BackBtn(self)	
		
		sleep(2)	
		
		regionBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/region_title")
		
		regionBtn.click()	
		
		sleep(2)	
		
		regionInUSABtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/option_usa")
		
		regionInUSABtn.click()	
		
		sleep(2)	
		
		regionOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_original")
		
		regionOkBtn.click()	
		
		sleep(2)	
		
		regionBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/region_title")
		
		regionBtn.click()	
		
		sleep(2)	
		
		regionInOther = self.driver.find_element_by_id("tv.tolka.vhometv:id/option_others")
		
		regionInOther.click()	
		
		sleep(2)	
		
		regionOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_original")
		
		regionOkBtn.click()	
		
		sleep(2)	
		
		passwordBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/password_title")
		
		passwordBtn.click()	
		
		sleep(2)	
		
		passwordEditView = self.driver.find_element_by_id("tv.tolka.vhometv:id/edit_password")
		
		passwordEditView.click()
		
		passwordEditView.send_keys("aaa123")	
		
		sleep(2)	
		
		phoneBack = self.driver.back()	
		
		passwordOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/btn_ok")
		
		passwordOkBtn.click()	
		
		sleep(3)	
		
		newPasswordEditView = self.driver.find_element_by_id("tv.tolka.vhometv:id/et_input_one")
		
		newPasswordEditView.click()
		
		newPasswordEditView.send_keys("aaa123")	
		
		sleep(2)	
		
		TouchAction(self.driver).tap(x=996, y=1824).perform()	
		
		sleep(2)	
		
		againCheckNewPassword = self.driver.find_element_by_id("tv.tolka.vhometv:id/et_input_two")
		
		againCheckNewPassword.click()
		
		againCheckNewPassword.send_keys("aaa123")	
		
		sleep(2)	
		
		phoneBack = self.driver.back()	
		
		sleep(2)	
		
		newPasswordOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_original")
		
		newPasswordOkBtn.click()	
		
		sleep(4)	
		
		backToSettingPage = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_original")
		
		backToSettingPage.click()	
		
		sleep(2)	
		
		logOutBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/logout_title")
		
		logOutBtn.click()	
		
		sleep(2)	
		
		logOutCancelBtn = self.driver.find_element_by_id("android:id/button2")
		
		logOutCancelBtn.click()	
		
		sleep(2)	
		
		logOutBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/logout_title")
		
		logOutBtn.click()	
		
		sleep(2)	
		
		logOutOkBtn = self.driver.find_element_by_id("android:id/button1")
		
		logOutOkBtn.click()	
		
		sleep(3)	

def SwipeUp(self,n):
	size = self.driver.get_window_size()
	x1 = size['width'] * 0.5
	y1 = size['height'] * 0.75
	y2 = size['height'] * 0.25

	for i in range (n):
		self.driver.swipe(x1,y1,x1,y2)

def SwipeDown(self,n):
	size = self.driver.get_window_size()
	x1 = size['width'] * 0.5
	y1 = size['height'] * 0.25
	y2 = size['height'] * 0.75

	for i in range(n):
		self.driver.swipe(x1,y1,x1,y2)

def GoLoginBack(self):
	goLoginBack = self.driver.find_element_by_id("tv.tolka.vhometv:id/iv_back")
	goLoginBack.click()

def GoLoginBtn(self):
	goLoginBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/btn_go_login")
	goLoginBtn.click()

def BackBtn(self):
	backBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_back")
	backBtn.click()


def suite():
    tests = [
		'testLogin',
    ]
    return unittest.TestSuite(map(GAAutoTestLogin, tests))