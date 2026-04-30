#!/usr/bin/env python3
"""Fix 姉御肌口上1.ERB: move 叫早 and 晚上调教后回自室 from CASE "访问" back to CASE "日程"."""

BASE = r"C:\Cursor local\era-makai-ranch\ERB\○口上\汎用口上"
FILENAME = "姉御肌口上1.ERB"

def read_file():
    with open(BASE + '\' + FILENAME, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(content):
    with open(BASE + '\' + FILENAME, 'w', encoding='utf-8') as f:
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

def find_block_range(lines, keyword, start_search=0):
    """Find a CASE block by keyword, return (start_line, end_line) inclusive.
    end_line is the line where the block ends (ENDSELECT or ENDIF closure)."""
    for i in range(start_search, len(lines)):
        stripped = lines[i].strip()
        if stripped == f'CASE "{keyword}"':
            # Find the matching ENDSELECT or ENDIF
            start = i
            depth = 0
            end = -1
            for j in range(i, len(lines)):
                s = lines[j].lstrip('\t')
                if s.startswith('SELECTCASE') or s.startswith('IF ') and 'ELSE' not in s:
                    if not s.startswith('ELSEIF'):
                        depth += 1
                elif s.startswith('ENDSELECT') or s.startswith('ENDIF'):
                    if depth == 0:
                        end = j
                        break
                    depth -= 1
            if end >= 0:
                return (start, end)
    return None

def main():
    content = read_file()
    lines = content.split('\n')

    # 1. Find and extract the two blocks from CASE "访问"
    wakeup_range = find_block_range(lines, "叫早")
    bedtime_range = find_block_range(lines, "晚上调教后回自室")

    if not wakeup_range:
        print("ERROR: 叫早 block not found")
        return
    if not bedtime_range:
        print("ERROR: 晚上调教后回自室 block not found")
        return

    print(f"叫早: lines {wakeup_range[0]+1}-{wakeup_range[1]+1}")
    print(f"晚上调教后回自室: lines {bedtime_range[0]+1}-{bedtime_range[1]+1}")

    # Extract block contents (excluding trailing blank after ENDIF if any)
    wakeup_lines = lines[wakeup_range[0]:wakeup_range[1]+1]
    bedtime_lines = lines[bedtime_range[0]:bedtime_range[1]+1]

    # Remove trailing blank line after wakeup block if present
    wakeup_end_idx = wakeup_range[1]
    if wakeup_end_idx + 1 < len(lines) and lines[wakeup_end_idx + 1].strip() == '':
        wakeup_end_idx += 1

    # For the bedtime block, check trailing blanks too
    # But we need to be careful - remove both blocks together
    bedtime_end_idx = bedtime_range[1]
    if bedtime_end_idx + 1 < len(lines) and lines[bedtime_end_idx + 1].strip() == '':
        bedtime_end_idx += 1

    # 2. Build new file content removing both blocks
    # We need to handle overlap (bedtime first, then wakeup after)
    if bedtime_range[0] < wakeup_range[0]:
        # bedtime comes first, remove both
        new_lines = []
        i = 0
        while i < len(lines):
            if bedtime_range[0] <= i <= bedtime_end_idx:
                i = bedtime_end_idx + 1
                continue
            if wakeup_range[0] <= i <= wakeup_end_idx:
                i = wakeup_end_idx + 1
                continue
            new_lines.append(lines[i])
            i += 1
    else:
        new_lines = []
        i = 0
        while i < len(lines):
            if wakeup_range[0] <= i <= wakeup_end_idx:
                i = wakeup_end_idx + 1
                continue
            if bedtime_range[0] <= i <= bedtime_end_idx:
                i = bedtime_end_idx + 1
                continue
            new_lines.append(lines[i])
            i += 1

    # 3. Find insertion points in CASE "日程"
    # Target 1: ENDSELECT at line ~964 (closes CASE "调教" SELECTCASE ARGS:2)
    # Insert 晚上调教后回自室 BEFORE this ENDSELECT
    # Target 2: ENDSELECT at line ~966 (closes CASE "日程" SELECTCASE ARGS:1)
    # Insert 叫早 BEFORE this ENDSELECT

    # Recalculate line numbers after removal
    wakeup_text = '\n'.join(wakeup_lines)
    bedtime_text = '\n'.join(bedtime_lines)

    # Indent bedtime_text by one tab (it needs to go from ARGS:1 to ARGS:2)
    bedtime_indented = indent_block(bedtime_text)

    # Find the insertion points in new_lines
    # Pattern: \t\tENDSELECT (close of 调教 SELECTCASE ARGS:2) followed by \tENDSELECT (close of 日程 SELECTCASE ARGS:1)
    insert_1 = None  # before the inner ENDSELECT (for bedtime)
    insert_2 = None  # before the outer ENDSELECT (for wakeup)

    for i, line in enumerate(new_lines):
        stripped = line.strip()
        if stripped == 'ENDSELECT':
            indent = line.count('\t')
            if indent == 2:
                # Check context: this should be the one closing CASE "调教" SELECTCASE ARGS:2
                # Verify by checking the line before it is also ENDSELECT at 1 tab or similar
                # Actually, let's look for the pattern: 2-tab ENDSELECT followed soon by 1-tab ENDSELECT
                # after some content that's part of 日程
                # The 调教 ENDSELECT at line 964 (original)
                # The 日程 ENDSELECT at line 966 (original)
                # After removals, they might be consecutive or separated by blank lines
                # Let's find them by looking for this pattern near where 日程 is

                # Check if this is inside 日程's structure
                # Look backward for CASE "日程"
                for j in range(i, -1, -1):
                    if new_lines[j].strip() == 'CASE "日程"':
                        insert_1 = i  # the 2-tab ENDSELECT closing 调教
                        # Now find the 1-tab ENDSELECT closing 日程
                        for k in range(i+1, len(new_lines)):
                            if new_lines[k].strip() == 'ENDSELECT' and new_lines[k].count('\t') == 1:
                                insert_2 = k
                                break
                        break
                if insert_1 is not None:
                    break

    if insert_1 is None or insert_2 is None:
        print("ERROR: Could not find insertion points")
        print(f"insert_1={insert_1}, insert_2={insert_2}")
        return

    print(f"Insert 晚上调教后回自室 before line {insert_1+1} (ENDSELECT at 2 tabs)")
    print(f"Insert 叫早 before line {insert_2+1} (ENDSELECT at 1 tab)")

    # 4. Build final output
    final_lines = []
    for i, line in enumerate(new_lines):
        if i == insert_1:
            # Insert bedtime_indented BEFORE this ENDSELECT
            final_lines.append(bedtime_indented)
            final_lines.append(line)
        elif i == insert_2:
            # Insert wakeup_text BEFORE this ENDSELECT
            final_lines.append(wakeup_text)
            final_lines.append(line)
        else:
            final_lines.append(line)

    write_file('\n'.join(final_lines))
    print("\nDONE! Verify with:")
    print('  grep -n -B3 "CASE.*叫早\|CASE.*晚上调教后回自室" ' + FILENAME)

if __name__ == "__main__":
    main()
