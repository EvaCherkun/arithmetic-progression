import unittest
from app import arithmetic_sum

class TestArithmeticSum(unittest.TestCase):
    def test_arithmetic_sum_1(self):
        self.assertEqual(arithmetic_sum(5), 25)  # Перевірка для 5 членів прогресії

    def test_arithmetic_sum_2(self):
        self.assertEqual(arithmetic_sum(0), 0)   # Нуль елементів

    def test_arithmetic_sum_3(self):
        self.assertEqual(arithmetic_sum(1), 10)   # Один елемент, сума = 4

    def test_arithmetic_sum_4(self):
        self.assertEqual(arithmetic_sum(3), 21)  # 4 + 7 + 10 = 21

    def test_arithmetic_sum_negative(self):
        self.assertEqual(arithmetic_sum(-3), 0)  # Перевірка для від'ємного числа, очікується 0


