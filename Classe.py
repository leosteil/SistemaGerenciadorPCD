from Banco import Banco

class Classe(object):
	def __init__(self, idclasse = 0, classe_nome ="", classe_codigo = "", classe_subordinacao = "", classe_regAbertura = "", classe_regDesativacao = "", classe_reativacao = "", classe_regMudancaNome = "", classe_regDeslocamento = "", classe_regExtincao = "", classe_indicador = ""):
		
		self.info = {}
		self.idclasse = idclasse
		self.classe_nome = classe_nome
		self.classe_codigo = classe_codigo
		self.classe_subordinacao = classe_subordinacao
		self.classe_regAbertura = classe_regAbertura
		self.classe_regDesativacao = classe_regDesativacao
		self.classe_reativacao = classe_reativacao
		self.classe_regMudancaNome = classe_regMudancaNome
		self.classe_regDeslocamento = classe_regDeslocamento
		self.classe_regExtincao = classe_regExtincao
		self.classe_indicador = classe_indicador


	def insertClasse(self):
		banco = Banco()
		try:
			c = banco.conexao.cursor()

			c.execute("insert into classe (classe_nome, classe_codigo, classe_subordinacao, classe_regAbertura, classe_regDesativacao, classe_reativacao, classe_regMudancaNome, classe_regDeslocamento, classe_regExtincao, classe_indicador) values('"+ self.classe_nome + "','" + self.classe_codigo + "','" + self.classe_subordinacao +"','" + self.classe_regAbertura + "','" + self.classe_regDesativacao + "','" + self.classe_reativacao + "','" + self.classe_regMudancaNome + "','" + self.classe_regDeslocamento + "','" + self.classe_regExtincao + "','" + self.classe_indicador + "')" )

			banco.conexao.commit()
			c.close()

			return "Classe cadastrada com sucesso"
		except:
			return "Ocorreu um errro na inserção do usuário"


	def buscaTodasClasses(self, tipo):
		banco = Banco()
		classe = Classe()
		lista = []
		lista2 = []

		try:
			c = banco.conexao.cursor()

			c.execute("select * From classe")

			if(tipo == 0):
				for linha in c:
					lista.append(linha[2] + " " + linha[1]) #manda apenas os conteúdos de codigo e nome para serem exibidos
			else:
				for linha in c:
					lista.append(linha[2] + ", " + linha[1]+ ", " + linha[3]+ ", " + linha[4]+ ", " + linha[5]+ ", " + linha[6]+ ", " + linha[7]+ ", " + linha[8]+ ", " + linha[9]+ ", " + linha[10]) #manda apenas os conteúdos de codigo e nome para serem exibidos

			return lista
		except:
			return lista2	