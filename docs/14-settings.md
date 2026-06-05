# 14 · 配置 settings.json

> 本节目标：了解 Claude Code 的配置文件 `settings.json`，学会把你的偏好、权限规则持久化下来。这是把前面所学"固化"的地方。

## 是什么

`settings.json` 是 Claude Code 的**配置文件**。前面学的很多东西 —— 权限规则、Hooks、环境变量、模型偏好 —— 都可以写进它，从而**持久生效**（重启依然记得），而不是每次手动设置。

## 配置文件在哪

按"作用范围"从大到小，常见有三层（**范围小的会覆盖范围大的**）：

| 文件 | 作用范围 | 用途 |
|------|----------|------|
| `~/.claude/settings.json` | 你的所有项目（用户级） | 个人通用偏好 |
| `<项目>/.claude/settings.json` | 当前项目，**可提交进 Git** | 团队共享的项目配置 |
| `<项目>/.claude/settings.local.json` | 当前项目，**不进 Git**（本地私有） | 你个人在本项目的私有设置、密钥 |

> 💡 团队协作约定：共享的规则放 `settings.json` 提交进仓库；个人私有的放 `settings.local.json`（记得加进 `.gitignore`）。

## 能配什么（常见项）

### 1. 权限规则（最常用）
把"哪些操作允许/询问/禁止"固化下来，免得每次都点批准：

```json
{
  "permissions": {
    "allow": [
      "Bash(npm test)",
      "Bash(npm run lint)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Read(./.env)"
    ],
    "ask": [
      "Bash(git push:*)"
    ]
  }
}
```

含义：测试/lint 直接放行不打扰；危险删除和读 `.env` 永久禁止；`git push` 每次都问。
（对应 [第 06 节](06-permissions.md) 学的三种处置：allow / ask / deny。）

### 2. Hooks 钩子
自动化规则（见 [第 13 节](13-hooks.md)）也写在这里的 `"hooks"` 字段下。

### 3. 环境变量
给会话注入环境变量：

```json
{
  "env": {
    "MY_API_BASE": "https://api.example.com"
  }
}
```

### 4. 其它
模型偏好、是否启用某些功能等，具体字段以官方文档为准。

## 怎么改（推荐姿势）

⚠️ **JSON 格式很挑剔**（少个逗号、多个逗号都会报错）。新手最稳的两种方式：

### 方式一：让 Claude Code 帮你改 ⭐强烈推荐
直接说需求，它会用正确的格式和当前版本的字段帮你写：
```
帮我在项目的 settings.json 里允许所有 pytest 命令不再询问，并禁止读取 .env 文件
```
它知道正确写法，还会避免你手抖写坏 JSON。

### 方式二：用 `/config` 和 `/permissions`
- `/config`：图形化地改常见设置（主题、模型等）。
- `/permissions`：交互式地增删权限规则，它会替你写回 settings.json。

### 方式三：手动编辑
打开对应的 `settings.json` 自己改。改完确保是合法 JSON。

## 安全须知

- ✅ **密钥不要写进会提交的文件**：放 `settings.local.json` 并 gitignore，或用环境变量。
- ✅ **`allow` 要克制**：只放行真正安全、重复的操作；危险命令宁可保持 `ask`。
- ✅ 善用 `deny` 给自己上保险，比如永久禁止 `rm -rf`、禁止读敏感文件。

## 动手试一试

1. 启动 `claude`，让它帮你配置（练习项目，随便试）：
   ```
   帮我在本项目的 .claude/settings.json 里添加权限：允许所有 python 命令不再询问。改完把文件内容展示给我看。
   ```
2. 观察它创建/修改了 `.claude/settings.json`，看看生成的 JSON 结构。
3. 输入 `/permissions`，确认刚加的规则出现在列表里。

---

⬅️ 上一节：[13 · Hooks 钩子](13-hooks.md)

> 🎉 **恭喜你完成全部 14 节！** 你已经从零认识了 Claude Code 的核心与进阶功能。
> 接下来：去 [exercises/](../exercises/README.md) 用真实任务巩固，并把 [CHEATSHEET](../CHEATSHEET.md) 收藏起来随时查。
> 最好的学习方式，就是**现在就用它做你手头真实的项目**。
