#!/usr/bin/python

import unittest
import sys
from pages import searchPage
from selenium import webdriver
import ConfigParser
import string

config = ConfigParser.ConfigParser()
config.read("conf.ini")
url = config.get("url","url") 

class Search(unittest.TestCase):
  def setUp(self):
     self.driver = webdriver.Chrome() #chromedriver located in /usr/local/bin
     self.driver.get(url)

#verify a site search will return results
  def test_Search(self):
      searchpage = searchPage.SearchPage(self.driver)
      searchpage.search('hockey')  
      results = searchpage.searchResults()
      self.assertGreater(results, 0)

#verify a site search will return 0 results results if search querey is not found
  def test_Search_NotFound(self):
      searchpage = searchPage.SearchPage(self.driver)
      searchpage.search('123xxx456yyy')  
      results = searchpage.searchResults()
      self.assertEquals(results, 0)

  def tearDown(self):
      self.driver.close()

if __name__ == '__main__': unittest.main()
