"""
Author: Pedro Henrique Carneiro de Araújo

    Treinando mapeamento Objeto-Relacional
    Vou copiar uns codigos aqui, mpra entender como usar o SQLAlchemy.
"""

"""
    Agora uma ligeira descrição do que o código faz, feita pelo chat GPT hoje 27/04/2023:
    
    Este código utiliza a biblioteca SQLAlchemy para criar um objeto de conexão com um banco de dados 
    MySQL e mapear as tabelas do banco de dados para objetos Python.
    
    Na primeira linha, ele importa as bibliotecas necessárias do SQLAlchemy. Em seguida, 
    cria um objeto de conexão com o banco de dados MySQL usando o módulo PyMySQL.

    O objeto de conexão é criado usando a função `create_engine`, que recebe como argumento uma string 
    de conexão que contém informações como o tipo de banco de dados, o tipo de conector, 
    o nome do usuário, a senha, o local de acesso e o nome do schema.

    Depois disso, ele cria um objeto `DB` que acessa o banco de dados usando o objeto de conexão `motor` 
    e, em seguida, usa o método `prepare` para mapear as tabelas do banco de dados para objetos Python. 
    As tabelas são mapeadas usando o objeto `DB.classes`.

    Por fim, o código imprime o tipo do objeto Python que representa a tabela `aluno`.

    Quanto ao erro que você mencionou, não é possível saber qual é o erro sem ver a mensagem de erro. 
    Se você puder compartilhar a mensagem de erro, poderei ajudá-lo a entender e corrigir o problema.
"""



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from funcaoMenu import *

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

# Trabalho com sessões da base agora Objeto-Relacional (utilizamos o padrão de projeto factory aqui)
fabrica_sessao = sessionmaker(bind=motor) # cria um objeto que gera uma sessão com esse motor
ses = fabrica_sessao() # ses é uma sessão que possui 'motor' para se conectar ao BD
#------------------------------------------------------------





menu()
