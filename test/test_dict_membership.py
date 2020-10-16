import unittest
from more_fun_with_collections import dict_membership as dict

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_dict = {'A': 10, 'B': 15, 'C': 30, 'M': 95, 'K': 39}

    def test_in_dict_true(self):
        self.assertTrue(dict.in_dict(self.test_dict, 'A'))

    def test_in_dict_false(self):
        self.assertFalse(dict.in_dict(self.test_dict, 'L'))


if __name__ == '__main__':
    unittest.main()
