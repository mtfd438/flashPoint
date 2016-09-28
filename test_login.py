#!/usr/bin/python

import unittest
import sys
from pages import loginPage
from selenium import webdriver
 

class Login(unittest.TestCase):
  def setUp(self):
     self.driver = webdriver.Chrome() #chromedriver located in /usr/local/bin
     self.driver.get("https://hub.docker.com/login/")

#verify user can successfully login
  def test_Login_Passed(self):
      loginpage = loginPage.LoginPage(self.driver)
      loginpage.login('mmittiga17','Elsa4564')  
      assert loginpage.login_success_displayed()

#verify user cannot login with bad credentials and login error alert is displayed 
  def test_Login_Failed(self):
      loginpage = loginPage.LoginPage(self.driver)
      loginpage.login('aldjfldj','aldjf')
      assert loginpage.login_error_displayed()

  def tearDown(self):
      self.driver.close()

if __name__ == '__main__': unittest.main()
