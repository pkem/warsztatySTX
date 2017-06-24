#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Logowanie (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        self.driver.get("http://diabcontrol1.herokuapp.com")
        self.login('admin', 'admin123')
        dirver.implicitly_wait(5)
        self.assertIn('Welcome to DiabControl system', driver.page_source)

        nawigacja=find_elements_by_clas("nav nav-sidebar")
        nawigacja.find_element_by_tag("a")
        a=nawigacja.find_element_by_tag("a")

        print [e.text for e in a]
    def test_patients(self):
        driver = self.browser
        driver.get("http://diabcontrol1.herokuapp.com")
        self.login('doctor_a@example.com', 'admin123')
        self.driver.find_element_by_link_text("My patients").click()

    def login(self, username, password):
        driver = self.driver
        login = driver.find_element_by_name('username')
        login.clear()
        login.send_keys(username)

        haslo = driver.find_element_by_name('password')
        haslo.clear()
        haslo.send_keys(password)
        haslo.send_keys(Keys.RETURN)


#    def tearDown(self):
#        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
