lista_cpfs = ['111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']

def buscaLinear(lista, valor) :
    tamanho = len(lista)
    for i in range(tamanho) :
        if valor == lista[i] :
            return True
    return False


def listaSemRepetidos(lista) :
    listaDups = []
    for cpf in lista :
        cpf = str(cpf)
        cpf = cpf.replace("-", "").replace(".", "")
        if len(cpf) == 11:
            if not buscaLinear(listaDups,cpf) :
                listaDups.append(cpf)
    return listaDups


def teste(lista_cpfs):
        listaDups = listaSemRepetidos(lista_cpfs)
        print(listaDups)

teste(lista_cpfs)