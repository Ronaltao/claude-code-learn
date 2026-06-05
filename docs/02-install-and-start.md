# 02 · 安装与启动

> 本节目标：把 Claude Code 装好、登录、第一次成功跑起来。

## 是什么

Claude Code 有多种使用形态，新手最常用两种：

1. **命令行（CLI）** —— 在终端里运行 `claude`，本教程主要用这种。
2. **IDE 插件** —— VS Code、JetBrains 里直接用（你现在可能就在 VS Code 插件里看到我）。

此外还有桌面 App 和网页版（claude.ai/code）。功能相通，先掌握 CLI 最通用。

## 怎么用

### 第 1 步：安装

推荐用官方安装脚本（最省心）：

**macOS / Linux：**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows（PowerShell）：**
```powershell
irm https://claude.ai/install.ps1 | iex
```

> 💡 你也可以用 npm 安装：`npm install -g @anthropic-ai/claude-code`（需要 Node.js 18+）。
> 如果安装命令将来有变化，以官方文档为准：https://docs.claude.com/claude-code

### 第 2 步：验证安装

新开一个终端，输入：

```bash
claude --version
```

能打印出版本号就说明装好了。如果提示"命令找不到"，重启一下终端，或检查安装日志里提示的 PATH 设置。

### 第 3 步：进入你的项目目录

Claude Code 是**以"当前目录"为工作区**的。所以先 `cd` 到你要工作的项目里。我们就用本学习项目：

```bash
cd f:/claude_code_project/project1
```

### 第 4 步：启动并登录

```bash
claude
```

**第一次启动**会引导你：

1. 选择主题（深色/浅色，随便选，以后能用 `/config` 改）。
2. **登录** —— 会打开浏览器，用你的 Claude 账号（订阅）或 Anthropic API 账号授权。按提示点同意即可。
3. 回到终端，看到输入框就成功了。

> 🔑 登录方式二选一：
> - **Claude 订阅账号**（Pro/Max 等）—— 用量包含在订阅里，适合个人。
> - **Anthropic API Key** —— 按用量付费，适合需要 API 计费的场景。

### 第 5 步：第一次对话

在输入框里打字，回车发送：

```
你好，介绍一下当前这个目录是什么项目
```

它会自己去读目录、读 `README.md` 和 `CLAUDE.md`，然后告诉你。🎉 你已经成功跑起来了！

## 常见问题

| 问题 | 解决 |
|------|------|
| `claude: command not found` | 重启终端；或检查安装脚本提示的 PATH 是否生效 |
| 浏览器没弹出登录 | 终端里会有一个链接，手动复制到浏览器打开 |
| 启动后很慢/没反应 | 检查网络；公司网络可能需要代理 |
| 想换登录账号 | `/logout` 后重新登录，或运行 `claude` 时重新授权 |
| 中文显示乱码 | 确认终端编码为 UTF-8（Windows 可用新版 Windows Terminal） |

## 动手试一试

1. 成功启动后，输入 `/help`，浏览一下都有哪些命令（不用记，混个眼熟）。
2. 再输入 `/cost`，看看一次对话大概消耗多少 —— 建立"它要花钱"的概念。
3. 输入 `/exit` 退出，再 `claude --continue` 一下，体会"继续上次会话"。

---

⬅️ 上一节：[01 · 什么是 Claude Code](01-what-is-claude-code.md) ｜ ➡️ 下一节：[03 · 基础交互](03-basics.md)
