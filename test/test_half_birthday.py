import unittest
from more_fun_with_collections import half_birthday as half
from datetime import datetime, timedelta


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.date = datetime.now()
        self.half = self.date + timedelta(days=90)

    def test_half_birthday(self):
        self.assertEqual(half.half_birthday(self.date), self.half)


if __name__ == '__main__':
    unittest.main()
