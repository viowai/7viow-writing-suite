# 7viow Writing Suite

三个独立的 writing skills，帮助你探索表达、编辑正文和组织演示内容。可以只装一个，也可以让它们协作。使用你当前 Agent 的模型，无需本套装专用账号或 API Key。

## 一句话安装

在能访问 GitHub、执行命令和写入项目文件的 Agent 中发送：

```text
请从 https://github.com/viowai/7viow-writing-suite 安装这三个写作技能到当前 Agent，按仓库 INSTALL.md 操作，并确认技能已可见。
```

也可以把“三个写作技能”换成“Writing Editor”，只安装正文编辑技能。

如果你自己使用终端，下面以 Codex 为例。先准备 Node.js 22.20+，在目标项目目录运行：

```bash
npx --yes skills@1.7.4 add viowai/7viow-writing-suite --agent codex --skill "*" --copy --yes
```

Claude Code 把 `codex` 换成 `claude-code`，Cursor 换成 `cursor`。默认只用于当前项目；Codex跨项目使用时加 `--global`，其它宿主的个人目录与例外见安装说明。完整宿主参数、上传方式、更新和卸载见 [安装说明](INSTALL.md)。

使用 Claude 网页版、Gemini Enterprise、千问办公等上传入口时，从 [下载页](https://github.com/viowai/7viow-writing-suite/releases/latest) 选择对应的单技能 ZIP，具体选择见 [上传方式](INSTALL.md#上传技能包)。

## 选择技能，开始写作

[套装 v0.3.0](https://github.com/viowai/7viow-writing-suite/releases/tag/v0.3.0) 包含以下三个技能。套装与技能分别编号，更新时以对应入口为准。

| 技能 | 版本 | 适合做什么 | 安装后的第一条请求 |
|---|---|---|---|
| [Writing Partner](skills/7viow-writing-partner/SKILL.md) | 0.7.0 | 找作者声音、发展营销概念、比较表达方向、连续共写 | 用 Writing Partner，根据这些事实给我三个不同的开头，再按我选中的方向继续写。 |
| [Writing Editor](skills/7viow-writing-editor/SKILL.md) | 0.8.0 | 直接审阅、改稿、编辑文件，或从明确简报成稿 | 用 Writing Editor 修改下面这段文字，保留事实、数字和我的立场：…… |
| [Deck Writing Editor](skills/7viow-deck-writing-editor/SKILL.md) | 0.7.0 | 安排演示叙事、页序、页面文字、讲稿与制作交接 | 用 Deck Writing Editor，把这些材料整理成6页演示内容，每页给标题、屏幕文案和讲述支持。 |

在 Codex 可用 `$7viow-writing-partner`、`$7viow-writing-editor`、`$7viow-deck-writing-editor` 明确调用；其他宿主可从技能菜单选择，或在请求中写出名称。安装后如果当前会话没有显示新技能，先新开会话或刷新技能列表。

三个技能各自带齐方法与资源。组合时由当前文稿主责整合修改，无需按固定顺序调用。Deck 负责演示内容；实际 PPTX 编辑、排版和导出使用宿主已有工具或你选择的制作技能。

## 与 Talis 配合（可选）

Mac 用户可以用 [Talis](https://github.com/viowai/7viow-talis) 补齐写作需求，或把常用请求保存为个人模板。需求已经明确时，直接在当前 Agent 写作；三个技能各自可以独立使用。

| 当前需要 | 配合方式 | 可复制的请求模板 |
|---|---|---|
| 读者、用途或表达方向还不清楚 | 在 Talis 用追问模式补齐关键条件，再回到 Partner 探索写法 | [Writing Partner 模板](skills/7viow-writing-partner/references/source-and-handoff.md#talis-handoff) |
| 经常按同一套规则改稿 | 保存保留事实、修改范围和目标语气，下次替换原文 | [Writing Editor 模板](skills/7viow-writing-editor/references/cooperation-and-output.md#talis-handoff) |
| 反复准备同类汇报 | 保存听众、预期决定、材料版本和已确认主线，再交给 Deck | [Deck Writing Editor 模板](skills/7viow-deck-writing-editor/references/artifact-and-handoff.md#talis-handoff) |

已在用 Talis 时，直接填写模板并复制请求回来；材料文件通过接收工具的附件功能提供。Talis 负责整理和保存请求，写作与技能调用在接收端完成。非 Mac 用户也可以把同一份模板保存在当前工具中。

需要安装 Talis 的 Mac 用户可使用其[源码安装说明](https://github.com/viowai/7viow-talis/blob/main/docs/agent-install.md)。手动填写和复制模板无需 AI 调用；Talis 的追问与 AI 改写使用你在 App 中配置的模型。

## 调整文风

默认使用严格文风。写作质量门禁检查读者能否理解、文字是否有用，以及标点、句式、结构和重复表达是否需要调整；确认缺陷或超过当前额度时修改并复查，保留事实、真实引文、必要术语和你指定的格式。

首次写作会提示可调整设置。你可以直接说：

```text
风格=标准。
```

或者逐项设置：

```text
风格=自定义，基于=严格，双引号每千字2对，破折号0处，加粗比例5%。
```

选择沿用到当前稿件的后续修改。完整额度及例外见 [写作质量门禁](skills/7viow-writing-editor/references/prose-quality-gate.md)，每个独立技能均带有相同规则。

## 使用条件

宿主需要支持 Agent Skills 并能读取完整技能目录。修改文件需要文件读写权限；普通写作不需要执行脚本。Editor 的可选检查脚本使用 Python 3.10+ 标准库。

GitHub 仓库安装、账号技能上传和原生插件安装是不同入口。支持目录安装不代表同品牌网页端也能读取本机目录；各入口见 [安装说明](INSTALL.md)。模型与账号的数据处理规则由所用宿主决定。

## 许可与作者

作者与维护者：**Viow**。**7viow**为产品系列品牌。

Copyright 2026 Wenbin Li。原创部分采用 [Apache-2.0](LICENSE)，适用第三方声明和完整许可见 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。普通写作成品无需添加7viow署名；用户输入和引用作品保留各自权利。

维护与更新由使用者手动触发。

使用遇到问题可提交 [Issue](https://github.com/viowai/7viow-writing-suite/issues)，注明宿主、技能名称和可复现步骤，并移除私人材料。
