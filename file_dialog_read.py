# Solution: Open file using dialog and print content
from tkinter.filedialog import askopenfilename
from tkinter import Tk

def main():
    root = Tk()
    root.withdraw()

    fname = askopenfilename(filetypes=[("Text files", "*.txt")])
    if fname:
        with open(fname, "r") as f:
            print(f.read())
    else:
        print("No file selected.")

main()
