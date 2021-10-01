from selenium import webdriver

class infow():
    def __init__(self):
        #D:\User\Work\final year\AI-project
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    def get_info(self,query):
        self.query= query
        self.driver.get(url="https://www.wikipedia.org")
        search= self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()
    
