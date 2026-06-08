"""
一个简单的命令行计算器小程序 —— 供 Claude Code 学习练习用。

运行方式：
    python calculator.py        # 进入交互模式
"""

import os

# 默认的历史记录文件名（相对当前工作目录）
DEFAULT_HISTORY_FILE = "calc_history.txt"


class Calculator:
    """一个支持基本运算和历史记录的计算器。

    可选地绑定一个历史文件 history_file：一旦绑定，会在创建时自动读回
    已有历史，并在每次运算后自动把历史写入文件，从而实现跨次运行的持久化。
    不传 history_file 时行为与纯内存版完全一致。
    """

    def __init__(self, history_file=None):
        self.history = []
        self.history_file = history_file
        if history_file:
            self._load()  # 启动时把已有历史读回来

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
        result = a * b
        self._record("multiply", a, b, result)
        return result

    def divide(self, a, b):
        """除法。"""
        if b == 0:
            raise ValueError("除数不能为 0")
        result = a / b
        self._record("divide", a, b, result)
        return result

    def average(self, numbers):
        """求一组数字的平均值。"""
        total = sum(numbers)
        return total / len(numbers)

    def _record(self, op, a, b, result):
        self.history.append(f"{a} {op} {b} = {result}")
        self._save()  # 每次运算后持久化到文件（若绑定了文件）

    def clear_history(self):
        """清空历史记录，并同步清空文件。"""
        self.history = []
        self._save()

    def _load(self):
        """从历史文件读回记录；文件不存在则静默跳过。"""
        if not self.history_file or not os.path.exists(self.history_file):
            return
        with open(self.history_file, "r", encoding="utf-8") as f:
            self.history = [line.rstrip("\n") for line in f if line.strip()]

    def _save(self):
        """把当前历史整体写回文件（未绑定文件则什么都不做）。"""
        if not self.history_file:
            return
        with open(self.history_file, "w", encoding="utf-8") as f:
            for line in self.history:
                f.write(line + "\n")

    def show_history(self):
        """打印历史记录。"""
        if not self.history:
            print("（暂无历史记录）")
        for line in self.history:
            print(line)


def main():
    calc = Calculator(history_file=DEFAULT_HISTORY_FILE)
    print("简单计算器（输入 q 退出）")
    print("用法示例：add 3 5")
    print(f"历史会自动保存到 {DEFAULT_HISTORY_FILE}；输入 history 查看、clear 清空")
    while True:
        raw = input("> ").strip()
        if raw in ("q", "quit", "exit"):
            break
        if raw == "history":
            calc.show_history()
            continue
        if raw == "clear":
            calc.clear_history()
            print("（历史已清空）")
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
