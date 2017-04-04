import sqlite3

class Banco():
   
      def __init__(self,):
          self.conexao = sqlite3.connect("banco.db")
          self.createTable()
   
      def createTable(self):
          c = self.conexao.cursor()
   
          c.execute("""create table if not exists classe (
                       idclasse integer primary key autoincrement ,
                       classe_nome text,
                       classe_codigo text,
                       classe_subordinacao text,
                       classe_regAbertura text,
                       classe_regDesativacao text,
                       classe_reativacao text,
                       classe_regMudancaNome text,
                       classe_regDeslocamento text,
                       classe_regExtincao text,
                       classe_indicador text,
                       classe_nivel int)
                       """)
          
          c.execute("""create table if not exists documento (
                       iddocumento integer primary key autoincrement ,
                       documento_nome text,
                       documento_codigo text,
                       doc_guarda_fase_corrente text,
                       doc_guarda_fase_intermediaria text,
                       dest_final text,
                       reg_alteracao text,
                       obs text)
                       """)
          
          self.conexao.commit()
          c.close()
