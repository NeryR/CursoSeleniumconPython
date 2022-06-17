#Automatización de navegación

import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'/home/neryr/chromedriver/stable/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com/')

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element(by=By.NAME, value = 'q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='select_language'))