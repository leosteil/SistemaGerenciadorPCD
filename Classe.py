from Banco import Banco

class Classe(object):
	def __init__(self, idclasse = 0, classe_nome ="", classe_codigo = "", id_classe_subordinacao = "", classe_regAbertura = "", classe_regDesativacao = "", classe_reativacao = "", classe_regMudancaNome = "", classe_regDeslocamento = "", classe_regExtincao = "", classe_indicador = "", classe_nivel = ""):
		
		self.info = {}
		self.idclasse = idclasse
		self.classe_nome = classe_nome
		self.classe_codigo = classe_codigo
		self.id_classe_subordinacao = id_classe_subordinacao
		self.classe_regAbertura = classe_regAbertura
		self.classe_regDesativacao = classe_regDesativacao
		self.classe_reativacao = classe_reativacao
		self.classe_regMudancaNome = classe_regMudancaNome
		self.classe_regDeslocamento = classe_regDeslocamento
		self.classe_regExtincao = classe_regExtincao
		self.classe_indicador = classe_indicador
		self.classe_nivel = classe_nivel


	def insertClasse(self):
		banco = Banco()
		try:
			c = banco.conexao.cursor()

			c.execute("insert into classe (classe_nome, classe_codigo, id_classe_subordinacao, classe_regAbertura, classe_regDesativacao, classe_reativacao, classe_regMudancaNome, classe_regDeslocamento, classe_regExtincao, classe_indicador, classe_nivel) values('"+ self.classe_nome + "','" + self.classe_codigo + "','" + self.id_classe_subordinacao +"','" + self.classe_regAbertura + "','" + self.classe_regDesativacao + "','" + self.classe_reativacao + "','" + self.classe_regMudancaNome + "','" + self.classe_regDeslocamento + "','" + self.classe_regExtincao + "','" + self.classe_indicador + "','" + self.classe_nivel + "')" )

			banco.conexao.commit()
			c.close()

			return "Classe cadastrada com sucesso"
		except:
			return "Ocorreu um erro na inserção do usuário"


	def buscaTodasClasses(self):
		banco = Banco()
		j = 0
		lista = []
		lista2 = []

		try:
			con = banco.conexao.cursor()
			con.execute("select * FROM classe order by CAST(classe_codigo as integer)")


			for linha in con:
				c = Classe()
				c.idclasse = linha[0]
				c.classe_nome = linha[1]
				c.classe_codigo = linha[2]
				c.id_classe_subordinacao = linha[3]
				c.classe_regAbertura = linha[4]
				c.classe_regDesativacao = linha[5]
				c.classe_reativacao = linha[6]
				c.classe_regMudancaNome = linha[7]
				c.classe_regDeslocamento = linha[8]
				c.classe_regExtincao = linha[9]
				c.classe_indicador = linha[10]
				c.classe_nivel = linha[11]

				lista.append(c)

			return lista
		except:
			return lista2

	def buscaClasse(self, codClasse):
		banco = Banco()
		c1 = Classe()

		query = "select * FROM classe WHERE classe_codigo = " + codClasse

		try:
			con = banco.conexao.cursor()
			con.execute(query)

			for linha in con:
				c = Classe()				
				c.idclasse = linha[0]
				c.classe_nome = linha[1]
				c.classe_codigo = linha[2]
				c.id_classe_subordinacao = linha[3]
				c.classe_regAbertura = linha[4]
				c.classe_regDesativacao = linha[5]
				c.classe_reativacao = linha[6]
				c.classe_regMudancaNome = linha[7]
				c.classe_regDeslocamento = linha[8]
				c.classe_regExtincao = linha[9]
				c.classe_indicador = linha[10]
				c.classe_nivel = linha[11]

			print(c.classe_codigo + "TESTE")

			return c
		except:
			return c1