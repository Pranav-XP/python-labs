# Solution: Demonstrate relative and absolute paths
from pathlib import Path

def main():
    path = Path("sample.txt")
    print("Relative path:", path)
    print("Absolute path:", path.resolve())

    parent_path = Path("..")
    print("Parent directory path:", parent_path.resolve())

main()
