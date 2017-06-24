import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        browser = self.browser
        browser.get("http://diabcontrol1.herokuapp.com")
        user_field = browser.find_element_by_name('username')
        user_field.clear()
        user_field.send_keys('doctor_a@example.com')

        password_field = browser.find_element_by_name('password')
        password_field.clear()
        password_field.send_keys('admin123')
        password_field.send_keys(Keys.RETURN)

    def tearDown(self):
        self.browser.quit()

    def test_text(self):
       sleep(1)
       assert 'Welcome to DiabControl system' in self.browser.page_source

    def test_patient(self):
        sleep(1)
        div = self.browser.find_element_by_class_name('col-sm-3')
        div.find_element_by_link_text('My patients').click()
        sleep(1)
        headers = self.browser.find_elements_by_tag_name('th')
        headers_text = [header.text for header in headers]
        self.assertIn('First Name', headers_text)
        expected_headers = [u'Email', u'First Name', u'Last Name']
        self.assertListEqual(expected_headers, headers_text)


if __name__ == "__main__":
    unittest.main()
