from operacoesbd import *

def removerOuvidoria ():

    consultaRemoverOuvidoria = "delete from ouvidoria where numeracao = %s"
    codigo = input("Qual o codigo que deseja remover? ")
    dados = [codigo]

    excluirBancoDados(cn,consultaRemoverOuvidoria,dados)
