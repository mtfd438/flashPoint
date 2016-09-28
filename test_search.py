#!/usr/bin/python

import unittest
import sys
from pages import searchPage
from selenium import webdriver
 

class Search(unittest.TestCase):
  def setUp(self):
     self.driver = webdriver.Chrome() #chromedriver located in /usr/local/bin
     self.driver.get("https://hub.docker.com/")

#verify a site search will return results
  def test_Search(self):
      searchpage = searchPage.SearchPage(self.driver)
      searchpage.search('hockey')  
      results = searchpage.searchResults()
      self.assertGreater(results, 0)

  def tearDown(self):
      self.driver.close()

if __name__ == '__main__': unittest.main()
