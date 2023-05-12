"""
        Disciplina DAO
    Aqui criarei uma classe DAO pra acessar a mapear os dados de disciplina.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

class DisciplinaDAO:
    #Para essa classe em específico, vou estabelecer conexão com o banco aqui.
    def __init__(self):
        motor = create_engine("mysql+pymysql://pedro:senhaTosca@localhost/db_escola?charset=utf8mb4")
        # Mapeando objetos
        DB=automap_base()
        DB.prepare(autoload_with=motor)
        self.disciplina=DB.classes.disciplina #Objeto mapeado
        fabrica_sessao = sessionmaker(bind=motor) # abre uma sessão de acesso ao BD
        self.sessao=fabrica_sessao()
    def create(self,disciplina):
        pass
    def readAll(self):
        pass
    def readByName(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass
    #Não sabia que python tinha destrutor
    def __del__(self):
        self.sessao.close()