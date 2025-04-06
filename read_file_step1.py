# Solution: Read fixed file
def main():
    with open("sample.txt", "r") as infile:
        data = infile.read()
    print(data)

main()
