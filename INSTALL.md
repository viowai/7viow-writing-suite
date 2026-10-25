# 安装与使用

能运行终端的 Agent 用命令安装；账号技能库按上传要求选 ZIP；ChatGPT Work 等原生插件入口使用平台的插件机制。

## 让 Agent 安装

把下面一句话发给当前 Agent：

```text
请从 https://github.com/viowai/7viow-writing-suite 安装这三个写作技能到当前 Agent，按仓库 INSTALL.md 操作，并确认技能已可见。
```

执行此请求的 Agent 先识别当前宿主和安装范围，沿用用户已有决定；未指定范围时使用当前项目。使用下表准确的 `--agent` 参数，仅安装所选技能。用户只选一个时按 `SKILL.md` 的稳定名称安装；每个目录保留完整 references、scripts、metadata 和法律文件。只复制 SKILL.md 会丢失写作方法。

已有同名技能时，保留用户的本地修改再更新原入口；不要同时启用目录版和同名插件版。完成后检查实际文件与宿主发现结果。没有终端、文件写入权限或导入能力时，提供对应上传步骤，不声称已经安装。安装不要求配置本套装的 MCP、Hook、后台服务或额外模型账号。

## 一条命令安装

需要 Node.js 22.20+。以下使用 Skills CLI 1.7.4，可在 macOS/Linux 终端或 PowerShell 运行；在目标项目目录执行：

```bash
npx --yes skills@1.7.4 add viowai/7viow-writing-suite --agent codex --skill "*" --copy --yes
```

固定安装本次发行时，将命令中的 `viowai/7viow-writing-suite` 换成 `https://github.com/viowai/7viow-writing-suite/tree/v0.2.0`。

只需要 Editor 时，把 `--skill "*"` 换成 `--skill 7viow-writing-editor`。更换宿主时只替换 `--agent` 参数：

| 宿主 | 参数值 | 当前项目的技能目录 |
|---|---|---|
| Codex | `codex` | `.agents/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` |
| Cursor | `cursor` | `.agents/skills/` |
| GitHub Copilot | `github-copilot` | `.agents/skills/` |
| OpenCode | `opencode` | `.agents/skills/` |
| Google Antigravity / Antigravity CLI | `antigravity` / `antigravity-cli` | `.agents/skills/` |
| Gemini CLI | `gemini-cli` | `.agents/skills/` |
| Grok Build | `grok` | `.grok/skills/` |
| CodeBuddy | `codebuddy` | `.codebuddy/skills/` |
| TRAE / TRAE CN | `trae` / `trae-cn` | `.trae/skills/` |
| Qoder / Qoder CN | `qoder` / `qoder-cn` | `.qoder/skills/` |
| ZCode | `zcode` | `.zcode/skills/` |

