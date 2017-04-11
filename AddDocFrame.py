import tkinter as tk
from tkinter import *
from tkinter import ttk
from Documento import Documento
from Classe import Classe


class AddDoc:
	def __init__(self, master):
		self.master = master
		j = 0
		
		self.container1 = tk.Frame(self.master, pady = 10)
		self.lblCabecalho = tk.Label(self.container1, text = "Digite os dados abaixo", fg = "black", font = "Verdana 10 bold")
		self.lblCabecalho.pack()
		self.container1.pack()
		
		self.container2 = tk.Frame(self.master, pady = 5, padx = 80)
		self.lblNome = tk.Label(self.container2, text = "Nome:", width = 25)
		self.entryNome = tk.Entry(self.container2)
		self.container2.pack()
		self.lblNome.pack(side=LEFT)
		self.entryNome.pack()
		
		self.container3 = tk.Frame(self.master, pady = 5, padx = 80)
		self.lblCodigo = tk.Label(self.container3, text = "Código:", width = 25)
		self.entryCodigo = tk.Entry(self.container3)
		self.container3.pack()
		self.lblCodigo.pack(side=LEFT)
		self.entryCodigo.pack()


		self.container11 = tk.Frame(self.master, pady = 5, padx = 80)
		self.lblFiliacao = tk.Label(self.container11, text = "Filiação:", width = 25)
		filiacao = Classe.buscaTodasClasses(self) #para preencher combobox com todas as classes

		filiacao2 = []

		while j < len(filiacao):
			filiacao2.append(filiacao[j].classe_codigo + ", " +filiacao[j].classe_nome)
			j = j + 1
			print(filiacao2)

		self.comboFiliacao = ttk.Combobox(self.container11, value = filiacao2, width = 10)
		self.container11.pack()
		self.lblFiliacao.pack(side=LEFT)
		self.comboFiliacao.pack()


		self.container4 = tk.Frame(self.master, pady = 5, padx = 80)
		self.lblg_fase_corrente = tk.Label(self.container4, text = "Prazo de Guarda na Fase Corrente:", width = 30)
		self.entryG_fase_corrente = tk.Entry(self.container4)
		self.container4.pack()
		self.lblg_fase_corrente.pack(side=LEFT)
		self.entryG_fase_corrente.pack()
		
		self.container5 = tk.Frame(self.master, pady = 5, padx = 80)
		self.lblg_fase_intermediaria = tk.Label(self.container5, text = "Prazo de Guarda na Fase Intermediária:", width = 30)
		self.entryG_fase_intermediaria = tk.Entry(self.container5)
		self.container5.pack()
		self.lblg_fase_intermediaria.pack(side=LEFT)
		self.entryG_fase_intermediaria.pack()
		
		self.container6 = tk.Frame(self.master, pady = 5, padx = 80)
		self.lbldestfinal = tk.Label(self.container6, text = "Destinação Final:", width = 25)
		destino = ("Preservação","Eliminação")
		self.comboDestino = ttk.Combobox(self.container6, value = destino, width = 10)
		self.container6.pack()
		self.lbldestfinal.pack(side=LEFT)
		self.comboDestino.pack()
		
		self.container7 = tk.Frame(self.master, pady = 5, padx = 80)
		self.lblreg_alteracao = tk.Label(self.container7, text = "Registro de Alteração:", width = 25)
		self.entryReg_alteracao = tk.Entry(self.container7)
		self.container7.pack()
		self.lblreg_alteracao.pack(side=LEFT)
		self.entryReg_alteracao.pack()
		
		self.container8 = tk.Frame(self.master, pady = 5, padx = 80)
		self.lblobs = tk.Label(self.container8, text = "Observações:", width = 25)
		self.entryObs = tk.Entry(self.container8)
		self.container8.pack()
		self.lblobs.pack(side=LEFT)
		self.entryObs.pack()
		
		self.container9 = tk.Frame(self.master, pady = 4, padx = 80)
		self.btnSubmeter = tk.Button(self.container9, text = "Submmit", width = 12, command = self.submmit)
		self.btnSubmeter.pack(side = LEFT)
		self.container9.pack(side = RIGHT)
		
		self.container10 = tk.Frame(self.master, pady = 4, padx = 80)
		self.lblmsg = tk.Label(self.container10, text="")
		self.lblmsg["font"] = ("Verdana", "9", "italic")
		self.lblmsg.pack()
		self.container10.pack()
		
	def submmit(self):
		d = Documento()
		
		d.documento_nome = self.entryNome.get()
		d.documento_codigo = self.entryCodigo.get()
		d.doc_guarda_fase_corrente = self.entryG_fase_corrente.get()
		d.doc_guarda_fase_intermediaria = self.entryG_fase_intermediaria.get()
		d.dest_final = self.comboDestino.get()
		d.reg_alteracao = self.entryReg_alteracao.get()
		d.obs = self.entryObs.get()
		self.lblmsg["text"] = d.insertDocumento()
