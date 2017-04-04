import tkinter as tk
from tkinter import *
from Documento import Documento

class ShowDocumentos:
    def __init__(self, master):
        self.master = master

        d = Documento()
        j = 0
        lista= []
        lista = d.buscaTodosDocumentos()

        self.container1 = tk.Frame(self.master, pady = 20, padx = 30)
        self.listbox1 = tk.Listbox(self.container1, width = 30)

        self.listbox1.insert(END, "Codigo " + "- Nome")

        '''while j < len(lista): 
       	    if(lista[j].classe_nivel == 1):
                self.listbox1.insert(END, lista[j].classe_codigo + " " + lista[j].classe_nome)
            elif(lista[j].classe_nivel == 2):                
                self.listbox1.insert(END, "  " + lista[j].classe_codigo + " " + lista[j].classe_nome)
            elif(lista[j].classe_nivel == 3):
                self.listbox1.insert(END, "    " + lista[j].classe_codigo+ " " + lista[j].classe_nome)
            elif(lista[j].classe_nivel == 4):
                self.listbox1.insert(END, "      " + lista[j].classe_codigo+ " " + lista[j].classe_nome)

            j = j + 1'''


        self.listbox1.pack()
        self.container1.pack()
