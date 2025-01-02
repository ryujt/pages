import os
import re
from urllib.parse import quote

folder_order = ["Software Engineering", "인공지능", "Projects", "Programming", "etc"]
ignored_folders = ["resource"]

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def get_subdirectories(path):
    # 무시할 폴더를 제외하고 폴더 리스트를 반환
    return [
        d for d in os.listdir(path)
        if os.path.isdir(os.path.join(path, d)) and d not in ignored_folders
    ]

def generate_index(path, indent=0):
    items = []
    dirs = sorted(get_subdirectories(path), key=natural_sort_key)
    readme_path = os.path.join(path, "README.md")
    basename = os.path.basename(path)
    rel_path = os.path.relpath(path, start_path)
    encoded_path = "/".join(quote(part) for part in rel_path.split(os.sep))
    
    # 현재 폴더 내부에 README.md만 있고, 다른 서브 폴더가 없다면 => 한 줄 링크로 처리
    if os.path.exists(readme_path) and not dirs:
        items.append((
            " " * indent + f"* [{basename}](./{encoded_path}/README.md)",
            basename
        ))
        return items
    
    # 그 외의 경우 (하위 폴더가 있거나, README.md가 없는 경우)
    # 폴더 이름만 표시 (추후 하위 구조 출력)
    # README.md가 있으면 같이 출력
    if os.path.exists(readme_path):
        # 폴더 제목
        items.append((
            " " * indent + f"* {basename}",
            basename
        ))
        # README 링크
        sub_indent = indent + 2
        items.append((
            " " * sub_indent + f"* [README](./{encoded_path}/README.md)",
            "README"
        ))
    else:
        # README.md 없으면 그냥 폴더 이름만 표시
        items.append((
            " " * indent + f"* {basename}",
            basename
        ))
        sub_indent = indent + 2
    
    # 하위 폴더 처리
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
