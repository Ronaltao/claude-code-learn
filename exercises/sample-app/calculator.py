"""
一个简单的命令行计算器小程序 —— 供 Claude Code 学习练习用。

⚠️ 注意：这个文件里【故意】留了几个 bug，用来给学员练习
"让 Claude Code 找 bug、修 bug"。请不要直接看下面的提示去手动改，
先去 exercises/README.md 看练习说明，用 Claude Code 来完成。

运行方式：
    python calculator.py        # 进入交互模式
"""


class Calculator:
    """一个支持基本运算和历史记录的计算器。"""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        """加法。"""
        result = a + b
        self._record("add", a, b, result)
        return result

    def subtract(self, a, b):
        """减法。"""
        result = a - b
        self._record("subtract", a, b, result)
        return result
    # 
    def multiply(self, a, b):
        """乘法。"""
        # BUG #1: 这里写成了加法，不是乘法
        result = a + b
        self._record("multiply", a, b, result)
        return result

    def divide(self, a, b):
        """除法。"""
        # BUG #2: 没有处理除数为 0 的情况，b=0 时会抛出未捕获的 ZeroDivisionError
        result = a / b
        self._record("divide", a, b, result)
        return result

    def average(self, numbers):
        """求一组数字的平均值。"""
        # BUG #3: 用 len(numbers) - 1 作分母是错的，应该是 len(numbers)
        total = sum(numbers)
        return total / (len(numbers) - 1)

    def _record(self, op, a, b, result):
        self.history.append(f"{a} {op} {b} = {result}")

    def show_history(self):
        """打印历史记录。"""
        if not self.history:
            print("（暂无历史记录）")
        for line in self.history:
            print(line)


def main():
    calc = Calculator()
    print("简单计算器（输入 q 退出）")
    print("用法示例：add 3 5")
    while True:
        raw = input("> ").strip()
        if raw in ("q", "quit", "exit"):
            break
        if raw == "history":
            calc.show_history()
            continue
        parts = raw.split()
        if len(parts) != 3:
            print("格式错误，请输入：<运算> <数字> <数字>，例如 add 3 5")
            continue
        op, x, y = parts
        x, y = float(x), float(y)
        if op == "add":
            print(calc.add(x, y))
        elif op == "subtract":
            print(calc.subtract(x, y))
        elif op == "multiply":
            print(calc.multiply(x, y))
        elif op == "divide":
            print(calc.divide(x, y))
        else:
            print(f"不支持的运算：{op}")


if __name__ == "__main__":
    main()
