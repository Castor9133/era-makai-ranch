# Emuera / ERB 常见错误与检查清单（era-makai-ranch）

**用途**：给人与 AI agent 在修改、审查 `ERB` 时对照；减少「能写进文件但 Emuera 1.824 解析/运行失败」类问题。  
**引擎基线**：本工程随包 `Emuera_readme.txt` 为 **Emuera 1.824**（与 eramaker 脚本兼容层；**非** C/Java 系语法）。

---

## 一、已踩过坑（务必记住）

### 1. 式中函数 `#FUNCTION` 在表达式里必须带 `()`

- **现象**：`"FOO"は解釈できない識別子`；严重时整行「解釈不可能」直接退出。
- **原因**：`@FOO` + `#FUNCTION` 定义的函数，在 `IF` / `SIF` / 表达式里必须写 **`FOO()`**，不能写裸标识符 `FOO`。
- **正例**：`SIF !PHIMOSIS_PLAYER_HAS_PHIMOSIS()`、`IF PHIMOSIS_PLAYER_HAS_PHIMOSIS() && …`
- **反例**：`IF PHIMOSIS_PLAYER_HAS_PHIMOSIS && …`（错误）
- **检查**（PowerShell，仓库根 `era-makai-ranch`）：

```powershell
$root = Join-Path (Get-Location) "ERB"
Get-ChildItem $root -Recurse -Filter "*.ERB" | ForEach-Object {
  Select-String -LiteralPath $_.FullName -Pattern 'PHIMOSIS_PLAYER_HAS_PHIMOSIS' | ForEach-Object {
    $ln = $_.Line.Trim()
    if ($ln -notmatch '@PHIMOSIS_PLAYER_HAS_PHIMOSIS' -and $ln -notmatch 'PHIMOSIS_PLAYER_HAS_PHIMOSIS\(\)') {
      "$($_.Path):$($_.LineNumber)"
    }
  }
}
```

（其它 `#FUNCTION` / `#FUNCTIONS` 同理，凡在表达式中出现均需 `()`。）

---

### 2. `FLAG` / `CFLAG` 名必须与 CSV 完全一致（简繁、用字）

- **现象**：`"口上显示"は解釈できない識別子`。
- **原因**：本工程 `CSV\Flag.csv` / `CSV\Cflag.csv` 登记的是 **`口上表示`**，不是「显示」。
- **规则**：新增开关前先查 `Flag.csv` / `Cflag.csv` / `Str.csv` 等，**复制粘贴 CSV 中的标识符**，避免同义不同字。
- **检查**：

```powershell
Select-String -Path "ERB\**\*.ERB" -Pattern "口上显示" -SimpleMatch
```

---

### 3. `CALL` / `TRYCALL` 实参与 `@子程序` 形参表必须一致（否则「引数が多すぎます」）

- **现象**：`PREGNANCY_SPAWN_DAUGHTER関数: 引数が多すぎます`。
- **原因**：Emuera 1.82x 要求子程序形参写在 `@` 行，例如 **`@SUB, ARG:0`**；仅写 `@SUB` 再 `CALL SUB, 1` 会判为「多传了参数」。
- **正例**：`@NURSERY_ADD_DAUGHTER, ARG:0` 与 `TRYCALL NURSERY_ADD_DAUGHTER, TARGET`
- **反例**：`@NURSERY_ADD_DAUGHTER` 却 `CALL NURSERY_ADD_DAUGHTER, x`
- **建议**：凡 `CALL xxx, a` / `TRYCALL xxx, a`，在 `@xxx` 行显式写 `, ARG:0`（或 `ARGS:0` 等），与文档一致。

---

### 4. `CALL` 推荐逗号形，避免 `CALL FUNC(a, b)` 括号形（与官方示例一致）

- **现象**：部分环境下与「引数个数/类型」报错纠缠，或与 `CALLFORM` 混淆。
- **规则**：优先 **`CALL FUNC, a, b`**；字符串常量 **`CALL FUNC, "深喉", ARGS:2`**。
- **检查思路**：对高频入口 `grep` / 人工扫 `CALL 大写前缀(`。

---

### 5. `@子程序` 形参名不要用 `ARGPHASE` 等「未登记标识符」

- **现象**：`"ARGPHASE"は解釈できない識別子`。
- **原因**：`@FOO(ARGPHASE)` 这类括号名并非 Emuera 标准形参写法；应使用 **`@FOO, ARGS:0`**（或 `ARG:0`）再在正文中用 **`ARGS:0`**。
- **正例**：`@KOJO_SHARE_ADV_DISPATCH_IRUMA, ARGS:0` + `SELECTCASE ARGS:0`

---

### 6. `MONEY` 等带下标变量须与 `Money.csv` 行一致

- **现象**：`"所持金"は解釈できない識別子`。
- **原因**：本工程 `Money.csv` 为 **`0,持有金`**，应使用 **`MONEY:0`**，没有 `MONEY:所持金` 这种别名。
- **规则**：凡 `MONEY:xxx` 的 `xxx` 必须是 CSV 第二列已登记名或合法下标约定。

---

### 7. 禁止 `SIF` 下一行直接 `IF`（同一逻辑块）

- **现象**：`SIF文の次の行を"IF"文にすることはできません`；并可能连带一串「假错误」。
- **原因**：Emuera 语法限制。
- **修法**：外层改为 **`IF …` … `ENDIF`**；或合并条件；**不要**指望用 `{` `}` 代替 `ENDIF`（见下条）。
- **检查**（非法模式：制表符 + `SIF NOWEX:` 且下一行是更深的 `IF`）：

