#Manejo de alerts y pop ups

import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'/home/neryr/chromedriver/stable/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element(by=By.NAME, value = 'q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element(by=By.CLASS_NAME, value = 'link-compare').click()
        driver.find_element(by=By.XPATH, value = '//*[@id="top"]/body/div/div[2]/div[2]/div/div[3]/div/div[2]/div/a').click()

        alert = driver.switch_to.alert
        alert_text = alert.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='select_language'))