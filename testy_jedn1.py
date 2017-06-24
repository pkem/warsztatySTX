#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Logowanie (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_logowanie(self):
        self.driver.get("http://diabcontrol1.herokuapp.com")
        driver = self.driver
        login = driver.find_element_by_name('username')
        login.clear()
        login.send_keys('admin')

        haslo = driver.find_element_by_name('password')
        haslo.clear()
        haslo.send_keys('admin123')
        haslo.send_keys(Keys.RETURN)
        self.assertIn('test', driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
