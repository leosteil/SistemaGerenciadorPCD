import tkinter as tk
from tkinter import *
from ShowClassesFrame import ShowClasses
from ShowDocumentosFrame import ShowDocumentos
from ExportImportClassFrame import ExportData
from AddClassDocFrame import AddFrame

class MainView:
    def __init__(self, master):
        self.master = master

        self.container1 = tk.Frame(self.master)
        self.button1 = tk.Button(self.container1, text = 'Adicionar Classe/Documento', width = 50, command = self.open_classDocFrame)
        self.button1.pack()
        self.container1.pack()

        self.container2 = tk.Frame(self.master)
        self.button2 = tk.Button(self.container2, text = 'Remover Classe', width = 50, command = self.open_classDocFrame)
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
        
        self.container5 = tk.Frame(self.master)
        self.button5 = tk.Button(self.container5, text = "Mostrar Documentos", width = 50, command = self.open_showDocumentosFrame)
        self.button5.pack()
        self.container5.pack()


    def open_classDocFrame(self):   
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddFrame(self.newWindow)
    
    def open_showDocumentosFrame(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ShowDocumentos(self.newWindow)

    def open_showClassesFrame(self):   
        self.newWindow = tk.Toplevel(self.master)
        self.app = ShowClasses(self.newWindow)
    
    def open_exportClass(self):   
        self.newWindow = tk.Toplevel(self.master)
        self.app = ExportData(self.newWindow)


root = tk.Tk()
root.title("Sistema de Gerenciamento de PCD")
MainView(root)
root.mainloop()
