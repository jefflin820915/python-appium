import unittest
from script.common.driver import get_driver
from time import sleep
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions



class GAAutoTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = get_driver()
	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
	
	

	def testUnLogin(self):
		
		self.driver = self.driver

		actions = TouchAction(self.driver)

		sleep(7)

		loginSkip = self.driver.find_element_by_id("tv.tolka.vhometv:id/btn_two")
		loginSkip.click()
		
		sleep(8)

		clickAvatar = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_avatar")
		clickAvatar.click()

		sleep(6)

		goLoginBtn = GoLoginBtn(self)
		
		sleep(4)

		goLoginBack = GoLoginBack(self)

		sleep(6)

		imageBackBtn = BackBtn(self)
		
		sleep(6)

		searchBar = self.driver.find_element_by_id("tv.tolka.vhometv:id/edit_search_bar")
		searchBar.click()

		sleep(3)

		searchBar.send_keys("東森")

		sleep(4)

		actions.tap(x=988, y=1811).perform()
	
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

		sleep(3)

		catrgoryVideoFour = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
		catrgoryVideoFour.click()

		sleep(3)

		catrgoryVideoFourBackBtn = BackBtn(self)

		sleep(3)

		moveToTopBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_up")
		moveToTopBtn.click()

		sleep(3)

		myFavorite = self.driver.find_element_by_id("tv.tolka.vhometv:id/ll_favorite_area")
		myFavorite.click()

		sleep(4)

		goLoginBtn = GoLoginBtn(self)

		sleep(4)

		goLoginBack = GoLoginBack(self)

		sleep(4)

		myFavoriteBackBtn = BackBtn(self)

		sleep(6)

		tvEPG = self.driver.find_element_by_id("tv.tolka.vhometv:id/ll_epg_area")
		tvEPG.click()

		sleep(3)

		tvListDialog = self.driver.find_element_by_id("android:id/button1")
		tvListDialog.click()

		sleep(6)


		watchHistory = self.driver.find_element_by_id("tv.tolka.vhometv:id/ll_history_area")
		watchHistory.click()

		sleep(3)

		goLoginBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/btn_go_login")
		goLoginBtn.click()

		sleep(2)

		goLoginBack = self.driver.find_element_by_id("tv.tolka.vhometv:id/iv_back")
		goLoginBack.click()

		sleep(3)

		watchHistoryBackBtn = BackBtn(self)

		sleep(6)

		videoOne = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
		videoOne.click()
		
		sleep(7)

		favoriteBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/pt_img_fav")
		favoriteBtn.click()

		sleep(3)

		favoriteLoginDiaLog = self.driver.find_element_by_id("android:id/button1")
		favoriteLoginDiaLog.click()
		
		sleep(6)

		goLoginBack = GoLoginBack(self)

		sleep(3)

		fullScreenBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/pt_fullscreen")
		fullScreenBtn.click()

		sleep(3)

		screenTap = self.driver.find_element_by_id("tv.tolka.vhometv:id/video_view")
		screenTap.click()

		sleep(0.2)

		fullScreenFavBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/lan_fav")
		fullScreenFavBtn.click()

		sleep(3)

		fullScreenfavoriteDiaLog = self.driver.find_element_by_id("android:id/button1")
		fullScreenfavoriteDiaLog.click()

		sleep(3)

		goLoginBack = GoLoginBack(self)

		sleep(3)

		screenTap = self.driver.find_element_by_id("tv.tolka.vhometv:id/video_view")
		screenTap.click()

		sleep(0.2)

		fullScreenChangeWindowBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/lan_full")
		fullScreenChangeWindowBtn.click()

		sleep(3)

		fullScreenBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/pt_fullscreen")
		fullScreenBtn.click()

		sleep(1)

		fullScreenCloseBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/lan_back")
		fullScreenCloseBtn.click()

		sleep(3)

		noResumeDiaLogCheckBox = self.driver.find_element_by_id("tv.tolka.vhometv:id/checkbox")
		noResumeDiaLogCheckBox.click()

		sleep(2)

		closePlayerOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/text_ok")
		closePlayerOkBtn.click()
		
		sleep(1)

#----------------------------------------------------TestUnLogin---------------------------------------------------------#



