import unittest
from ddt import ddt, unpack, file_data, data

import yaml
with open('3.yaml', 'r')as f:
    d1 = yaml.load(f, Loader=yaml.FullLoader)


@ddt
class A(unittest.TestCase):
    @file_data(r'3.yaml')
    def test_1(self, **value):
        print(value)


if __name__ == '__main__':
    unittest.main()
