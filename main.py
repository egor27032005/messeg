import tkinter as tk


from registr import Registration


if __name__ == "__main__":
    root = tk.Tk()
    app = Registration(root)
    root.mainloop()