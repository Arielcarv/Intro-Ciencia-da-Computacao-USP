import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado! ")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

# Minha implementação

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura = []
    lista_palavras = []
    lista_frases = []
    soma_tamanho_palavras = 0
    total_de_palavras = 0

    # Lista de Sentenças
    lista_sentenças = separa_sentencas(texto)
    for sent in lista_sentenças:
        novas_frases = separa_frases(sent)
        lista_frases.extend(novas_frases)

    for frase in lista_frases:
        novas_palavras = separa_palavras(frase)
        lista_palavras.extend(novas_palavras)

    for palavra in lista_palavras:
        soma_tamanho_palavras += len(palavra.strip())
        total_de_palavras += 1

    """Tamanho médio de palavra"""
    wal_texto = soma_tamanho_palavras / total_de_palavras
    assinatura.append(wal_texto)

    """Relação Type-Token"""
    ttr_texto = n_palavras_diferentes(lista_palavras) / total_de_palavras
    assinatura.append(ttr_texto)

    """Razão Hapax Legomana"""
    hlr_texto = n_palavras_unicas(lista_palavras) / total_de_palavras
    assinatura.append(hlr_texto)

    """Tamanho médio de sentença"""
    total_caracteres_sentenças = 0
    for position in range(len(lista_sentenças)):
        total_caracteres_sentenças += len(lista_sentenças[position])
    sal_texto = total_caracteres_sentenças / len(lista_sentenças)
    assinatura.append(sal_texto)

    """Complexidade de sentença"""
    total_de_frases = len(lista_frases)
    sac_texto = total_de_frases / len(lista_sentenças)
    assinatura.append(sac_texto)

    """Tamanho médio de frase"""
    total_caracteres_frases = 0
    for position in range(len(lista_frases)):
        total_caracteres_frases += len(lista_frases[position])
    pal_texto = total_caracteres_frases / len(lista_frases)
    assinatura.append(pal_texto)

    """Return assinatura_do_texto"""
    return assinatura


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    Sab = 0
    for indice in range(5):
        Sab += abs(as_a[indice] - as_b[indice])
        grau_de_similaridades = Sab / 6

    return grau_de_similaridades


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_Sab = []
    for eachtext in textos:
        as_texto = calcula_assinatura(eachtext)
        comparar = compara_assinatura(ass_cp, as_texto)
        lista_Sab.append(comparar)


    max_value = max(lista_Sab)

    texto_com_maior_probabilidade = lista_Sab.index(max_value)
    return texto_com_maior_probabilidade


def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    avalia_textos(textos, ass_cp)

    print(f"O autor do texto {avalia_textos(textos, ass_cp)} está infectado com COH-PIAH")


main()
