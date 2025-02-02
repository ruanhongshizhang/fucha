import os
import subprocess

# 设置 MkDocs 项目的路径（假设脚本与项目在同一目录下）
project_dir = os.path.dirname(os.path.abspath(__file__))

# 切换到项目目录
os.chdir(project_dir)

# 运行 mkdocs build 命令
try:
    subprocess.run(['mkdocs', 'build'], check=True)
    print("MkDocs build completed successfully!")
except subprocess.CalledProcessError:
    print("Error: MkDocs build failed.")