#------------------------------------------------------TestLogin---------------------------------------------------------#

	def testLogin(self):

		sleep(7)

		gologinBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_log_in")
		gologinBtn.click()

		sleep(6)

		tvTerms = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_terms")
		tvTerms.click()

		sleep(6)

		phoneBack(self)

		sleep(3)

		mailEditView = self.driver.find_element_by_id("tv.tolka.vhometv:id/edit_id")
		mailEditView.click()
		mailEditView.send_keys("tvr47819@eoopy.com")

		sleep(3)

		passwordEditView = self.driver.find_element_by_id("tv.tolka.vhometv:id/edit_password")
		passwordEditView.click()
		passwordEditView.send_keys("aaa123")

		sleep(3)

		phoneBack(self)

		sleep(3)

		loginBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_original")
		loginBtn.click()

		sleep(35)
		
		#需要沒評價過的帳號才能做, dev跟pro時間不同,須改動 dev: 3min/6min  pro: 72min/144min

		clickAvatar = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_avatar")
		clickAvatar.click()

		sleep(180)

		settingBackBtn = BackBtn(self)

		sleep(6)

		commnetLater = self.driver.find_element_by_id("android:id/button2")
		commnetLater.click()

		sleep(3)

		clickAvatar = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_avatar")
		clickAvatar.click()

		sleep(360)

		settingBackBtn = BackBtn(self)

		sleep(6)

		goComment = self.driver.find_element_by_id("android:id/button1")
		goComment.click()

		sleep(4)

		phoneBack(self)

		sleep(4)

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

		moveToTopBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_up")
		moveToTopBtn.click()

		sleep(3)

		swipLeft(self,n=5)

		sleep(3)

		VideoOne = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
		VideoOne.click()

		sleep(7)

		screenTap = self.driver.find_element_by_id("tv.tolka.vhometv:id/youtube_player_view")
		screenTap.click()

		sleep(3)

		favoriteBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/pt_img_fav")
		favoriteBtn.click()

		sleep(3)

		fullScreenBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/pt_fullscreen")
		fullScreenBtn.click()

		sleep(6)

		screenTap = self.driver.find_element_by_id("tv.tolka.vhometv:id/video_view")
		screenTap.click()

		sleep(0.3)

		fullScreenFavBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/lan_fav")
		fullScreenFavBtn.click()

		sleep(3)

		screenTap = self.driver.find_element_by_id("tv.tolka.vhometv:id/video_view")
		screenTap.click()

		sleep(0.3)

		fullScreenChangeWindowBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/lan_full")
		fullScreenChangeWindowBtn.click()

		sleep(4)

		favoriteBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/pt_img_fav")
		favoriteBtn.click()

		sleep(4)

		fullScreenBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/pt_fullscreen")
		fullScreenBtn.click()

		sleep(1)

		fullScreenCloseBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/lan_back")
		fullScreenCloseBtn.click()
		
		sleep(3)

		noResumeDiaLogCheckBox = self.driver.find_element_by_id("tv.tolka.vhometv:id/checkbox")
		noResumeDiaLogCheckBox.click()

		sleep(2)

		closePlayerOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/text_ok")
		closePlayerOkBtn.click()

		sleep(3)

		swipRight(self,n=5)

		sleep(4)

		VideoOne = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
		VideoOne.click()

		sleep(8)

		channelReplayBtn = self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='節目回放']/android.widget.TextView")
		channelReplayBtn.click()

		sleep(6)

		channelReplayOne = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ImageView")
		channelReplayOne.click()
		
		sleep(7)

		closePlayer = self.driver.find_element_by_id("tv.tolka.vhometv:id/pt_back")
		closePlayer.click()

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

		favoriteAllCheckBox = self.driver.find_element_by_id("tv.tolka.vhometv:id/rl_select_all_area")
		favoriteAllCheckBox.click()

		sleep(2)

		favoriteDelChannel = self.driver.find_element_by_id("tv.tolka.vhometv:id/ll_remove_selected_area")
		favoriteDelChannel.click()

		sleep(10)

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

		epgSearchEidtView = self.driver.find_element_by_id("tv.tolka.vhometv:id/et_input")
		epgSearchEidtView.click()
		epgSearchEidtView.send_keys("新聞")

		sleep(4)

		phoneBack(self)

		sleep(3)

		epgSearchOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/text_ok")
		epgSearchOkBtn.click()

		sleep(3)

		epgBackBtn = BackBtn(self)

		sleep(8)

		watchHistory = self.driver.find_element_by_id("tv.tolka.vhometv:id/ll_history_area")
		watchHistory.click()

		sleep(3)

		watchHistoryManage = self.driver.find_element_by_id("tv.tolka.vhometv:id/text_manage")
		watchHistoryManage.click()

		sleep(3)

		watchHistoryCheckBox = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.CheckBox")
		watchHistoryCheckBox.click()

		sleep(2)

		watchHistoryAllCheckBox = self.driver.find_element_by_id("tv.tolka.vhometv:id/rl_select_all_area")
		watchHistoryAllCheckBox.click()

		sleep(2)

		watchHistoryDelChannel = self.driver.find_element_by_id("tv.tolka.vhometv:id/ll_remove_selected_area")
		watchHistoryDelChannel.click()

		sleep(10)

		watchHistoryFinishBtn = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.TextView")
		watchHistoryFinishBtn.click()

		sleep(3)

		watchHistoryBackBtn = BackBtn(self)

		sleep(7)

		clickAvatar = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_avatar")
		clickAvatar.click()

		sleep(3)

		shareApp = self.driver.find_element_by_id("tv.tolka.vhometv:id/share_app_title")
		shareApp.click()

		sleep(2)

		phoneBack(self)

		sleep(2)

		goComment = self.driver.find_element_by_id("tv.tolka.vhometv:id/go_comment_title")
		goComment.click()

		sleep(3)

		phoneBack(self)

		sleep(2)

		goFaceBook = self.driver.find_element_by_id("tv.tolka.vhometv:id/go_fb_title")
		goFaceBook.click()

		sleep(3)

		phoneBack(self)

		sleep(2)

		goTwitter = self.driver.find_element_by_id("tv.tolka.vhometv:id/go_twitter_title")
		goTwitter.click()

		sleep(3)

		phoneBack(self)

		sleep(2)

		goInstagram = self.driver.find_element_by_id("tv.tolka.vhometv:id/go_ig_title")
		goInstagram.click()

		sleep(3)

		phoneBack(self)

		sleep(2)
		
		SwipeUp(self,n=4)

		sleep(2)


		#依手機可能會要稍微改動
		#小米不用
		#samsung A7要 A7寫信件頁面back退出會有訊息,步驟需稍微改

		supportBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/support_title")
		supportBtn.click()

		sleep(6)

		phoneBack(self)

		sleep(3)

		phoneBack(self)

		sleep(3)

		samsungMail = self.driver.find_element_by_id("com.samsung.android.email.provider:id/button2")
		samsungMail.click()

		sleep(3)


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

		sleep(6)

		regionBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/region_title")
		regionBtn.click()

		sleep(3)

		regionInOther = self.driver.find_element_by_id("tv.tolka.vhometv:id/option_others")
		regionInOther.click()

		sleep(3)

		regionOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_original")
		regionOkBtn.click()

		sleep(6)


		passwordBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/password_title")
		passwordBtn.click()

		sleep(4)

		passwordEditView = self.driver.find_element_by_id("tv.tolka.vhometv:id/edit_password")
		passwordEditView.click()
		passwordEditView.send_keys("aaa123")

		sleep(4)

		phoneBack(self)

		passwordOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/btn_ok")
		passwordOkBtn.click()

		sleep(8)

		newPasswordEditView = self.driver.find_element_by_id("tv.tolka.vhometv:id/et_input_one")
		newPasswordEditView.click()
		newPasswordEditView.send_keys("aaa123")

		sleep(4)

		TouchAction(self.driver).tap(x=996, y=1824).perform()

		sleep(4)

		againCheckNewPassword = self.driver.find_element_by_id("tv.tolka.vhometv:id/et_input_two")
		againCheckNewPassword.click()
		againCheckNewPassword.send_keys("aaa123")

		sleep(4)

		phoneBack(self)

		sleep(4)

		newPasswordOkBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_original")
		newPasswordOkBtn.click()

		sleep(6)

		backToSettingPage = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_original")
		backToSettingPage.click()

		sleep(4)

		logOutBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/logout_title")
		logOutBtn.click()

		sleep(4)

		logOutCancelBtn = self.driver.find_element_by_id("android:id/button2")
		logOutCancelBtn.click()

		sleep(4)

		logOutBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/logout_title")
		logOutBtn.click()

		sleep(3)

		logOutOkBtn = self.driver.find_element_by_id("android:id/button1")
		logOutOkBtn.click()

		sleep(7)

		clickAvatar = self.driver.find_element_by_id("tv.tolka.vhometv:id/image_avatar")
		clickAvatar.click()

		sleep(6)

		goLoginBtn = GoLoginBtn(self)
		
		sleep(2)

		forgetPasswordBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/forget_pwd")
		forgetPasswordBtn.click()

		sleep(3)

		forgetPasswordEditView = self.driver.find_element_by_id("tv.tolka.vhometv:id/et_input")
		forgetPasswordEditView.click()
		forgetPasswordEditView.send_keys("tvr47819@eoopy.com")

		sleep(6)

		phoneBack(self)

		sleep(3)

		forgetPasswordnextStepBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/tv_original")
		forgetPasswordnextStepBtn.click()

		sleep(40)

		resendMailBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/btn_two")
		resendMailBtn.click()

		sleep(35)

		resendMailBtn = self.driver.find_element_by_id("tv.tolka.vhometv:id/btn_two")
		resendMailBtn.click()

		sleep(5)


def phoneBack(self):
	self.driver.back()

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


def swipLeft(self,n):
    size = self.driver.get_window_size()
    x1 = size['width'] * 0.75
    y1 = size['height'] * 0.6
    x2 = size['width'] * 0.25

    for i in range(n):
        self.driver.swipe(x1, y1, x2, y1)

def swipRight(self,n):
    size = self.driver.get_window_size()
    x1 = size['width'] * 0.25
    y1 = size['height'] * 0.6
    x2 = size['width'] * 0.75

    for i in range(n):
        self.driver.swipe(x1, y1, x2, y1)	

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
    return unittest.TestSuite(map(GAAutoTest, tests))
