#!/usr/bin/python

import unittest
import sys
from pages import signUpPage
from selenium import webdriver
import ConfigParser
import string

config = ConfigParser.ConfigParser()
config.read("conf.ini")
url = config.get("url","url") 
id = config.get("fake credentials","id") 
pw = config.get("fake credentials","pw") 
email = config.get("fake credentials","email") 

class SignUp(unittest.TestCase):
  def setUp(self):
     self.driver = webdriver.Chrome() #chromedriver located in /usr/local/bin
     self.driver.get(url)

#verify a new user can successfully signup for new account
  def test_SignUp_Passed(self):
      signup = signUpPage.SignUp(self.driver)
      signup.signup(id, email, pw)
      assert signup.signUp_success_displayed()


  def tearDown(self):
      self.driver.close()

if __name__ == '__main__': unittest.main()
