"""
calculator.py 的单元测试。

这些测试描述了【正确】的预期行为。因为 calculator.py 里故意留了 bug，
所以现在运行这些测试会有几个【失败】—— 这正是练习的起点。

运行方式（在 sample-app 目录下）：
    python -m unittest test_calculator.py -v
"""

import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        # 这个测试会失败，因为 multiply 里有 BUG #1
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        # 预期：除以 0 时应抛出 ValueError 并给出友好提示（而不是 ZeroDivisionError）
        # 这个测试会失败，因为 divide 有 BUG #2（没处理除零）
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_average(self):
        # 这个测试会失败，因为 average 有 BUG #3（分母用错）
        self.assertEqual(self.calc.average([2, 4, 6]), 4)

    def test_history_records(self):
        self.calc.add(1, 2)
        self.calc.subtract(5, 1)
        self.assertEqual(len(self.calc.history), 2)


if __name__ == "__main__":
    unittest.main()
