'''
Projeto ouvidoria
UNIFACISA
Professor: Daniel Abella
Nome Grupo:
- jose carlos
- klyane cabral
- Felipe Duarte
- Pedro Henrique
- Luis Eduardo

'''

from ouvidoria import *

cn = criarConexao('localhost','root','root','db_ouvidoria_abc') #conectando ao banco de dados

opcao = 1
print()
print('Bem-vindo à Ouvidoria ABC 🗿🍷')
while opcao != 6:
    print()
    print('Opções da Ouvidoria: ')
    print("1)Listar"
          "\n2)Inserir"
          "\n3)Atualizar Status"
          "\n4)Pesquisar"
          "\n5)Remover"
          "\n6)Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        listarOuvidoria(cn)
    elif opcao == 2:
        inserirOuvidoria(cn)
    elif opcao == 3:
        listarOuvidoria(cn)
        updateOuvidoria(cn)
    elif opcao == 4:
        pesquisarPorCodigo(cn)
    elif opcao == 5:
        removerOuvidoria(cn)
    elif opcao != 6:
        print('Opção inválida, tente novamente.')

print()
print('A Ouvidoria ABC 🗿🍷 agradece pelo seu acesso.')
print('Bye!👋')

encerrarBancoDados(cn) #encerrando a conexão como banco de dados