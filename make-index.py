import os
import re

folder_order = ["Software Engineering", "인공지능", "Projects", "Programming", "etc"]
ignored_folders = ["resource"]

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def encode_path_with_spaces(rel_path):
    # UTF-8로 인코딩한 후 %로 시작하는 시퀀스로 변환
    parts = rel_path.split(os.sep)
    encoded_parts = []
    for part in parts:
        # 각 문자를 UTF-8로 인코딩하고 퍼센트 인코딩으로 변환
        encoded = ''.join(['%' + '{:02X}'.format(b) for b in part.encode('utf-8')])
        encoded_parts.append(encoded)
    return '/'.join(encoded_parts)

def get_subdirectories(path):
    return [d for d in os.listdir(path)
            if os.path.isdir(os.path.join(path, d)) and d not in ignored_folders]

def generate_index(path, indent=0):
    items = []
    dirs = sorted(get_subdirectories(path), key=natural_sort_key)
    readme_path = os.path.join(path, "README.md")
    basename = os.path.basename(path)
    rel_path = os.path.relpath(path, start_path)
    encoded_path = encode_path_with_spaces(rel_path)
    
    # 1) README.md만 존재하고 하위 폴더가 전혀 없는 경우
    if os.path.exists(readme_path) and not dirs:
        items.append((
            " " * indent + f"* [{basename}](./{encoded_path}/README.md)",
            basename
        ))
        return items
    
    # 2) 그 외의 경우
    if os.path.exists(readme_path):
        items.append((
            " " * indent + f"* {basename}",
            basename
        ))
        sub_indent = indent + 2
        items.append((
            " " * sub_indent + f"* [README](./{encoded_path}/README.md)",
            "README"
        ))
    else:
        items.append((
            " " * indent + f"* {basename}",
            basename
        ))
        sub_indent = indent + 2
    
    for d in dirs:
        subpath = os.path.join(path, d)
        subitems = generate_index(subpath, sub_indent)
        items.extend(subitems)

    return items

start_path = "./"
os.chdir(start_path)

index_content = ["# 목차\n"]

for main_dir in folder_order:
    if os.path.isdir(main_dir):
        index_content.append(f"\n## {main_dir}\n")
        results = generate_index(main_dir, 0)
        for line, _ in results:
            index_content.append(line)

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(index_content))

print("Index generated successfully.")