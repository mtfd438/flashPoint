from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class SignUp(BasePage):

    def set_userID(self, id):
        userIdElement =  self.driver.find_element_by_xpath('//input[@placeholder="Choose a Docker Hub ID"]')
        userIdElement.send_keys(id)

    def set_email(self, email):
        emailElement = self.driver.find_element_by_xpath('//input[@placeholder="Enter your email address"]')
        emailElement.send_keys(email)

    def set_password(self, password):
        pwordElement = self.driver.find_element_by_xpath('//input[@placeholder="Choose a password"]')
        pwordElement.send_keys(password)        
        
    def click_signupButton(self):
        submitBttn = self.driver.find_element_by_xpath('//button[text()="Sign Up"]')
        submitBttn.click()
        time.sleep(5) # delays for 3 seconds
    
    def signUp_success_displayed(self):
        notifcationElement = self.driver.find_element_by_xpath('//div[text()="Sweet! You\'re almost ready to go!"]')
        return notifcationElement.is_displayed()

    def signup(self, id, email, password):
        self.set_userID(id) 
        self.set_email(email)
        self.set_password(id) 
        self.click_signupButton()
        
        
        

