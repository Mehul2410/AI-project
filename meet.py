from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from ss import *

class meet():
    def __init__(self):
        #D:\User\Work\final year\AI-project
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    def get_info(self):
        self.driver.get(url="https://meet.new/")
        opt=Options()
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
        })
        username=self.driver.find_element_by_id('identifierId')
        username.click()
        username.send_keys(email)

        next=self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
        next.click()
        time.sleep(2)
        password=self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password.click()
        password.send_keys('m1e2h3u4l5')
        next=self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
        next.click()

        time.sleep(5)
        # dismiss=self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
        # dismiss.click()
