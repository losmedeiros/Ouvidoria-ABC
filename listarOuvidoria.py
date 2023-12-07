from operacoesbd import *

def listarOuvidoria (cn):

    consultaListaOuvidoria = "select * from ouvidoria;"
    listaOuvidoria = listarBancoDados(cn,consultaListaOuvidoria)

    if len(listaOuvidoria) > 0:
        print("Ouvidoria ABC")
        for ouvidoria in listaOuvidoria:
            print (ouvidoria[0],"| "+ouvidoria[1]+" | "+ouvidoria[2]+" | "+ ouvidoria[3] +" | "+ouvidoria[4])
    else:
        print ("Lista vazia!")