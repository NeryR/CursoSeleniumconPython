#Manejar form, textbox, checkbox y radio button

import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/neryr/chromedriver/stable/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_new_user(self):
        driver = self.driver
        driver.find_element(by=By.XPATH, value = "/html/body/div/div[2]/header/div/div[2]/div/a/span[2]").click()
        driver.find_element(by=By.XPATH, value = '/html/body/div/div[2]/header/div/div[5]/div/ul/li[6]/a').click()

        create_account_button = driver.find_element(by=By.XPATH, value = '//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element(by=By.ID, value = 'firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_adress = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element(by=By.XPATH, value = '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled() and middle_name.is_enabled() and last_name.is_enabled() and email_adress.is_enabled() and news_letter_subscription.is_enabled() and password.is_enabled() and confirm_password.is_enabled() and confirm_password.is_enabled() and submit_button.is_enabled())

        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_adress.send_keys('Test@gmail.com')
        news_letter_subscription.click()
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='register-new-user'))