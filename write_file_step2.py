# Solution: Write user input lines to file until 'done'
from datetime import datetime

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"user_output_{timestamp}.txt"
    with open(fname, "w") as f:
        while True:
            line = input("Enter a line (or 'done' to finish): ")
            if line.lower() == "done":
                break
            print(line, file=f)
    print(f"Content saved in {fname}")

main()
