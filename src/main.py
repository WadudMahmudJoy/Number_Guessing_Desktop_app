from gui import NumberGuessingApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()