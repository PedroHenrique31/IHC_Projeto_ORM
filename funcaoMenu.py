def menu():
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
         incluir()
     elif opc == '2':
         consultar()
     elif opc == '3':
         alterar()
     elif opc == '4':
         excluir()
     elif opc == '5':
         continuar = False
     else:
         print ('Opção inválida')
         input()
 # Finalizando o programa

## Vamos colocar aqui as funcoes de CRUD
def incluir():
    pass
def consultar():
    pass
def alterar():
    pass
def excluir():
    pass