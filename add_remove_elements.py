#Agregar y eliminar elementos

import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'/home/neryr/chromedriver/stable/chromedriver')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(by = By.LINK_TEXT, value = 'Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element(by = By.XPATH, value = '//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element(by = By.XPATH, value = '//*[@id="elements"]/button')
                delete_button.click()
            except:
                print("You're trying to delete more elements the existent")
                break

        if total_elements > 0:
            print("There are " + str(total_elements) + " elements on screen")
        else:
            print("There are 0 elements on screen")

        sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='add_remove_elements'))