跨项目使用加 `--global`，安装器会选择对应个人目录。多个宿主可在 `--agent` 后一起列出；`--all`会选择所有宿主，不用于普通单宿主安装。详情见 [CLI命令](https://github.com/vercel-labs/skills/blob/v1.7.4/docs/commands.md) 和 [宿主表](https://github.com/vercel-labs/skills/blob/v1.7.4/docs/agents.md)。

Antigravity App的个人目录按[官方说明](https://www.antigravity.google/docs/skills)使用 `~/.gemini/config/skills/`。Skills CLI 1.7.4的 `antigravity --global` 仍指向旧目录 `~/.gemini/antigravity/skills/`；App优先使用上表项目级命令，跨项目使用则复制完整目录到官方个人位置。Antigravity CLI另有独立目录，不混用两者。

Node.js用于这条安装命令，普通写作不依赖Node.js。也可下载源码ZIP，解压后把 `skills/` 下选中的完整目录复制到上述位置；使用个人目录时按宿主官方说明选择路径。

## 上传技能包

从 [GitHub Releases](https://github.com/viowai/7viow-writing-suite/releases/latest) 下载。每次选择一个技能，按需要分别安装三个；不要把整套源码ZIP直接当成单技能上传。

| 入口 | 选择与操作 |
|---|---|
| Claude账号技能库 | 选 `-folder.zip`，在 Customize → Skills 上传并启用；需账号开放该功能并启用代码执行。见 [官方说明](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) |
| Gemini Enterprise | 选 `-upload.zip`；Skills → Upload skill → Import。官方也接受单一外层文件夹结构；需要管理员启用，Frontline不允许自行上传。见 [官方说明](https://docs.cloud.google.com/gemini/enterprise/docs/skills) |
| M365 Agent Builder预览 | 选 `-upload.zip`，Configure → Skills → Add；仅适用符合条件的Frontier组织。见 [官方说明](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills) |
| 千问办公组织技能 | 选 `-folder.zip`，管理员在组织技能中添加并上传，按需要设置团队可见性。见 [官方说明](https://www.alibabacloud.com/help/zh/qwenwork/skills-management) |
| DuMate | 专家套件·技能 → 添加 → 安装技能，支持完整ZIP或GitHub URL导入；每次一个技能。多文件URL识别需在客户端确认，ZIP可保留全部引用。见 [官方说明](https://cloud.baidu.com/doc/Dumate/s/9mrdg87nq) |
| ChatGPT Work / ChatGPT插件入口 | 使用平台插件目录或已配置的个人/组织插件市场。GitHub仓库公开不会自动上架；本仓库未提供已上架插件安装链接。见 [官方说明](https://learn.chatgpt.com/docs/plugins) |

普通技能上传选择下表 `-folder.zip` 或 `-upload.zip`。`-plugin.zip` 供接受相应插件结构的宿主或插件市场使用，不能替代单技能上传；整套目录见 [skills.zip](https://github.com/viowai/7viow-writing-suite/releases/latest/download/7viow-writing-suite-skills.zip)，完整仓库快照见 [source.zip](https://github.com/viowai/7viow-writing-suite/releases/latest/download/7viow-writing-suite-source.zip)。

单技能下载：

| 技能 | 带顶层技能文件夹 | SKILL.md位于ZIP根目录 |
|---|---|---|
| Writing Partner | [folder.zip](https://github.com/viowai/7viow-writing-suite/releases/latest/download/7viow-writing-partner-folder.zip) | [upload.zip](https://github.com/viowai/7viow-writing-suite/releases/latest/download/7viow-writing-partner-upload.zip) |
| Writing Editor | [folder.zip](https://github.com/viowai/7viow-writing-suite/releases/latest/download/7viow-writing-editor-folder.zip) | [upload.zip](https://github.com/viowai/7viow-writing-suite/releases/latest/download/7viow-writing-editor-upload.zip) |
| Deck Writing Editor | [folder.zip](https://github.com/viowai/7viow-writing-suite/releases/latest/download/7viow-deck-writing-editor-folder.zip) | [upload.zip](https://github.com/viowai/7viow-writing-suite/releases/latest/download/7viow-deck-writing-editor-upload.zip) |

WorkBuddy、TRAE导入、Qoder桌面、千问办公个人入口、豆包工作、dots、Grok Bot、库库AI及Comate的具体多文件导入步骤仍待客户端确认。上表命令行目录支持不等于这些账号或桌面入口也适用；优先查看客户端官方导入说明。

## 确认可用

查看安装器记录：

```bash
npx --yes skills@1.7.4 list --agent codex
```

全局安装的查询也加 `--global`。随后在Agent技能列表确认所选入口；如当前会话未刷新，新开会话或刷新技能列表，再发一条真实请求：

```text
用 Writing Editor 修改下面这段文字，保留事实和数字，直接给修改稿：……
```

三个技能独立工作，无需先执行初始化技能。更多请求示例见 [README](README.md#选择技能开始写作)。

Talis 是可选的 Mac 请求整理工具，Writing 的安装命令只安装写作技能。协作方式与各角色模板见 [README](README.md#与-talis-配合可选)；已有 Talis 的用户可直接复制使用。

## 更新和移除

更新由你手动触发：保留本地改动后，再运行相同的安装命令，保持安装范围和宿主参数一致；上传型入口重新上传对应包，按平台要求替换旧版本。

移除当前项目的三个Codex技能：

```bash
npx --yes skills@1.7.4 remove 7viow-writing-partner 7viow-writing-editor 7viow-deck-writing-editor --agent codex --yes
```

个人目录版本加 `--global`；只移除一个时只保留其名称。手动复制的目录按宿主的移除方式处理，保留其他技能。

## 常见问题

- 找不到技能：核对宿主参数、项目/个人范围、实际目录和 `SKILL.md`，再刷新技能列表；网页端不会自动读取本机技能目录。
- 找不到方法：重新安装完整目录，保持references与SKILL.md的相对位置。
- Node版本不满足：使用Node.js 22.20+，或下载源码ZIP按目录安装。
- 网络无法访问GitHub或npm：下载对应完整ZIP后导入；安装请求不能绕过网络和账号权限。
- 有重复入口：检查是否同时装了个人版、项目版或插件版，保留需要的范围与入口。

本机Codex的安装与技能发现已验证。其它入口的目录映射或上传要求不等于已在每个客户端、模型和账号上完成运行验证；按实际宿主权限使用文件编辑、脚本和其它工具。
