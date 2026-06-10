# 12 · MCP 扩展

> 本节目标：理解 MCP 是什么，它如何让 Claude Code 连接外部世界（数据库、浏览器、第三方服务）。进阶功能，了解为主。

## 是什么

**MCP（Model Context Protocol，模型上下文协议）** 是一个开放标准，让 Claude Code 能**连接外部工具和数据源**。

默认情况下，Claude Code 能操作你的文件和命令行。但通过 MCP，它还能：

- 🗄️ 查询**数据库**（PostgreSQL、SQLite 等）
- 🌐 控制**浏览器**（打开页面、点击、截图 —— 用于测试或抓取）
- 🐙 操作 **GitHub / GitLab**（管理 issue、PR）
- 📋 连接 **Jira、Slack、Notion** 等团队工具
- 🔧 接入你公司内部的自定义服务

类比：MCP 就像给 Claude Code 装"扩展插件 / 外设接口"。核心功能是身体，MCP 让它能接上各种"外接设备"。

## 它解决什么问题

没有 MCP：你想让它根据数据库里的数据做事，得自己导出再贴给它。
有了 MCP：它**直接连数据库查**。同理，它能直接开浏览器验证你的网页改动、直接在 GitHub 上建 issue。

一句话：**MCP 把"Claude Code 能感知和操作的范围"从你的本地文件扩展到了整个外部世界。**

## 怎么用

### 查看已连接的 MCP 服务器
```
/mcp
```
显示当前接了哪些 MCP 服务器、状态如何、提供哪些工具。

### 添加 MCP 服务器
MCP 服务器通过配置添加。常见做法是在配置文件里声明一个服务器（命令、参数、环境变量等）。例如（示意）：

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "./mydata.db"]
    }
  }
}
```

> 具体配置因服务器而异，安装时看对应 MCP 服务器的说明文档。官方与社区有大量现成的 MCP 服务器可用。

### 使用
连上之后就**自然语言驱动**，例如（假设连了数据库）：
```
查一下 users 表里最近注册的 10 个用户
```
Claude Code 会通过 MCP 工具去执行。

## 实战：连接 GitHub MCP 服务器

前面是"示意"，这里给一个**能真正跑通**的例子 —— 让 Claude Code 连上 GitHub，帮你查 / 建 issue 和 PR。

### 第 1 步：写配置文件

在**项目根目录**新建 `.mcp.json`（这种放在项目里的配置叫"项目级配置"，可以随仓库提交给团队共享）：

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PAT}"
      }
    }
  }
}
```

这里用的是 GitHub 官方托管的**远程 MCP 服务器**（`https://api.githubcopilot.com/mcp/`），不用本地安装。

### 第 2 步：准备一个 GitHub 令牌（PAT）

`${GITHUB_PAT}` 是个**环境变量占位符**，Claude Code 启动时会自动把它替换成你电脑里 `GITHUB_PAT` 这个环境变量的值。这样配置文件里**不出现真实密钥**，即使提交进仓库也安全。

1. 打开 https://github.com/settings/personal-access-tokens/new ，创建一个 fine-grained token。
2. 选中你要操作的仓库。
3. 在 **Repository permissions** 里按需给权限：
   - 只想**查询**：Issues、Pull requests、Contents 给 `Read-only` 即可。
   - 还想**创建 issue / PR**：把对应项改成 `Read and write`（光有只读会报 403）。
4. 生成后复制那串 `github_pat_xxx`（只显示一次）。
5. 把它设成环境变量（Windows PowerShell）：
   ```bash
   setx GITHUB_PAT "github_pat_你复制的那串"
   ```

### 第 3 步：重启后启用

`setx` 设的环境变量**只对之后新启动的进程生效**，所以要**完全退出并重启** Claude Code（在 VS Code 里"重新加载窗口"不够，要整个关掉 VS Code 再开）。重启后输入 `/mcp`，看到 `github` 变成 ✓ connected 就成功了。然后就能自然语言驱动：

```
帮我查一下当前仓库有哪些未关闭的 issue
```

## 常见报错排查

第一次配 MCP 很容易卡住，下面是几个高频问题：

| 报错 / 现象 | 原因 | 解决 |
| --- | --- | --- |
| `SDK auth failed: Incompatible auth server: does not support dynamic client registration` | Claude Code 在走 OAuth 自动注册，但 GitHub 不支持这种方式 | 改用 PAT（即上面 `headers` 里的 `Bearer ${GITHUB_PAT}` 写法） |
| 设了环境变量还是读不到 / 连接为空 | `setx` 只对新进程生效，旧的 Claude Code 没继承到 | **完全重启** VS Code / Claude Code，别只"重新加载窗口" |
| 已经改成 PAT 了，却还在报 OAuth 错误 | 之前失败的 OAuth 状态被缓存了 | 清理 `~/.claude/.credentials.json` 里 `mcpOAuth` 下的相关条目，再重启 |
| 创建 issue 报 `403 Resource not accessible by personal access token` | token 只有读权限 | 把对应权限（如 Issues）改成 `Read and write` |

> 小技巧：想确认到底是"网络不通""token 无效"还是"Claude Code 端问题"，可以用 `curl` 单独验证：
> ```bash
> # 验证 token 是否有效（返回 200 即有效）
> curl -s -o /dev/null -w "%{http_code}\n" -H "Authorization: Bearer 你的token" https://api.github.com/user
> ```

## 安全须知（重要）

MCP 让 Claude Code 能接触外部系统，**权限和信任要格外注意**：

- ⚠️ 只连接**你信任的** MCP 服务器，第三方服务器可能能读你的数据。
- ⚠️ 连生产数据库要极其谨慎，**优先用只读账号**。
- ⚠️ 通过 MCP 把数据发给外部服务，等于"对外发布"，注意敏感信息。
- ✅ 权限系统同样管 MCP 工具调用，危险操作仍会请求批准。
- 🔑 **密钥别写死在配置里**：用 `${环境变量}` 占位符，不要把真实 token 明文写进 `.mcp.json`（它会被提交进仓库）；万一泄露，及时去 GitHub 吊销重建。

## 什么时候关注它

- 入门期：**完全可以先跳过**。把本地开发玩熟再说。
- 进阶期：当你需要"让 AI 直接连你的数据库/浏览器/团队工具"时，再来研究具体接哪个 MCP 服务器。

## 动手试一试

本节无需真的安装服务器，先建立认知：

1. 启动 `claude`，输入 `/mcp`，看看当前有没有连接 MCP 服务器（很可能没有，这正常）。
2. 问它：
   ```
   MCP 能让你连接哪些类型的外部工具？给我三个实际场景的例子。
   ```
3. 思考一下：你自己的工作里，有哪个外部系统如果能让 AI 直接连，会很省事？

---

⬅️ 上一节：[11 · Subagents 子代理](11-subagents.md) ｜ ➡️ 下一节：[13 · Hooks 钩子](13-hooks.md)
