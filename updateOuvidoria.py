from operacoesbd import *

def updateOuvidoria(cn):

    sqlUpdate = "update ouvidoria set estado = %s where numeracao = %s"

    novoEstado = input("Atualize o tipo: ")
    codigo = input ("Digite o codigo o qual deseja alterar: ")

    valores = [novoEstado,codigo]
    atualizarBancoDados(cn,sqlUpdate,valores)
