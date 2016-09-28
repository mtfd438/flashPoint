from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def set_userID(self, id):
        userIdElement =  self.driver.find_element_by_xpath('//input[@placeholder="Username"]')
        userIdElement.send_keys(id)

    def set_password(self, password):
        pwordElement = self.driver.find_element_by_xpath('//input[@placeholder="Password"]')
        pwordElement.send_keys(password)        
        
    def click_submitButton(self):
        submitBttn = self.driver.find_element_by_xpath('//button[text()="Log In"]')
        submitBttn.click()
        time.sleep(5) # delays for 3 seconds
    
    def login_error_displayed(self):
        notifcationElement = self.driver.find_element_by_xpath('//p[text()="Login Failed. The username or password may be incorrect."]')
        return notifcationElement.is_displayed()

    def login_success_displayed(self):
        notifcationElement = self.driver.find_element_by_xpath('//H1[text()="Welcome to Docker Hub"]')
        return notifcationElement.is_displayed()

    def login(self, id, password):
        self.set_password(password)
        self.set_userID(id) 
        self.click_submitButton()
        
        
        

