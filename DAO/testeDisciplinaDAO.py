from disciplinaDAO import DisciplinaDAO

daoDisciplina=DisciplinaDAO()
def testeCreate():
    #daoDisciplina=DisciplinaDAO()

    novaDisciplina=daoDisciplina.disciplina()
    novaDisciplina.NOME="Manutenção de bolo de pote"
    novaDisciplina.SIGLA="MBPT"
    novaDisciplina.CARGA_HORARIA=12

    daoDisciplina.create(novaDisciplina)
def testeRead():
    pass
def testeReadName():
    pass
def testeUpdate():
    pass
def testeDelete():
    pass

testeCreate()