import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from prettytable import *

# --------------------------------------- VARIÁVEIS GLOBAIS ------------------------------------
# Ligação com o esquema de banco de dados
engine = create_engine("mysql+mysqlconnector://root:uniceub@localhost/bd_escola?charset=utf8mb4")

# Mapeamento Objeto Relacional com o SQLAlchemy
DB = automap_base()
DB.prepare(engine, reflect=True)
tb_alu = DB.classes.tb_alu
tb_dis = DB.classes.tb_dis
ta_mat = DB.classes.ta_mat

# Trabalho com sessões da base agora Objeto-Relacional
session_factory = sessionmaker(bind=engine)
ses = session_factory()
#-------------------------------------------------------------------------------------------------

continuar = True
while continuar:
   print("\n" * 30)
   # Descobrindo o menor e maior identificador cadastrado
   #menor, maior = ses.query(func.min(tb_cliente.idt_cliente), func.max(tb_cliente.idt_cliente)).first()
   disciplinas=ses.query(tb_dis).all()
   tab=PrettyTable(["Identificador","Nome da disciplina","Carga horária"]) #intancia um objeto tab do tipo Prettytable
   for c in clientes:
      tab.add_row([c.idt_dis,c.nme_dis,c.num_c_dis]) # adiciona os dados linha por linha
   print(tab)
   idt = int(input('Matricular aluno em turma?: '))
   cli = ses.query(disciplinas).filter_by(idt_dis=idt).first()
   if cli==None:
      input("Cliente não encontrado. Tecle [Enter] para recomeçar.")
      continue

   print("\n" * 30)
   # Listar os serviços disponíveis
   servicos = ses.query(tb_alu).all()
   print('Catálogo de alunos')
   print('-' * 40)
   for s in servicos:
       print(s.idt_alu, '-', s.nme_alu, 'R$', s.dta_nasc_alu)
   print('-' * 40)
   print('Aluno:', cli.nme_alu)
   idt = int(input('Qual número do aluno para matricular? '))
   dta = input('Qual a menção? ')
   hor = input('Quantas faltas ele teve? ')

   serv = ses.query(tb_servico).filter_by(idt_servico=idt).first()

   # Incluindo um novo agendamento
   a = ta_agendamento()
   a.tb_cliente = cli
   a.tb_servico = serv
   a.dti_agendamento = dta[6:10]+"-"+dta[3:5]+"-"+dta[0:2] + ' ' + hor
   ses.add(a)
   ses.commit()

   # Listar os agendamentos do cliente
   print("\n" * 30)
   print('Cliente:', cli.nme_cliente)
   print('-' * 40)
   for a in cli.ta_agendamento_collection:
       print(a.tb_servico.dsc_servico, a.dti_agendamento)

   opc = input('Fazer mais um agendamento [S-N]? ')
   if opc.upper() == 'N':
       continuar = False

ses.close()
