import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

#Esta línea sirve para preparar el entorno de prueba
    #Classmethod sirve para ejecutar las pruebas en una misma ventana del navegador, sin esto se ejecuta una ventana diferente por prueba
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'/home/neryr/chromedriver/stable/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

#Entorno de prueba y acciones a realizar en este entorno
    def test_hello_world(cls):
        driver = cls.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(cls):
        cls.driver.get('https://www.wikipedia.org')

#Acciones finales a realizar, en este caso sería cerrar las ventanas al finalizar
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))