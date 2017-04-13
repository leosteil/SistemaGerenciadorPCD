import tkinter as tk
#from tkFileDialog import askopenfilename   
from tkinter import filedialog
from tkinter import *
from Classe import Classe
import csv, sqlite3

class ExportData:
	def __init__(self, master):
		self.master = master

		self.container1 = tk.Frame(self.master, padx = 30, pady = 10)
		self.lblMsg = tk.Label(self.container1, text = "Você deseja exportar/importar os dados para/de um CSV?", fg = "black", font = "Verdana 10 bold")
		self.container1.pack()
		self.lblMsg.pack()

		self.container2 = tk.Frame(self.master)
		self.btnExport = tk.Button(self.container2, text = "Exportar", command = self.export)
		self.entryCsvName = tk.Entry(self.container2)
		self.btnImport = tk.Button(self.container2, text = "Importar", command = self.importar(self.entryCsvName.get()))
		self.lblDigiteNome = tk.Label(self.container2, text = "Nome do arquivo a ser importado")
		self.container2.pack()
		self.btnExport.pack()
		self.btnImport.pack()
		self.lblDigiteNome.pack(side = LEFT)
		self.entryCsvName.pack()



	def export(self):
		c = Classe()
		
		j = 0
		lista= []
		lista = c.buscaTodasClasses()

		#f = open("teste.csv", "r")

		conteudo = []
		conteudo.append("codigo,nome,subordinação,regAbertura,regDesativação,reativação,regMudançaNome,regDeslocamento,regExtinção,regIndicador, nivel\n")

		while j < len(lista):
		   l = lista[j]
		   conteudo.append(l.classe_codigo+ ", " + l.classe_nome + ", " +  l.classe_subordinacao + ", " + l.classe_regAbertura + ", " + l.classe_regDesativacao+ ", " + l.classe_reativacao + ", " + l.classe_regMudancaNome + ", " + l.classe_regDeslocamento + ", " + l.classe_regExtincao + ", " + l.classe_indicador + ", " + str(l.classe_nivel) + ", " + "\n")
		   j = j + 1 

		c = open("teste.csv", "w")

		c.writelines(conteudo)
		c.close()


	def importar(self, csvName):
		banco = Banco()

		with open("csvName") as f:

		con = banco.conexao.cursor()

