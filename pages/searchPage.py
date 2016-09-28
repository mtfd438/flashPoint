from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class SearchPage(BasePage):

    def set_SearchText(self, searchText):
        SearchTextBox =  self.driver.find_element_by_xpath('//input[@placeholder="Search"]')
        SearchTextBox.send_keys(searchText)
        SearchTextBox.submit()

    def searchResults(self):
        repoStr = self.driver.find_element_by_xpath('//h3[contains(text(),"Repositories")]').text
        result = int(filter(unicode.isdigit, repoStr))
        return result
 
    def search(self, searchText):
        self.set_SearchText(searchText)
        time.sleep(3)
        self.searchResults()
        
        
        

