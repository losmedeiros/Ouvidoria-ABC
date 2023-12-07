from operacoesbd import *

def listarOuvidoria(cn):

    consultaListaOuvidoria = "select * from ouvidoria;"
    listaOuvidoria = listarBancoDados(cn,consultaListaOuvidoria)

    if len(listaOuvidoria) > 0:
        print("Ouvidoria ABC")
        for item in listaOuvidoria:
            print()
            print ('Código: ', item[0],'|','Nome: ', item[1],'|', 'Tipo: ', item[2],'|','Descrição: ', item[3],'|','Status: ', item[4])
    else:
        print ("Lista De Ocorrências vazia!")

def inserirOuvidoria(cn):

    consultaInserirOuvidoria= "insert into ouvidoria(nome,tipo,descricao, estado) values(%s,%s,%s,%s);"

    nome = input("Digite seu nome: ")
    print("Escolha uma das opções a seguir")
    print("S = Sugestão")
    print("E = Elogio")
    print("R = Reclamação")
    tipo = input ("Qual o tipo de Ocorrência? ")
    if tipo == "S" or tipo == "s":
        tipoObservacao = "Sugestão"
        descricao = input("Digite a descrição: ")
        status = 'Em Aberto'

        dados = [nome,tipoObservacao, descricao, status]

        insertNoBancoDados(cn, consultaInserirOuvidoria, dados)
        print('Ocorrência inserida com sucesso!')
    elif tipo == "E" or tipo == "e":
        tipoObservacao = "Elogio"
        descricao = input("Digite a descrição da Ocorrência: ")
        status = 'Em Aberto'

        dados = [nome, tipoObservacao, descricao, status]

        insertNoBancoDados(cn, consultaInserirOuvidoria, dados)
        print('Ocorrência inserida com sucesso!')
    elif tipo == "R" or tipo == "r":
        tipoObservacao = "Reclamação"
        descricao = input("Digite a descrição: ")
        status = 'Em Aberto'

        dados = [nome, tipoObservacao, descricao, status]

        insertNoBancoDados(cn, consultaInserirOuvidoria, dados)
        print('Ocorrência inserida com sucesso!')
    else:
        print("Opção invalida!")

def updateOuvidoria(cn):

    codigo = input("Digite o codigo Da ocorrência que deseja atualizar: ")
    consultaPesquisarCodigo = "select * from ouvidoria where numeracao = "+ codigo
    listaOuvidoria = listarBancoDados(cn, consultaPesquisarCodigo)

    if len(listaOuvidoria) > 0:
        sqlUpdate = "update ouvidoria set estado = %s where numeracao =%s"
        print("Ouvidoria Pesquisada")

        print("Escolha uma das opções a seguir")
        print("AB = Em Aberto")
        print("AN = Em Andamento")
        print("FN = Finalizado")

        status = input("Digite uma das 3 opções de status da Ocorrência: ")

        if status == "AB" or status == "ab" or status == "Ab" or status == "aB":
            novoEstado = "Em Aberto"
            valores = [novoEstado, codigo]
            atualizarBancoDados(cn,sqlUpdate, valores)
            print("Status atualizado!")

        elif status == "AN" or status == "an" or status == "An" or status == "aN":
            novoEstado = "Em Andamento"
            valores = [novoEstado, codigo]
            atualizarBancoDados(cn,sqlUpdate, valores)
            print("Status atualizado!")

        elif status == "FN" or status == "fn" or status == "Fn" or status == "fN":
            novoEstado = "Finalizado"
            valores = [novoEstado, codigo]
            atualizarBancoDados(cn,sqlUpdate, valores)
            print("Status atualizado!")

        else:
            print("Opção invalida!")
    else:
        print("Não existe Ocorrência com esse codigo!")
def removerOuvidoria (cn):
    print('Listagem de ocorrências')
    print()

    consultaListaOuvidoria = "select * from ouvidoria;"
    listaOcorrencia = listarBancoDados(cn, consultaListaOuvidoria)

    if len(listaOcorrencia) == 0:
        print('Não existem ocorrências a serem exibidas')
    else:
        for item in listaOcorrencia:
            print ('Código: ', item[0],'|','Nome: ', item[1],'|', 'Tipo: ', item[2])

        print()

        codigo = input('Digite o código da ocorrência a ser removida: ')
        consultaRemoverOuvidoria = "delete from ouvidoria where numeracao = %s"
        dados = [codigo]

        ouvidoriaRemovida = excluirBancoDados(cn,consultaRemoverOuvidoria,dados)
        if ouvidoriaRemovida > 0 :
            print ("Ocorrência Removida!")
        else:
            print("Não existe Ocorrência com este codigo!")

def pesquisarPorCodigo (cn):
    codigoPesquisado = input("Digite o codigo desejado: ")
    consultaPesquisarCodigo = "select * from ouvidoria where numeracao = "+ codigoPesquisado
    listaOuvidoria = listarBancoDados(cn,consultaPesquisarCodigo)

    if len(listaOuvidoria) > 0:
        print ("OCorrência Pesquisada")
        for item in listaOuvidoria:
            print()
            print ('Código: ', item[0],'|','Nome: ', item[1],'|', 'Tipo: ', item[2],'|','Descrição: ', item[3],'|','Status: ', item[4])
    else:
        print('Não existem ocorrência com esse codigo!')