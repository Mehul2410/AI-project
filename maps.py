from selenium import webdriver
import time

class maps():
    def __init__(self):
        #D:\User\Work\final year\AI-project
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    def get_info(self,query):
        self.driver.get(url="https://www.google.com/maps")
        loc=self.driver.find_element_by_xpath('//*[@id="searchboxinput"]')
        loc.click()
        loc.send_keys(query)
        search=self.driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
        search.click()

