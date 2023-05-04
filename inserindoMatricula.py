from prettytable import *


class matricula_func:
    def __init__(self, DB, ses):
        self.BancoDados = DB
        self.sesssao = ses

    def inserir(self):
        tb_matricula = self.BancoDados.classes.matricula
        tb_disciplinas = self.BancoDados.classes.disciplina
        tb_aluno = self.BancoDados.classes.aluno
        # Listar todas as disciplinas disponíveis
        disciplinas = self.sesssao.query(tb_disciplinas).all()
        tabelaDis = PrettyTable(["ID", "Nome", "Sigla"])
        print("--------- Disciplinas disponíveis ----------------")
        for dis in disciplinas:
            tabelaDis.add_row([dis.COD, dis.NOME, dis.SIGLA])
        print(tabelaDis)
        ## Escolher disciplina por id
        id_disciplina = int(input("Digite o ID da disciplina que deseja selecionar: "))
        disciplina_mat = self.sesssao.query(tb_disciplinas).filter_by(COD=id_disciplina).first()
        if disciplina_mat == None:
            input("Disciplina não encontrada. Pressione [Enter] para recomeçar.")
        # Listar alunos
        alunos = self.sesssao.query(tb_aluno).all()
        tabelaAlu = PrettyTable(["ID", "Nome"])
        print("--------- Alunos disponíveis ----------------")
        for alu in alunos:
            tabelaAlu.add_row([alu.COD, alu.NOME])
        print(tabelaAlu)
        ## Escolher aluno por id
        id_aluno = int(input("Digite o número do aluno que deseja selecionar: "))
        aluno_mat = self.sesssao.query(tb_aluno).filter(tb_aluno.COD == id_aluno).first()
        if aluno_mat == None:
            input("Aluno não encontrado. Pressione [Enter] para recomeçar.")
        ## criar novo objeto
        matricula_nova = tb_matricula()
        matricula_nova.aluno = aluno_mat
        matricula_nova.disciplina = disciplina_mat
        # Pedir menção
        matricula_nova.MENCAO = input("Digite a menção do aluno: ")
        # Pedir número de faltas
        matricula_nova.QTD_FALTAS = int(input("Digite o número de faltas: "))
        # Gravar na associativa
        self.sesssao.add(matricula_nova)
        self.sesssao.commit()
        # Mostrar alunos matriculados na disciplina escolhida
        tabelaMat = PrettyTable(["Aluno"])
        for a in disciplina_mat.matricula_collection:
            tabelaMat.add_row([a.aluno.NOME])
        print(tabelaMat)
