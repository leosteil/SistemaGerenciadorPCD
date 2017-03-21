import tkinter as tk
from AddClassFrame import AddClass

class MainView:
    def __init__(self, master):
        self.master = master

        self.container1 = tk.Frame(self.master)
        self.button1 = tk.Button(self.container1, text = 'Adicionar nova classe', width = 50, command = self.open_addClassFrame)
        self.button1.pack()
        self.container1.pack()

        self.container1 = tk.Frame(self.master)
        self.button1 = tk.Button(self.container1, text = 'Remover Classe', width = 50, command = self.open_addClassFrame)
        self.button1.pack()
        self.container1.pack()


        self.container1 = tk.Frame(self.master)
        self.button2 = tk.Button(self.container1, text = "Importar", width = 50, command = self.open_addClassFrame)
        self.button2.pack()
        self.container1.pack()

    def open_addClassFrame(self):   
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddClass(self.newWindow)


root = tk.Tk()
MainView(root)
root.mainloop()