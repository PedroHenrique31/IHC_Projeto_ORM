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
        self.sessao.add(disciplina)
        self.sessao.commit()
    def readAll(self):
        disciplinas=self.sessao.query(self.disciplina).all()
        return disciplinas
    def readByName(self,nomeDisciplina):
        disc=self.disciplina
        disciplinasEncontrada=self.sessao.query(disc).filter_by(disc.NOME.ilike('%'+nomeDisciplina+'%')).all()
        return disciplinasEncontrada
    def update(self):
        self.sessao.commit()
    def delete(self,disciplina):
        self.sessao.delete(disciplina)
        self.sessao.commit()
    #Não sabia que python tinha destrutor
    def __del__(self):
        self.sessao.close()

