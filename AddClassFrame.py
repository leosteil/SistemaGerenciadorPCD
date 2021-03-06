import tkinter as tk
from tkinter import *
from tkinter import ttk
from Classe import Classe
from datetime import date

class AddClass:
    def __init__(self, master):
        self.master = master

        j = 0

        self.container1 = tk.Frame(self.master, pady = 10)
        self.lblCabecalho = tk.Label(self.container1, text = "Digite os dados abaixo", fg = "black", font = "Verdana 10 bold")
        self.lblCabecalho.pack()
        self.container1.pack()

        self.container2 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblNome = tk.Label(self.container2, text = "Nome:", width = 25)
        self.entryNome = tk.Entry(self.container2)
        self.container2.pack()
        self.lblNome.pack(side=LEFT)
        self.entryNome.pack()

        self.container14 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblNivel = tk.Label(self.container14, text = "Nivel da Classe:", width = 25)
        
        valor = (1,2,3,4)
        self.comboNivel = ttk.Combobox(self.container14, value = valor, width = 3)

        self.container14.pack()
        self.lblNivel.pack(side=LEFT)
        self.comboNivel.pack()

        self.container3 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblCodigo = tk.Label(self.container3, text = "Código:", width = 25)
        self.entryCodigo = tk.Entry(self.container3)
        self.container3.pack()
        self.lblCodigo.pack(side=LEFT)
        self.entryCodigo.pack()

        self.container15 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblFiliacao = tk.Label(self.container15, text = "Filiação/Subordinação:", width = 25)
        filiacao = Classe.buscaTodasClasses(self)

        filiacao2 = []

        while j < len(filiacao):
        	filiacao2.append(filiacao[j].classe_codigo + ", " + filiacao[j].classe_nome)
        	j = j + 1

        filiacao2.sort()

        self.comboFiliacao = ttk.Combobox(self.container15, value = filiacao2, width = 25)
        self.container15.pack()
        self.lblFiliacao.pack(side=LEFT)
        self.comboFiliacao.pack()

        """self.container4 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblSubordinacao = tk.Label(self.container4, text = "Subordinação:", width = 25)
        self.entrySubordinacao = tk.Entry(self.container4)
        self.container4.pack()
        self.lblSubordinacao.pack(side=LEFT)
        self.entrySubordinacao.pack()"""

        self.container5 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblRegAbertura = tk.Label(self.container5, text = "Registro de abertura:", width = 25)
        self.entryRegAbertura = tk.Entry(self.container5)
        self.entryRegAbertura.insert(0, date.today())
        self.container5.pack()
        self.lblRegAbertura.pack(side=LEFT)
        self.entryRegAbertura.pack()


        """self.container6 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblRegDesativacao = tk.Label(self.container6, text = "Registro de desativação:", width = 25)
        self.entryRegDesativacao = tk.Entry(self.container6)
        self.container6.pack()
        self.lblRegDesativacao.pack(side=LEFT)
        self.entryRegDesativacao.pack()

        self.container7 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblRegAtivacao = tk.Label(self.container7, text = "Registro de ativação:", width = 25)
        self.entryRegAtivacao = tk.Entry(self.container7)
        self.container7.pack()
        self.lblRegAtivacao.pack(side=LEFT)
        self.entryRegAtivacao.pack()

        self.container8 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblRegMundancaNome = tk.Label(self.container8, text = "Registro de mudança de nome:", width = 25)
        self.entryRegMudancaNome = tk.Entry(self.container8)
        self.container8.pack()
        self.lblRegMundancaNome.pack(side=LEFT)
        self.entryRegMudancaNome.pack()

        self.container9 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblRegDeslocamento = tk.Label(self.container9, text = "Registro de deslocamento:", width = 25)
        self.entryRegDeslocamento = tk.Entry(self.container9)
        self.container9.pack()
        self.lblRegDeslocamento.pack(side=LEFT)
        self.entryRegDeslocamento.pack()

        self.container10 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblRegExtincao = tk.Label(self.container10, text = "Registro de extinção:", width = 25)
        self.entryRegExtincao = tk.Entry(self.container10)
        self.container10.pack()
        self.lblRegExtincao.pack(side=LEFT)
        self.entryRegExtincao.pack()

        self.container11 = tk.Frame(self.master, pady = 5, padx = 50)
        self.lblIndicador = tk.Label(self.container11, text = "Indicador da classe:", width = 25)
        self.entryIndicador = tk.Entry(self.container11)
        self.container11.pack()
        self.lblIndicador.pack(side=LEFT)
        self.entryIndicador.pack()"""

        self.container12 = tk.Frame(self.master, pady = 4, padx = 50)
        self.btnSubmeter = tk.Button(self.container12, text = "Submmit", width = 12, command = self.submmit)
        self.btnSubmeter.pack(side = LEFT)
        self.container12.pack(side = RIGHT)

        self.container13 = tk.Frame(self.master, pady = 4, padx = 50)
        self.lblmsg = tk.Label(self.container13, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
        self.container13.pack()

    def submmit(self):
       	c = Classe()
       	cAux = Classe()

       	c.classe_nome = self.entryNome.get()
       	c.classe_codigo = self.entryCodigo.get()
       	c.classe_regAbertura = self.entryRegAbertura.get()

       	stringAux = self.comboFiliacao.get()
       	x = stringAux.find(',')

       	cAux = cAux.buscaClasse(stringAux[:x])

        if(len(cAux.classe_codigo) > 0):
       	    c.id_classe_subordinacao = cAux.classe_codigo

       	print(c.id_classe_subordinacao + "TESTE2")

       	c.classe_nivel = self.comboNivel.get()

       	self.lblmsg["text"] = c.insertClasse()
