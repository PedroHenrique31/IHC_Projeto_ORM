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
    for c in daoDisciplina.readAll():
        print(c.NOME+" - "+c.SIGLA+" Carga horária: "+str(c.CARGA_HORARIA))
def testeReadName():
    for c in daoDisciplina.readByName('j'):
        print(c.NOME)
def testeUpdate():
    disc=daoDisciplina.readByID(12)
    disc.NOME="Preenchimento IRPF 2018"
    daoDisciplina.update()
def testeDelete():
    disc=daoDisciplina.readByID(12)
    daoDisciplina.delete(disc)

#testeCreate()
#testeRead()
#testeReadName()
#testeUpdate()
testeDelete()