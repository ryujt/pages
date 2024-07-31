import os
from urllib.parse import quote

# 폴더 순서 정의
folder_order = ["Software Engineering", "인공지능", "Projects", "Programming", "etc"]

# 제목 추출 함수
def extract_title_from_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith("# "):
                return line[2:].strip()
    return os.path.basename(os.path.dirname(filepath))

# URL 안전 경로 생성 함수
def create_safe_path(path):
    return '/'.join(quote(part) for part in path.split('/'))

# README.md 생성 함수
def generate_readme(root_dir):
    document = "# 목차\n\n"

    for folder in folder_order:
        folder_path = os.path.join(root_dir, folder)
        if os.path.exists(folder_path):
            document += f"## {folder}\n"

            titles_and_paths = []
            for subdir, _, files in os.walk(folder_path):
                if "README.md" in files:
                    title = extract_title_from_md(os.path.join(subdir, "README.md"))
                    if title:
                        relative_path = os.path.relpath(subdir, root_dir).replace("\\", "/")
                        titles_and_paths.append((title, relative_path))

            titles_and_paths.sort(key=lambda x: x[1])  # 상대 경로로 정렬

            for title, relative_path in titles_and_paths:
                safe_path = create_safe_path(relative_path)
                document += f" * [{title}](./{safe_path}/README.md)\n"
            document += "\n"

    with open(os.path.join(root_dir, "README.md"), 'w', encoding='utf-8') as file:
        file.write(document)

# 실행
generate_readme("D:/Projects/Personal/pages")  # 지정된 디렉토리를 기준으로 실행