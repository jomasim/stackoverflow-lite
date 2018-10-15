import unittest
from app.calc import add ,multiply


class test_class(unittest.TestCase):
    def test_add(self):
       res = add(10, 7)
       return self.assertEqual(res,17)
