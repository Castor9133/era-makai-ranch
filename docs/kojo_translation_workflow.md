# 口上 MESSAGE_BOX 翻译流水线（可选）

本仓库口上正文约定见 **`docs/口上创作DEMO与性格扩展清单.md`**（玩家可见台词建议统一简体中文）。下列脚本用于**批量抽取** `CALL MESSAGE_BOX,@"…"`、**分批机翻/人工填译**、**校验占位符**、**回写 ERB**。

## 依赖

- Python 3.10+
- `requirements-kojo-i18n.txt`（无第三方硬性依赖）

## 命令一览（在仓库根目录）

```bash
python scripts/kojo_extract_translatables.py
```

生成 `out/kojo_messagebox_strings.jsonl`（字段：`id`, `path`, `line`, `source`）。

```bash
python scripts/kojo_export_batches.py --in out/kojo_messagebox_strings.jsonl --size 500
```

生成 `out/batches/part_00001.jsonl` … 与 `out/BATCH_PROGRESS.md`。

对每条记录**补全** `zh_CN` 后：

```bash
python scripts/kojo_import_batches.py --dir out/batches
```

合并为 `out/kojo_messagebox_translations.jsonl`。

```bash
python scripts/kojo_validate_translations.py --translations out/kojo_messagebox_translations.jsonl
```

检查 `%…%` 占位符数量与集合是否与 `source` 一致。

```bash
python scripts/kojo_apply_translations.py --translations out/kojo_messagebox_translations.jsonl
```

将 `zh_CN` 写回对应 ERB（按 `path` + `line` + `source` 定位）。

也可以使用统一入口：

```bash
python scripts/kojo_i18n_pipeline.py extract
python scripts/kojo_i18n_pipeline.py export-batches --in out/kojo_messagebox_strings.jsonl
python scripts/kojo_i18n_pipeline.py import-batches --dir out/batches
python scripts/kojo_i18n_pipeline.py validate --translations out/kojo_messagebox_translations.jsonl
python scripts/kojo_i18n_pipeline.py apply --translations out/kojo_messagebox_translations.jsonl
```

## 约定

- **`CASE "……"`** 内的指令名、 **`%MASTER_CALL()%` 等占位符**：勿改或与工程不一致。
- 译文中的双引号 `"` 会自动写成 `""`（Emuera `@"` 字面量规则）。
- 回写前务必 **validate**，避免占位符遗漏导致运行时展开错误。
