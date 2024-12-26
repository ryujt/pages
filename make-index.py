import os
from urllib.parse import quote
import re

folder_order = ["Software Engineering", "인공지능", "Projects", "Programming", "etc"]
ignored_folders = ["resource"]

def natural_sort_key(s):
    """숫자가 포함된 문자열의 자연스러운 정렬을 위한 키 함수"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def get_sorted_dirs(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d not in ignored_folders]
    return sorted(dirs, key=lambda x: folder_order.index(x) if x in folder_order else float('inf'))

def generate_index(path, indent=0):
    content = []
    dirs = get_sorted_dirs(path)
    current_group = None
    group_items = []
    
    for dir in dirs:
        dir_path = os.path.join(path, dir)
        rel_path = os.path.relpath(dir_path, start_path)
        
        if dir == "etc":
            continue
        
        subdirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d)) and d not in ignored_folders]
        
        # 숫자로 시작하는 항목 체크
        is_numbered = bool(re.match(r'^\d+\.', dir))
        
        if is_numbered and current_group is None:
            # 새로운 그룹의 시작을 찾음
            parent_dir = os.path.basename(os.path.dirname(dir_path))
            if parent_dir not in folder_order:  # 메인 카테고리가 아닐 경우에만 그룹 추가
                current_group = parent_dir
                content.append((f"{'  ' * indent}* {current_group}", current_group))
                indent += 1

        if is_numbered:
            # 번호가 매겨진 항목은 현재 그룹에 추가
            readme_path = os.path.join(dir_path, "README.md")
            if os.path.exists(readme_path):
                encoded_path = "/".join(quote(part) for part in rel_path.split("\\"))
                group_items.append((f"{'  ' * indent}* [{dir}](./{encoded_path}/README.md)", dir))
        else:
            # 이전 그룹의 아이템들을 정렬하여 추가
            if group_items:
                content.extend(sorted(group_items, key=lambda x: natural_sort_key(x[1])))
                group_items = []
                indent -= 1
                current_group = None

            # 일반 디렉토리 처리
            if not subdirs:
                readme_path = os.path.join(dir_path, "README.md")
                if os.path.exists(readme_path):
                    encoded_path = "/".join(quote(part) for part in rel_path.split("\\"))
                    content.append((f"{'  ' * indent}* [{dir}](./{encoded_path}/README.md)", dir))
            else:
                has_numbered_children = any(bool(re.match(r'^\d+\.', d)) for d in subdirs)
                if has_numbered_children:
                    content.append((f"{'  ' * indent}* {dir}", dir))
                    subcontents = generate_index(dir_path, indent + 1)
                    if subcontents:
                        # 마지막 항목(중복된 디렉토리 이름) 제거
                        filtered_subcontents = [item for item in subcontents if item[1] != dir]
                        content.extend(sorted(filtered_subcontents, key=lambda x: natural_sort_key(x[1])))
                else:
                    content.append((f"{'  ' * indent}* {dir}", dir))
                    subcontents = generate_index(dir_path, indent + 1)
                    if subcontents:
                        content.extend(sorted(subcontents, key=lambda x: natural_sort_key(x[1])))

    # 마지막 그룹의 아이템들 처리
    if group_items:
        content.extend(sorted(group_items, key=lambda x: natural_sort_key(x[1])))

    return content

start_path = "./"
os.chdir(start_path)

index_content = ["# 목차\n"]

for main_dir in folder_order:
    if os.path.exists(main_dir) and os.path.isdir(main_dir):
        index_content.append(f"\n## {main_dir}\n")
        sorted_items = generate_index(main_dir)
        index_content.extend(item[0] for item in sorted_items)

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(index_content))

print("Index generated successfully.")