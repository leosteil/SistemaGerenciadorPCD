from Banco import Banco

class Documento(object):
	def __init__ (self, iddocumento = 0, documento_nome = "", documento_codigo = "", doc_guarda_fase_corrente = "", doc_guarda_fase_intermediaria = "", dest_final = "", reg_alteracao = "", obs = ""):
		
		self.info = {}
		self.iddocumento = iddocumento
		self.documento_nome = documento_nome
		self.documento_codigo = documento_codigo
		self.doc_guarda_fase_corrente = doc_guarda_fase_corrente
		self.doc_guarda_fase_intermediaria = doc_guarda_fase_intermediaria
		self.dest_final = dest_final
		self.reg_alteracao = reg_alteracao
		self.obs = obs
		
	def insertDocumento(self):
		banco = Banco()
		try:
			d = banco.conexao.cursor()
			print(self.obs)
			d.execute("insert into documento (documento_nome, documento_codigo, doc_guarda_fase_corrente, doc_guarda_fase_intermediaria, dest_final, reg_alteracao, obs) values('"+ self.documento_nome + "','"+ self.documento_codigo + "','"+ self.doc_guarda_fase_corrente + "','"+ self.doc_guarda_fase_intermediaria + "','"+ self.dest_final + "','"+ self.reg_alteracao + "','" + self.obs + "')" )
			banco.conexao.commit()
			d.close()
			
			return "Documento cadastrado com sucesso"
		except:
			return "Ocorreu um erro na inserção do Documento" 
	
	def buscaTodosDocumentos(self):
		banco = Banco()
		lista = []
		lista2 = []
		
		try:
				con = banco.conexao.cursor()
				con.execute("select * FROM documento")
				
				for linha in con:
					d = Documento()
					d.iddocumento = linha[0]
					d.documento_nome = linha[1]
					d.documento_codigo = linha[2]
					d.doc_guarda_fase_corrente = linha[3]
					d.doc_guarda_fase_intermediaria = linha[4]
					d.dest_final = linha[5]
					d.reg_alteracao = linha[6]
					d.obs = linha[7]
					
					lista.append(d)
				
				return lista
		except:
				return lista2
