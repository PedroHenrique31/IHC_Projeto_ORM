"""
Author: Pedro Henrique Carneiro de Araújo

    Treinando mapeamento Objeto-Relacional
    Vou copiar uns codigos aqui, mpra entender como usar o SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

# ------- Variáveis globais ---------------------------------------------------
# Ligação com o DB feita por um objeto motor -engine- do SQLAlchemy ele que realiza o trabalho de conectar e mapear
motor=create_engine("mysql+pymysql://pedro:senhaTosca@localhost/db_escola?charset=utf8mb4")
# estrutura URL:  ([tipoDB]+[tipoConnector]://[nomeUsuário]:[senha]@[localacesso]/[nomeSchema]?[outrasInfo])

# Mapeando o BD para os Objetos
DB=automap_base() # cria um objeto que acessa o BD
DB.prepare(autoload_with=motor) # acessa o BD usando o motor
## agora sim mapeia as tabelas para objetos
aluno=DB.classes.aluno
disciplina=DB.classes.disciplina
matricula=DB.classes.matricula

#print(type(aluno)) # tá... queria ver a classe aí, mas fiquei mais confuso


