# Solution: Write a fixed list to file
def main():
    lines = ["First line", "Second line", "Third line"]
    with open("output.txt", "w") as outfile:
        for line in lines:
            print(line, file=outfile)

main()
