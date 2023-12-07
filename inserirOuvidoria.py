from operacoesbd import *

def inserirOuvidoria(cn):

    consultaInserirOuvidoria= "insert into ouvidoria(nome,tipo,descricao) values(%s,%s,%s);"

    nome = input("Digite seu nome: ")
    tipo= input ("Qual o tipo de observação? ")
    descricao = input ("Digite a descrição: ")

    dados = [nome,tipo,descricao]

    insertNoBancoDados(cn,consultaInserirOuvidoria,dados)
