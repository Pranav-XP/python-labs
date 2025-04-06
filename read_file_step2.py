# Solution: Read user input file with error handling and line count
def main():
    try:
        fname = input("Enter the filename: ")
        with open(fname, "r") as infile:
            lines = infile.readlines()
            print("".join(lines))
            print(f"Total lines: {len(lines)}")
    except FileNotFoundError:
        print("File not found. Please check the name and try again.")

main()
