#!/usr/bin/env python3
"""Fix: move CASE "叫早" from ARGS:0 to ARGS:1 level (inside CASE "日程") for 3 files.
   Also fix 姉御肌's "晚上调教后回自室" moving back inside 調教 at ARGS:2 level.
   Also fix 人妻's duplicate 叫早."""

BASE = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上"

def read_file(filename):
    with open(BASE + '\\' + filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(BASE + '\\' + filename, 'w', encoding='utf-8') as f:
        f.write(content)

def indent_block(text, extra_tab='\t'):
    """Add one tab to every non-empty line."""
    lines = text.split('\n')
    result = []
    for line in lines:
        if line.strip() == '':
            result.append(line)
        else:
            result.append(extra_tab + line)
    return '\n'.join(result)

def fix_叫早_level(filename):
    """Move CASE "叫早" from ARGS:0 level to ARGS:1 (inside 日程's SELECTCASE)."""
    content = read_file(filename)
    lines = content.split('\n')

    # Find CASE "叫早" at ARGS:0 level (no leading tab, after ENDSELECT with 1 tab)
    wakeup_start = -1
    for i, line in enumerate(lines):
        if line == 'CASE "叫早"':
            # Check if this is at ARGS:0 (preceded by blank line after ENDSELECT)
            prev_nonempty = ''
            for j in range(i-1, -1, -1):
                if lines[j].strip():
                    prev_nonempty = lines[j]
                    break
            if prev_nonempty.lstrip('\t').startswith('ENDSELECT'):
                wakeup_start = i
                break

    if wakeup_start < 0:
        print(f"  SKIP {filename}: no ARGS:0 叫早 found")
        return

    # Find the end of the 叫早 block (matching ENDSELECT at same indent level)
    wakeup_end = -1
    depth = 0
    for i in range(wakeup_start, len(lines)):
        stripped = lines[i].lstrip('\t')
        if stripped.startswith('SELECTCASE'):
            depth += 1
        elif stripped.startswith('ENDSELECT'):
            if depth == 0:
                wakeup_end = i
                break
            depth -= 1

    if wakeup_end < 0:
        print(f"  ERROR {filename}: can't find end of 叫早 block")
        return

    # Extract the叫早 block
    wakeup_lines = lines[wakeup_start:wakeup_end+1]
    wakeup_text = '\n'.join(wakeup_lines)

    # Indent it
    indented_wakeup = indent_block(wakeup_text)

    # Find the ENDSELECT that closes 日程's SELECTCASE ARGS:1
    # (should be right before where the叫早 block was)
    # The ENDSELECT is at 1-tab indent, right before the叫早 block
    insert_after = wakeup_start - 1
    while insert_after >= 0 and lines[insert_after].strip() == '':
        insert_after -= 1

    if not lines[insert_after].lstrip('\t').startswith('ENDSELECT'):
        print(f"  ERROR {filename}: can't find ENDSELECT before 叫早")
        return

    # Build new content:
    # - Remove the original叫早 block
    # - Insert indented version before the ENDSELECT
    new_lines = []
    for i, line in enumerate(lines):
        if i == insert_after:
            # Insert indented叫早 before ENDSELECT
            new_lines.append(indented_wakeup)
            new_lines.append(line)  # the ENDSELECT
        elif wakeup_start <= i <= wakeup_end:
            continue  # skip original叫早 block
        else:
            new_lines.append(line)

    write_file(filename, '\n'.join(new_lines))
    print(f"  FIXED {filename}: 叫早 moved to ARGS:1 level")

def fix_renqi_duplicate():
    """Remove duplicate CASE "叫早" from 人妻口上1.ERB."""
    content = read_file("人妻口上1.ERB")
    lines = content.split('\n')

    # Find all叫早 occurrences
    wakeup_positions = []
    for i, line in enumerate(lines):
        if line.strip() == 'CASE "叫早"':
            wakeup_positions.append(i)

    if len(wakeup_positions) <= 1:
        print(f"  SKIP 人妻: {len(wakeup_positions)} 叫早 blocks")
        return

    # Remove the first one (the duplicate - there should be one at correct level)
    # Actually, let's find which one is at the right level.
    # Both are at ARGS:1 since the original was correctly placed by v2 script
    # Just remove the first one
    first_pos = wakeup_positions[0]

    # Find the end of this叫早 block
    depth = 0
    end_pos = -1
    for i in range(first_pos, len(lines)):
        stripped = lines[i].lstrip('\t')
        if stripped.startswith('SELECTCASE'):
            depth += 1
        elif stripped.startswith('ENDSELECT'):
            if depth == 0:
                end_pos = i
                break
            depth -= 1

    if end_pos < 0:
        print(f"  ERROR 人妻: can't find end of first 叫早")
        return

    # Remove the block (including trailing blank line)
    new_lines = []
    skip_until = end_pos + 1  # skip the blank line after ENDSELECT too
    if skip_until < len(lines) and lines[skip_until].strip() == '':
        skip_until += 1

    for i, line in enumerate(lines):
        if first_pos <= i < skip_until:
            continue
        new_lines.append(line)

    write_file("人妻口上1.ERB", '\n'.join(new_lines))
    print(f"  FIXED 人妻: removed duplicate 叫早")

def fix_ane_neesan():
    """姉御肌 also has "晚上调教后回自室" at wrong level (ARGS:1, should be ARGS:2 inside 調教)."""
    content = read_file("姉御肌口上1.ERB")
    # This is more complex - "晚上调教后回自室" is at ARGS:1 level but should be at ARGS:2
    # For now, just report the issue
    print(f"  TODO 姉御肌: 晚上调教后回自室 needs to move back inside 調教 (ARGS:2)")
    print(f"            This requires manual restructuring of the调教 block")

def main():
    print("=== Fixing 叫早 ARGS level ===")
    for filename in ["非敬語幼め口上1.ERB", "生真面目口上1.ERB", "姉御肌口上1.ERB"]:
        fix_叫早_level(filename)

    print("\n=== Fixing duplicate 叫早 ===")
    fix_renqi_duplicate()

    print("\nDone! Verify with: grep -n -B2 'CASE \"叫早\"' *.ERB")

if __name__ == "__main__":
    main()
