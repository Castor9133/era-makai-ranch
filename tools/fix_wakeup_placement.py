#!/usr/bin/env python3
"""Fix CASE "叫早" placement: move from inside 调教 SELECTCASE ARGS:2 to SELECTCASE ARGS:1 level."""

import os
import re

BASE = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上"

# Files that need fixing (CASE "叫早" is nested inside 调教)
FILES = [
    "仇恨口上1.ERB",
    "堅物口上1.ERB",
    "元気っ子口上1.ERB",
    "天然口上1.ERB",
    "大和抚子口上1.ERB",
    "懦弱口上1.ERB",
    "気品口上1.ERB",
    "温柔大姐姐口上1.ERB",
    "無口口上1.ERB",
    "知心口上1.ERB",
    "虔诚口上1.ERB",
    "闷骚小姐姐口上1.ERB",
]

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    # Strategy: Find CASE "叫早" that appears inside 调教 block (indented with \t\t)
    # and move it to after the ENDSELECT that closes 调教's SELECTCASE ARGS:2

    new_lines = []
    wakeup_block_lines = []  # lines of the CASE "叫早" block (to be re-inserted later)
    in_wakeup = False
    wakeup_depth = 0
    insert_wakeup_at = -1  # line index after which to insert the wakeup block
    removed_count = 0

    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect CASE "叫早" at the WRONG level (inside 调教 = starts with \t\tCASE)
        if not in_wakeup and re.match(r'^\t\tCASE "叫早"$', line):
            in_wakeup = True
            wakeup_depth = 1
            # Collect the entire CASE "叫早" block
            # Adjust indentation: reduce by one tab
            adjusted_line = '\t' + line[2:] if line.startswith('\t\t') and not line.startswith('\t\t\t') else line[1:] if line.startswith('\t\t\t') else line
            wakeup_block_lines.append(adjusted_line)
            i += 1
            removed_count += 1
            continue

        if in_wakeup:
            # Count tabs at start to track depth
            stripped = line.lstrip('\t')
            current_indent = len(line) - len(stripped)

            if stripped == '':
                # Empty line - include it
                adjusted = '\t' + line[2:] if line.startswith('\t\t') and not line.startswith('\t\t\t') else line[1:] if line.startswith('\t\t\t') else line
                wakeup_block_lines.append(adjusted)
                i += 1
                continue

            # Check if we're exiting the CASE "叫早" block
            # The wakeup block starts at indent level 2 (two tabs for CASE "叫早")
            # We exit when we hit a line at indent level 2 that starts a new CASE
            if current_indent <= 2 and stripped.startswith('CASE ') and '叫早' not in stripped:
                in_wakeup = False
                # This line is NOT part of the wakeup block, process normally
                new_lines.append(line)
                i += 1
                continue

            # Still in wakeup block - adjust indentation and add
            if line.startswith('\t\t\t\t'):  # 4 tabs -> 3 tabs
                adjusted = '\t' + line[3:]
            elif line.startswith('\t\t\t'):  # 3 tabs -> 2 tabs
                adjusted = '\t' + line[2:]
            elif line.startswith('\t\t'):  # 2 tabs -> 1 tab
                adjusted = '\t' + line[1:]
            else:
                adjusted = line

            wakeup_block_lines.append(adjusted)
            removed_count += 1
            i += 1
            continue

        # Not in wakeup block - check if this is where we should insert the wakeup block
        # We insert after CASE "调教"'s ENDSELECT and before CASE "探索魔界" (at ARGS:1 level)
        if (re.match(r'^\t\tENDSELECT$', line) and
            i + 1 < len(lines) and
            re.match(r'^\tCASE "探索魔界"$', lines[i + 1].lstrip('\t'))):
            new_lines.append(line)
            if wakeup_block_lines:
                new_lines.extend(wakeup_block_lines)
                wakeup_block_lines = []
                print(f"  [INSERT] 叫早 block ({removed_count} lines) after line {i + 1}")
                removed_count = 0
            i += 1
            continue

        new_lines.append(line)
        i += 1

    # If wakeup block wasn't inserted (no CASE "探索魔界" found), try inserting before CASEELSE/ENDSELECT
    if wakeup_block_lines:
        # Find the right spot in new_lines
        final_lines = []
        inserted = False
        for j, line in enumerate(new_lines):
            final_lines.append(line)
            # Insert after 调教's ENDSELECT (two tabs) and before the next ARGS:1 CASE or parent ENDSELECT
            if not inserted and re.match(r'^\t\tENDSELECT$', line):
                # Check next non-empty line
                next_idx = j + 1
                while next_idx < len(new_lines) and new_lines[next_idx].strip() == '':
                    next_idx += 1
                if next_idx < len(new_lines):
                    next_line = new_lines[next_idx]
                    stripped_next = next_line.lstrip('\t')
                    next_indent = len(next_line) - len(stripped_next)
                    # Insert if next line is at ARGS:1 level (1 tab) and not inside 调教
                    if next_indent <= 1 and (stripped_next.startswith('CASE') or stripped_next.startswith('ENDSELECT')):
                        final_lines.extend(wakeup_block_lines)
                        inserted = True
                        print(f"  [INSERT-FALLBACK] 叫早 block after ENDSELECT at line {j + 1}")
        if not inserted:
            final_lines.extend(wakeup_block_lines)
            print(f"  [INSERT-END] 叫早 block appended at end")
        new_lines = final_lines

    result = '\n'.join(new_lines)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)

    return True

