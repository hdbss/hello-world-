import unittest
import time
from selenium.webdriver.common.by import By
from fool import A
from ddt import ddt, data, unpack
from selenium import webdriver


@ddt
class BaiDu(unittest.TestCase):
    input1 = (By.ID, 'kw')
    in_click = (By.ID, 'su')

    def send_key1(self, value1):
        q1 = A()
        q1.send_key123(self.input1, value1)
        time.sleep(3)
        q1.click(self.in_click)
    @classmethod
    def setUpClass(cls):
        cls.driver = A()
        # cls.driver.get('http://www.baidu.com')

    @data(1, 2)
    def test1(self, value):
        self.driver.send_key123(self.input1, value)
        # self.driver.find_element(By.ID, 'kw').send_keys(value)
        time.sleep(3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
