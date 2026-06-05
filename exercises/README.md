# 动手练习 · 闯关清单

> 看十遍不如做一遍。下面是 6 个由易到难的关卡，每一关都对应教程里的某个功能。
> **请真的在 Claude Code 里完成它们**，做完打个勾 ✅。

## 准备工作

1. 确保已经装好 Claude Code（[第 02 节](../docs/02-install-and-start.md)）。
2. 在本项目目录启动：
   ```bash
   cd f:/claude_code_project/project1
   claude
   ```
3. （推荐）把本项目变成 Git 仓库，这样你能随时看改动、随时还原：
   ```bash
   git init && git add -A && git commit -m "起始状态"
   ```

> 🐍 练习用到的小程序在 [`sample-app/`](sample-app/)，是一个**故意留了 3 个 bug** 的 Python 计算器。只用到 Python 标准库，无需安装任何依赖。

---

## 🟢 关卡 1 · 读懂一个陌生程序
**练的是**：[基础交互](../docs/03-basics.md)、[读写文件](../docs/04-files.md)

在 Claude Code 里输入：
```
读一下 exercises/sample-app/calculator.py，告诉我：
1) 这个程序是做什么的 2) 它有哪几个方法 3) 怎么运行它
```

✅ 通关标准：它能准确说出计算器的功能和各个方法，并告诉你 `python calculator.py` 怎么跑。

---

## 🟢 关卡 2 · 跑测试，发现 bug
**练的是**：[让它读改验证闭环](../docs/04-files.md)

```
进入 exercises/sample-app 目录，运行单元测试 test_calculator.py，
告诉我有几个测试失败、分别是什么原因。先不要改任何代码。
```

✅ 通关标准：它运行测试，报告有 **3 个失败**（multiply、divide_by_zero、average），并能解释每个失败的原因。

> 💡 注意它运行命令前会**请求你批准**——这就是 [第 06 节权限系统](../docs/06-permissions.md) 在起作用。

---

## 🟡 关卡 3 · 用计划模式修 bug
**练的是**：[计划模式](../docs/07-plan-mode.md)、[修改文件](../docs/04-files.md)

1. 按 `Shift + Tab` 切到**计划模式**。
2. 输入：
   ```
   calculator.py 里有几个 bug 导致测试失败。先给我一份修复方案，
   说明每个 bug 在哪、怎么改，先不要动代码。
   ```
3. 看完方案觉得 OK，批准它执行。
4. 让它收尾：
   ```
   按方案修复，然后重新跑测试确认全部通过
   ```

✅ 通关标准：所有 7 个测试通过。期间你体验了"先看方案 → 再动手 → 自动验证"的完整流程。

---

## 🟡 关卡 4 · 加一个新功能
**练的是**：[计划模式](../docs/07-plan-mode.md) + [写测试](../docs/04-files.md)

```
给 Calculator 类增加一个 power(a, b) 方法用于求幂（a 的 b 次方），
要求：1) 同样记录到 history 2) 在 test_calculator.py 里补一个对应测试
3) 跑测试确认通过
```

✅ 通关标准：新方法可用、有测试、测试通过。

---

## 🟡 关卡 5 · 写项目记忆 CLAUDE.md
**练的是**：[CLAUDE.md 项目记忆](../docs/08-claude-md.md)

给 sample-app 单独建一份记忆：
```
在 exercises/sample-app/ 目录下创建一个 CLAUDE.md，说明这个小程序的功能、
怎么运行、怎么跑测试，并注明"代码注释用中文"。
```

然后**退出再重进** Claude Code，验证它记住了：
```
根据项目记忆，sample-app 这个程序怎么跑测试？
```

✅ 通关标准：重启后它能从 CLAUDE.md 复述出运行/测试方式。

---

## 🔴 关卡 6 · 完整的 Git 工作流
**练的是**：[Git 与版本控制](../docs/09-git.md)、[斜杠命令](../docs/05-slash-commands.md)

把你前面几关的改动好好提交：
```
看一下当前所有改动，帮我分成几个有意义的提交（修 bug 一个、加 power 功能一个、
加文档一个），每个 commit message 用中文写清楚
```

进阶：
```
/review
```
让它审查一遍你的改动。

✅ 通关标准：`git log` 里能看到几条清晰的中文提交记录。

---

## 🎓 毕业挑战（自由发挥）

不再给你具体指令，自己用学到的技能完成：

- 让 Claude Code 给 calculator 增加一个**交互模式下的 `power` 命令**（目前 main() 里没接上）。
- 让它把 calculator 的运算历史**保存到文件**，下次启动能读回来。
- 给整个 sample-app 写一份漂亮的 `README.md`。

> 完成这些，你就已经能独立用 Claude Code 做真实开发了。👏

---

## 学完之后

- 把 [CHEATSHEET](../CHEATSHEET.md) 收藏好，随时查命令。
- **最重要的一步**：打开你自己手头真实的项目，`cd` 进去，`claude` 启动，开始用它干活。教程的终点，是日常的起点。
