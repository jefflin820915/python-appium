import unittest
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys 
from time import sleep
class Chrome(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com.tw/')
        self.assertIn('Google', self.browser.title)

    def input_test(self):

        el1 = self.browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]")
        el1.send_keys('1234567')

        sleep(1)

        el2 = self.browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center[1]/input[1]")
        el2.click()

        sleep(1)

    def tearDown(self):
        self.browser.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)