```powershell
$root = "ERB"
foreach ($f in Get-ChildItem $root -Recurse -Filter "*.ERB") {
  $lines = Get-Content -LiteralPath $f.FullName -Encoding UTF8
  for ($i=0; $i -lt $lines.Count-1; $i++) {
    if ($lines[$i] -match '^\tSIF NOWEX:' -and $lines[$i+1] -match '^\t\tIF ') {
      Write-Host "$($f.FullName):$($i+1)"
    }
  }
}
```

**说明**：单独一行 `SIF NOWEX:Ｖ绝顶` 下接 **`CALL` 或单行语句** 通常是合法的；问题集中在 **`SIF` + 下一行 `IF` 块`**。

---

### 8. 不要用 C/Java 风格 `{` `}` 块代替 `IF`/`ENDIF`

- **现象**：`対応する"ENDIF"の無い"IF"文`。
- **原因**：Emuera 以 **`IF`/`ELSEIF`/`ELSE`/`ENDIF`** 配对为主；`{` `}` 不是可靠块语法。
- **修法**：全部展开为 `IF` … `ENDIF`。

---

### 9. `SIF` 与 `ELSEIF` 不能直接串（`ELSEIF` 必须跟在 `IF`/`ELSEIF` 后）

- **现象**：`IF～ENDIFの外で"ELSEIF"文が使われました`。
- **修法**：最外层改为 **`IF` … `ELSEIF` … `ENDIF`**，不要用 `SIF` 开头再接 `ELSEIF`。

---

### 10. `CALL MESSAGE_BOX,@"……` 多行字符串必须落在同一对 `@" … "` 内

- **现象**：`""が閉じられていません`。
- **修法**：中间断行用 **`\n`** 或拆成多次 `CALL MESSAGE_BOX`，**不要**在 `@"` 未闭合前物理换行。

---

### 11. `#DIM` / `#DIMS` 须在**本函数**内、且在**首次使用**变量之前

- **现象**：`変数"LPR"はこの関数中では定義されていません`（或 `TIER` 等）。
- **原因**：把 `#DIMS LPR` 写在中间 `RETURN` 之后、或写在 `IF` 块之后才执行到。
- **修法**：紧跟 `@子程序` 后声明；子程序带参时优先用 **`ARG` / `ARGS`** 或 `@NAME, ARG:0` 与 `SELECTCASE ARG:0`。

---

### 12. `MESSAGE_BOX` 内嵌 `%SELF_CALL()%` 等宏勿漏写括号

- **现象**：`"SELF_CALL"は解釈できない識別子`（或同类）。
- **反例**：`%SELF_CALL%`、`%SELF_CALL`（缺 `%` 或缺 `()` 视引擎宏规则而定）
- **正例**：与工程内既有口上一致，使用 **`%SELF_CALL()%`**。

---

### 13. `NOWEX` / `EX` 等名须与 `Nowex.csv`、`exp.csv` 等完全一致

- **现象**：`"Ｕ绝顶"は解釈できない識別子`、`"尿道调教经验"` 等。
- **规则**：从对应 CSV **原样复制** 列名（全角半角、`Ｕ` 与 `U` 等易混）。
- **说明**：若 CSV 已登记仍报错，先排除 **上文的语法错误**（未闭合 `IF`/`@"`）导致的级联误报。

---

### 14. 魔改常量 `#DIM`：全文件用同一套字符（简繁、`_产_` vs `_産_`）

- **现象**：`"魔界_有効_产褥"は解釈できない識別子`（多为**另一处**拼写与 `#DIM` 行不一致，或解析顺序导致未见到定义）。
- **规则**：常量名在 **`#DIM` / 使用处 / 注释** 中保持**字节级一致**；避免同一概念混用「产/産」「园/園」。

---

### 15. 文件编码

- **风险**：用工具批量写回 `UTF-8` 无 BOM 后，若你本地习惯 **Shift_JIS**，可能出现乱码。
- **规则**：批量替换后随机抽几个含日文/中文的 ERB 在编辑器里确认编码；与团队约定 **UTF-8 BOM** 或 **CP932** 二选一并写进本文件修订记录。

---

## 二、改完后的最小验证

1. 启动 **`Emuera.exe`**，确认不再出现 **`解釈不可能な行`** 直接退出。  
2. 打开 **`emuera.log`**，对 **`警告Lv2`**、**`エラー`** 逐条清零或评估为可接受。  
3. 对本次改动过的 `ERB`，在仓库根执行第一节中的 **PowerShell 检查片段**（按需增删关键字）。

---

## 三、与其它项目（fc-pregmod 等）的边界

- **`fc-pregmod`（`bin/*.html` + SugarCube）**：语法为 JavaScript/HTML，**不适用**本清单的 `CALL`/`@`/`ENDIF` 规则；错误模式完全不同。  
- **本清单仅适用于**：`era-makai-ranch` 下 **Emuera + ERB** 工作流。

---

## 四、修订记录

| 日期 | 说明 |
|------|------|
| 2026-05-03 | 初版：根据一次大规模编译报错修复过程归纳（`#FUNCTION` 括号、`口上表示`、形参表、`MONEY`、`SIF`/`IF`、`{}`、`MESSAGE_BOX` 多行、`#DIM` 顺序、`CALL` 逗号形、`ARGS` 形参名等）。 |

---

**给其他 agent 的短指令**：在修改 `era-makai-ranch/ERB` 后，必须先对照本文 **第一节**，再跑 **第二节**；若引入新 `FLAG`/`CFLAG`/`MONEY` 名，必须先改 **CSV** 再写 **ERB**，且全仓库搜索避免「显示/表示」类混用。
