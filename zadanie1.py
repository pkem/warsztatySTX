#!/usr/bin/python
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get("http:duckduckgo.com/")


elem = browser.find_element_by_name("q")
elem.clear()
elem.send_keys("the biggest python software house")
elem.send_keys(Keys.RETURN)

browser.implicitly_wait(5)
#odnosnik=browser.find_element_by_class_name("result__a")
odnosnik=browser.find_elements_by_class_name("result__a")
print odnosnik[1]
l=odnosnik[1]
l.click()
browser.quit()
