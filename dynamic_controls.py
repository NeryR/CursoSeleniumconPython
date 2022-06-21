#Controles dinámicos, en este ejercicio se tendrán que habilitar controles que se encuentran deshabilitados o viceversa

from cgitb import enable
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'/home/neryr/chromedriver/stable/chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(by = By.LINK_TEXT, value = 'Dynamic Controls').click()

    def test_name_elements(self):
        driver = self.driver

        checkbox = driver.find_element(by = By.CSS_SELECTOR, value = '#checkbox > input[type=checkbox]')
        checkbox.click

        remove_add_button = driver.find_element(by = By.CSS_SELECTOR, value = '#checkbox-example > button')
        remove_add_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')))
        remove_add_button.click()

        enable_disable_button = driver.find_element(by = By.CSS_SELECTOR, value = '#input-example > button')
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))

        text_area = driver.find_element(by = By.CSS_SELECTOR, value = '#input-example > input[type=text]')
        text_area.send_keys('Platzi')

        enable_disable_button.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='dynamic_controls'))