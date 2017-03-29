from tkinter import filedialog
import tkinter as tk

class ExportData:
    def __init__(self, master):
        self.master = master

        self.container1 = tk.Frame(self.master)

       	tkFileDialog.asksaveasfilename()