import tkinter as tk
#from tkFileDialog import askopenfilename   
from tkinter import filedialog
from tkinter import *
from Classe import Classe

class ExportData:
	def __init__(self, master):
		self.master = master

		self.container1 = tk.Frame(self.master, padx = 30, pady = 10)
		self.lblMsg = tk.Label(self.container1, text = "Você deseja exportar/importar os dados para/de um CSV?", fg = "black", font = "Verdana 10 bold")
		self.container1.pack()
		self.lblMsg.pack()

		self.container2 = tk.Frame(self.master)
		self.btnExport = tk.Button(self.container2, text = "Exportar", command = self.export)
		self.btnImport = tk.Button(self.container2, text = "Importar", command = self.importar)
		self.container2.pack()
		self.btnExport.pack()
		self.btnImport.pack()


	def export(self):
		c = Classe()
		
		j = 0
		lista= []
		lista = c.buscaTodasClasses(1)

		lista.sort()

		#f = open("teste.csv", "r")

		conteudo = []
		conteudo.append("codigo,nome,subordinação,regAbertura,regDesativação,reativação,regMudançaNome,regDeslocamento,regExtinção,regIndicador\n")

		while j < len(lista):
		   conteudo.append(lista[j] + "\n")
		   j = j + 1 

		c = open("teste.csv", "w")

		c.writelines(conteudo)
		c.close()


	def importar(self):
		pass