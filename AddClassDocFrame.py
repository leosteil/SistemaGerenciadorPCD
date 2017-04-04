"""Este frame será utilizado para redirecionar para a criação de classes e documentos"""

import tkinter as tk
from tkinter import *
from AddClassFrame import AddClass
from AddDocFrame import AddDoc

class AddFrame:
	def __init__(self, master):
		self.master = master

		self.container1 = tk.Frame(self.master, padx = 30, pady = 10)
		self.lblMsg = tk.Label(self.container1, text = "O que você deseja adicionar?", fg = "black", font = "Verdana 10 bold")
		self.container1.pack()
		self.lblMsg.pack()

		self.container2 = tk.Frame(self.master)
		self.btnExport = tk.Button(self.container2, text = "Classe", width = 20, command = self.open_AddClass)
		self.btnImport = tk.Button(self.container2, text = "Documento", width = 20)
		self.container2.pack()
		self.btnExport.pack()
		self.btnImport.pack()


	def open_AddClass(self):
		self.newWindow = tk.Toplevel(self.master)  
		self.app = AddClass(self.newWindow)