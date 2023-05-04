from prettytable import *

class matricula:
   def __init__(self,DB,ses):
      self.BancoDados=DB
      self.sesssao=ses

   def inserir(self):
      tb_matricula=self.BancoDados.classes.matricula
      tb_disciplinas=self.BancoDados.classes.disciplinas
      #Listar todas as disciplinas disponíveis
      disciplinas=self.sesssao.query(tb_disciplinas).all()
      for dis in disciplinas:

      #Escolher disciplina por id
      #Listar alunos
      #Escolher aluno por id
      #Pedir menção
      #Pedir número de faltas
      #Gravar na associativa
      #Mostrar alunos matriculados na disciplina escolhida
