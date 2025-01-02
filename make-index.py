import os
import re

# GitHub 사용자명/저장소명, 원하는 브랜치를 지정하세요.
# 예) 사용자명: ryujt, 저장소명: pages, 브랜치: main
GITHUB_USER = "ryujt"
GITHUB_REPO = "pages"
GITHUB_BRANCH = "main"

folder_order = ["Software Engineering", "인공지능", "Projects", "Programming", "etc"]
ignored_folders = ["resource"]

start_path = "./"
os.chdir(start_path)

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def encode_path_with_spaces(path):
    # 공백은 %20으로, 나머지는 그대로.
    # 경로 구분자는 / 로 통일 (Windows/Unix 차이 제거)
    return path.replace(" ", "%20").replace(os.sep, "/")

def make_github_link(is_file, rel_path):
    # 폴더면 tree, 파일이면 blob 링크를 만든다.
    base = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}"
    if is_file:
        return f"{base}/blob/{GITHUB_BRANCH}/{rel_path}"
    else:
        return f"{base}/tree/{GITHUB_BRANCH}/{rel_path}"

def get_subdirectories(path):
    # 무시 대상이 아닌 폴더만 가져오기
    return [
        d for d in os.listdir(path)
        if os.path.isdir(os.path.join(path, d)) and d not in ignored_folders
    ]

def generate_index(path, indent=0):
    items = []
    dirs = sorted(get_subdirectories(path), key=natural_sort_key)
    basename = os.path.basename(path)
    readme_path = os.path.join(path, "README.md")

    # GitHub 경로 만들기용 상대 경로
    rel_path_raw = os.path.relpath(path, start_path)  # 예: "Programming/React/..."
    rel_path_encoded = encode_path_with_spaces(rel_path_raw)

    # 현재 디렉토리에 README.md가 있는지 확인
    has_readme = os.path.exists(readme_path)

    # 1) "하위 폴더가 없고" + "README.md만 있다면" → 바로 파일 링크 (blob)
    #    (즉, 오직 하나의 README.md만 있을 때)
    if has_readme and not dirs:
        file_link = make_github_link(is_file=True, rel_path=f"{rel_path_encoded}/README.md")
        items.append((
            " " * indent + f"* [{basename}]({file_link})",
            basename
        ))
        return items
    
    # 2) 그 외 (하위 폴더가 있거나, README.md가 없거나, 여러 파일이 있을 때)
    #    → 폴더 링크 (tree) + (README.md 있으면 blob)
    folder_link = make_github_link(is_file=False, rel_path=rel_path_encoded)
    items.append((
        " " * indent + f"* [{basename}]({folder_link})",
        basename
    ))
    sub_indent = indent + 2

    # 만약 README.md가 있으면, 그 밑에 README 파일 링크를 걸어준다.
    if has_readme:
        file_link = make_github_link(is_file=True, rel_path=f"{rel_path_encoded}/README.md")
        items.append((
            " " * sub_indent + f"* [README]({file_link})",
            "README"
        ))

    # 하위 폴더 재귀 처리
    for d in dirs:
        sub_path = os.path.join(path, d)
        items.extend(generate_index(sub_path, sub_indent))
    return items

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
