import unittest
from more_fun_with_collections import dict_membership as dict

class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertTrue(dict.in_dict())

    def test_in_dict_false(self):
        self.assertFalse(dict.in_dict())


if __name__ == '__main__':
    unittest.main()
