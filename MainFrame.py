import tkinter as tk
from tkinter import *
from AddClassFrame import AddClass
from ShowClassesFrame import ShowClasses
from ExportClassFrame import ExportData

class MainView:
    def __init__(self, master):
        self.master = master

        self.container0 = tk.Frame(self.master)
        self.lblNomeBanco = tk.Label(self.container0, width = 20, text = "Digite o nome do banco")
        self.entryNomeBanco = tk.Entry(self.container0)
        self.container0.pack()
        self.lblNomeBanco.pack(side = LEFT)
        self.entryNomeBanco.pack()

        self.container1 = tk.Frame(self.master)
        self.button1 = tk.Button(self.container1, text = 'Adicionar nova classe', width = 50, command = self.open_addClassFrame)
        self.button1.pack()
        self.container1.pack()

        self.container2 = tk.Frame(self.master)
        self.button2 = tk.Button(self.container2, text = 'Remover Classe', width = 50, command = self.open_addClassFrame)
        self.button2.pack()
        self.container2.pack()


        self.container3 = tk.Frame(self.master)
        self.button3 = tk.Button(self.container3, text = "Exportar/Importar Dados de CSV", width = 50, command = self.open_exportClass)
        self.button3.pack()
        self.container3.pack()

        self.container4 = tk.Frame(self.master)
        self.button4 = tk.Button(self.container4, text = "Mostrar Classes", width = 50, command = self.open_showClassesFrame)
        self.button4.pack()
        self.container4.pack()


    def open_addClassFrame(self):   
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddClass(self.newWindow)

    def open_showClassesFrame(self):   
        self.newWindow = tk.Toplevel(self.master)
        self.app = ShowClasses(self.newWindow)

    def open_exportClass(self):   
        self.newWindow = tk.Toplevel(self.master)
        self.app = ExportData(self.newWindow)


root = tk.Tk()
MainView(root)
root.mainloop()