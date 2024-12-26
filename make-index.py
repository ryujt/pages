import os
from urllib.parse import quote

folder_order = ["Software Engineering", "인공지능", "Projects", "Programming", "etc"]
ignored_folders = ["resource"]  # Add resource folder to ignored list

def get_sorted_dirs(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d not in ignored_folders]
    return sorted(dirs, key=lambda x: folder_order.index(x) if x in folder_order else -1)

def generate_index(path, indent=0):
    content = []
    dirs = get_sorted_dirs(path)
    
    for dir in dirs:
        dir_path = os.path.join(path, dir)
        rel_path = os.path.relpath(dir_path, start_path)
        
        if dir == "etc":
            continue
        
        subdirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d)) and d not in ignored_folders]
        
        if not subdirs:
            readme_path = os.path.join(dir_path, "README.md")
            if os.path.exists(readme_path):
                encoded_path = "/".join(quote(part) for part in rel_path.split("\\"))
                content.append(f"{'  ' * indent}* [{os.path.basename(dir_path)}](./{encoded_path}/README.md)")
            else:
                content.append(f"{'  ' * indent}* {dir}")
        else:
            content.append(f"{'  ' * indent}* {dir}")
            subcontents = generate_index(dir_path, indent + 1)
            if subcontents:
                content.extend(subcontents)
            else:
                # If there are no subcontents, check for README.md in the current directory
                readme_path = os.path.join(dir_path, "README.md")
                if os.path.exists(readme_path):
                    encoded_path = "/".join(quote(part) for part in rel_path.split("\\"))
                    readme_content = open(readme_path, 'r', encoding='utf-8').read()
                    first_heading = readme_content.split('\n', 1)[0].strip('# ')
                    content.append(f"{'  ' * (indent+1)}* [{first_heading}](./{encoded_path}/README.md)")
    
    return content

start_path = "./"
os.chdir(start_path)

index_content = ["# 목차\n"]

for main_dir in folder_order:
    if os.path.exists(main_dir) and os.path.isdir(main_dir):
        index_content.append(f"\n## {main_dir}\n")
        index_content.extend(generate_index(main_dir))

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(index_content))

print("Index generated successfully.")