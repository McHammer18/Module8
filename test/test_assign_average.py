import unittest
from more_fun_with_collections import assign_average as assign

class MyTestCase(unittest.TestCase):
        def test_A(self):
            self.assertEqual("You Entered an A!", assign.switch_average('A'))

        def test_B(self):
            self.assertEqual("You Entered an B!", assign.switch_average('B'))

        def test_C(self):
            self.assertEqual("You Entered an C!", assign.switch_average('C'))

        def test_D(self):
            self.assertEqual("You Entered an D!", assign.switch_average('D'))

        def test_F(self):
            self.assertEqual("You Entered an F!", assign.switch_average('F'))

        def test_non_key(self):
            self.assertEqual("This is not a valid Grade!", assign.switch_average('R'))

if __name__ == '__main__':
    unittest.main()
