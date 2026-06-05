"""
calculator.py 的单元测试。

这些测试描述了【正确】的预期行为。因为 calculator.py 里故意留了 bug，
所以现在运行这些测试会有几个【失败】—— 这正是练习的起点。

运行方式（在 sample-app 目录下）：
    python -m unittest test_calculator.py -v
"""

import os
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


class TestHistoryPersistence(unittest.TestCase):
    """验证历史记录持久化到文件、并能跨实例读回。"""

    def setUp(self):
        # 用固定名的临时文件（本环境禁用随机数），每次测试前先清掉残留
        self.tmp = "test_history_tmp.txt"
        if os.path.exists(self.tmp):
            os.remove(self.tmp)

    def tearDown(self):
        if os.path.exists(self.tmp):
            os.remove(self.tmp)

    def test_history_persisted_across_instances(self):
        # 第一个实例做几次运算，历史应自动写入文件
        calc1 = Calculator(history_file=self.tmp)
        calc1.add(1, 2)
        calc1.subtract(9, 4)
        self.assertTrue(os.path.exists(self.tmp))

        # 新建第二个实例绑定同一文件，应把历史读回来
        calc2 = Calculator(history_file=self.tmp)
        self.assertEqual(calc2.history, calc1.history)
        self.assertEqual(len(calc2.history), 2)

    def test_clear_history_clears_file(self):
        calc = Calculator(history_file=self.tmp)
        calc.add(1, 1)
        calc.clear_history()
        self.assertEqual(calc.history, [])

        # 重新读取文件，确认文件内容也被清空
        reloaded = Calculator(history_file=self.tmp)
        self.assertEqual(reloaded.history, [])

    def test_memory_only_mode_writes_no_file(self):
        # 不绑定文件时，行为与纯内存版一致，且不应产生文件
        calc = Calculator()
        calc.add(2, 3)
        self.assertEqual(len(calc.history), 1)
        self.assertFalse(os.path.exists(self.tmp))


if __name__ == "__main__":
    unittest.main()
