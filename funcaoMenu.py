from sqlalchemy.ext.automap import automap_base


class visualiza:
    # gera uma classe com um BD, opnde perfomamos as coisas
    def __init__(self, DB,ses):
        self.BancoDados = DB
        self.sessao=ses

    def menu(self):
        continuar = True
        while continuar:
            print('\n' * 12)
            print('CRUD de Serviços - MENU')
            print('1 - Incluir')
            print('2 - Consultar')
            print('3 - Alterar')
            print('4 - Excluir')
            print('5 - Sair')
            opc = input('Qual a sua opção? ')
            print("\n" * 30)
            if opc == '1':
                self.incluir()
            elif opc == '2':
                consultar()
            elif opc == '3':
                alterar()
            elif opc == '4':
                excluir()
            elif opc == '5':
                continuar = False
            else:
                print('Opção inválida')
                input()
        # Finalizando o programa


    ## Vamos colocar aqui as funcoes de CRUD
    def incluir(self):

        opcao = input("Selecione o que deseja incluir\n1-Aluno\n2-Disciplina\n3-Matricular aluno em disciplina\n")
        if opcao == '1':
            self.inserirAluno()
        else:
            print("Não entendi o que disse")

    def inserirAluno(self):

        aluno = self.BancoDados.classes.aluno # isso gera uma classe que representa a tablea aluno no banco
        novoAluno=aluno()
        print(type(aluno))
        print("\n" * 30)
        print("Digite as informações a seguir")
        nome = input("Nome do aluno: ")
        nascimento = input("Data de nascimento do aluno: ")
        novoAluno.NOME=nome
        novoAluno.DATA_NASCIMENTO=nascimento
        self.sessao.add(novoAluno)
        self.sessao.commit()

    def consultar(self):
        pass


    def alterar(self):
        pass


    def excluir(self):
        pass

def incluirMatricula():
    pass


def inserirDisciplina():
    pass



