import unittest
from more_fun_with_collections import set_membership as set

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_set = {1, 5, 6, 3, 7, 9}
    def test_in_set_true(self):
        self.assertTrue(set.in_set(self.test_set, 5))

    def test_in_set_false(self):
        self.assertFalse(set.in_set(self.test_set, 4))


if __name__ == '__main__':
    unittest.main()
