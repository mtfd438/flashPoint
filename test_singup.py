#!/usr/bin/python

import unittest
import sys
from pages import signUpPage
from selenium import webdriver
 

class Login(unittest.TestCase):
  def setUp(self):
     self.driver = webdriver.Chrome() #chromedriver located in /usr/local/bin
     self.driver.get("https://hub.docker.com/")

#verify user can successfully login
  def test_SignUp_Passed(self):
      signup = signUpPage.SignUp(self.driver)
      signup.signup('IDxxxx','blahblahblah@blahblah.com','X*1xxxxxxxxxx')  
      assert signup.signUp_success_displayed()


  def tearDown(self):
      self.driver.close()

if __name__ == '__main__': unittest.main()
