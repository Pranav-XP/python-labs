# Solution: Save file using dialog with user input
from tkinter.filedialog import asksaveasfilename
from tkinter import Tk

def main():
    root = Tk()
    root.withdraw()

    text = input("Enter the text to save in file: ")
    fname = asksaveasfilename(defaultextension=".txt")
    if fname:
        with open(fname, "w") as f:
            f.write(text)
        print(f"File saved as {fname}")
    else:
        print("No file saved.")

main()