def fix_renqi(filepath):
    """Special fix for 人妻口上1.ERB - 叫早 was deleted entirely, need to re-insert."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    wakeup_block = """	CASE "叫早"
		SELECTCASE ARGS:2
		CASE "开始"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「早上好……让妾身用嘴……帮你醒一醒……♥」"
				CALL MESSAGE_BOX,@"「（轻轻含入，抬眼望着你）……别急……今天一整天，妾身都会陪着你……♥」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……要这样叫早是吗……好……我照做……（迟疑地张开了嘴）……」"
			ELSE
				CALL MESSAGE_BOX,@"「……早上就要……？别这样……我丈夫他……唔……（被按住头，眼眶红了）……」"
			ENDIF
		CASE "射精"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……唔……要出来了吗……没事，全都交给妾身……♥」"
				CALL MESSAGE_BOX,@"「咽下去也好，吐出来也好……都依你……♥」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……要射了吗……那……请快一些……」"
			ELSE
				CALL MESSAGE_BOX,@"「……不……不要在我嘴里……求你了……」"
			ENDIF
		CASE "继续"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……嗯……嚅……（轻轻舔净）……早上的你，比白天味道更浓呢……♥」"
				CALL MESSAGE_BOX,@"「……还卧着别动，妾身去准备早食……想吃什么？」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……结束了……？（擦了擦嘴角）……我去收拾……」"
			ELSE
				CALL MESSAGE_BOX,@"「……咳……哈……这样的早晨……我会记住的……总有一天……」"
			ENDIF
		CASE "结束"
			IF CFLAG:乳牛 || CFLAG:洗脑 || ＃陷落状态／恋慕以上＃
				CALL MESSAGE_BOX,@"「……咦，不射吗……？也好，妾身只是想让你醒得舒服点……」"
				CALL MESSAGE_BOX,@"「那妾身去备早点。想吃甜的还是咸的？」"
			ELSEIF ＃陷落状态／屈服以上＃
				CALL MESSAGE_BOX,@"「……不做了吗……那我去忙了……（松了口气，匆匆离开）……」"
			ELSE
				CALL MESSAGE_BOX,@"「……结束了吗……谢天谢地……（低着头快步离开）……」"
			ENDIF
		ENDSELECT"""

    # Insert after 调教's ENDSELECT, before CASE "探索魔界"
    old = '\t\tENDSELECT\n\tCASE "探索魔界"'
    new = '\t\tENDSELECT\n' + wakeup_block + '\n\tCASE "探索魔界"'

    if old not in content:
        print(f"  ERROR: Could not find insertion point in 人妻口上1.ERB")
        return False

    content = content.replace(old, new, 1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [FIXED] 人妻口上1.ERB - 叫早 block re-inserted")
    return True

def main():
    # Fix 人妻 first (special case - block was deleted)
    renqi_path = os.path.join(BASE, "人妻口上1.ERB")
    if os.path.exists(renqi_path):
        fix_renqi(renqi_path)

    # Fix remaining 12 files
    for filename in FILES:
        filepath = os.path.join(BASE, filename)
        if not os.path.exists(filepath):
            print(f"  SKIP: {filename} not found")
            continue
        print(f"Processing: {filename}")
        fix_file(filepath)

    print("\nDone! Verify with: grep -n -B2 'CASE \"叫早\"' *.ERB")

if __name__ == "__main__":
    main()
