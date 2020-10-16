import unittest
from more_fun_with_collections import set_membership as set

class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertTrue(set.in_set())

    def test_in_set_false(self):
        self.assertFalse(set.in_set())


if __name__ == '__main__':
    unittest.main()
