#Data Driven Testing

from itertools import product
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'/home/neryr/chromedriver/stable/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    @data(('dress', 5), ('music', 5))
    @unpack    

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element(by = By.NAME, value = 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements(by = By.XPATH, value = '//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')
        
        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='search_ddt'))