# Claude Code 新手入门实战课

> 一个从零开始、边学边练的 Claude Code 学习项目。
> 目标：让完全没接触过的新手，在 1～2 小时内能独立、自信地用 Claude Code 完成日常开发任务。

Claude Code 是 Anthropic 官方的命令行 AI 编程助手 —— 你用自然语言描述需求，它能读代码、改代码、跑命令、查资料、提交 Git，像一位坐在你旁边结对编程的工程师。

本项目不是"功能文档堆砌"，而是一条**学习路线**：每一节都先讲"是什么、为什么、怎么用"，再给一个 30 秒就能上手的小练习。

---

## 🗺️ 学习路线图

建议**按顺序**学习。每节文档末尾都有"动手试一试"，请务必真的去 Claude Code 里敲一遍 —— 看十遍不如自己敲一遍。

### 第一阶段 · 入门（必学）

| # | 章节 | 你将学会 |
|---|------|----------|
| 01 | [什么是 Claude Code](docs/01-what-is-claude-code.md) | 它能做什么、不能做什么、和 ChatGPT 的区别 |
| 02 | [安装与启动](docs/02-install-and-start.md) | 装好、登录、第一次跑起来 |
| 03 | [基础交互](docs/03-basics.md) | 怎么提问、怎么打断、怎么看它在干什么 |
| 04 | [让它读写文件](docs/04-files.md) | 读代码、改代码、新建文件的正确姿势 |
| 05 | [斜杠命令](docs/05-slash-commands.md) | `/help` `/clear` `/init` 等高频命令 |

### 第二阶段 · 进阶（推荐）

| # | 章节 | 你将学会 |
|---|------|----------|
| 06 | [权限与安全](docs/06-permissions.md) | 它会不会乱删我的文件？怎么控制权限 |
| 07 | [计划模式](docs/07-plan-mode.md) | 让它"先想后做"，避免改错方向 |
| 08 | [CLAUDE.md 项目记忆](docs/08-claude-md.md) | 让它记住你的项目规范，少走弯路 |
| 09 | [Git 与版本控制](docs/09-git.md) | 让它帮你写 commit、开分支、提 PR |

### 第三阶段 · 高手（按需）

| # | 章节 | 你将学会 |
|---|------|----------|
| 10 | [Skills 技能](docs/10-skills.md) | 把重复流程封装成可复用的能力 |
| 11 | [Subagents 子代理](docs/11-subagents.md) | 派出"分身"并行干活、隔离上下文 |
| 12 | [MCP 扩展](docs/12-mcp.md) | 连接数据库、浏览器、第三方工具 |
| 13 | [Hooks 钩子](docs/13-hooks.md) | 自动化："每次改完代码自动跑测试" |
| 14 | [配置 settings.json](docs/14-settings.md) | 持久化你的偏好与权限规则 |

---

## ✋ 动手练习区

光看不练假把式。学完前几节后，去 [exercises/](exercises/) 完成几个真实小任务：

- [练习说明与闯关清单](exercises/README.md)
- 自带一个**故意留了 bug 的小程序** [`sample-app/`](exercises/sample-app/)，让你练习"让 Claude Code 找 bug、修 bug、补测试"。

## 📋 速查表

记不住命令？[CHEATSHEET.md](CHEATSHEET.md) 一页纸把高频命令、快捷键、技巧全列出来，建议打印或置顶。

---

## 🚀 30 秒快速体验

如果你已经装好了 Claude Code（没装看 [第 02 节](docs/02-install-and-start.md)），现在就可以试：

```bash
cd f:/claude_code_project/project1   # 进入本项目目录
claude                                # 启动 Claude Code
```

然后输入：

```
读一下 exercises/sample-app/calculator.py，告诉我这个程序是做什么的
```

恭喜，你已经用 Claude Code 完成了第一次"代码阅读"。接下来从 [第 01 节](docs/01-what-is-claude-code.md) 正式开始吧。

---

## 学习建议

- **真的去敲**：每节的"动手试一试"不要跳过。
- **大胆问它**：不懂的概念，直接在 Claude Code 里问"什么是 XX"，它会用你项目的上下文回答。
- **不怕改错**：本项目纯学习用途，文件改坏了重新拉一份即可；正式项目记得用 Git。
- **循序渐进**：第三阶段（Skills/MCP/Hooks）是高级功能，入门阶段可以先跳过。

> 💡 本项目本身就是用 Claude Code 友好的方式组织的：根目录有 [CLAUDE.md](CLAUDE.md) 作为"项目记忆"的示范，你可以打开看看一个真实的 CLAUDE.md 长什么样。
