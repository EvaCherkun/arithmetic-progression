import unittest
from main import arithmetic_sum

class TestArithmeticSum(unittest.TestCase):
    def test_zero_members(self):
        self.assertEqual(arithmetic_sum(0), 0)

    def test_one_member(self):
        self.assertEqual(arithmetic_sum(1), 4)

    def test_multiple_members(self):
        self.assertEqual(arithmetic_sum(5), 55)  # 4 + 7 + 10 + 13 + 16 = 55

    def test_negative_input(self):
        self.assertEqual(arithmetic_sum(-5), 0)

if __name__ == "__main__":
    unittest.main()
