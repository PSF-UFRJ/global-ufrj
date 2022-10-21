# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 22:57:20 2022

@author: Emanuel Cardoso
"""
import doctest
import random
import itertools

# cartas = ["A", "A", "A", "A", "A",
#           "7", "7", "7", "7", "7",
#           "K", "K", "K", "K", "K",
#           "Q", "Q", "Q", "Q", "Q",
#           "J", "J", "J", "J", "J"]

# Ontologia de erros:
class MaoErrada(Exception): pass

class TipoRodadaErrado(Exception): pass

class TipoJogador1Errado(Exception): pass

class TipoJogador2Errado(Exception): pass

class DoisTiposJogadoresHumanosÉErrado(Exception): pass

class NumeroDeRemocaoErrado(Exception): pass

class CartasMaoNumeroErrado(Exception): pass

#
# Questão 1 - a)
#
def valor_mao(mao):
    """Recebe uma mão e retorna o seu valor em pontos.
    
    >>> valor_mao(["A", "A", "J", "Q", "K"])
    1
    
    >>> valor_mao(["A", "A", "7", "7", "J"])
    2
    
    >>> valor_mao(["A", "A", "A", "J", "Q"])
    3
    
    >>> valor_mao(["A", "A", "A", "7", "7"])
    5
    
    >>> valor_mao(["A", "A", "A", "A", "J"])
    10
    
    >>> valor_mao(["A", "A", "A", "A", "A"])
    50
    """
    # Verifica se mão tem no máximo cinco cartas
    if len(mao) != 5:
        raise MaoErrada
        
    # Cópia de segurança de mão:
    mao_ordenada = mao.copy()
    mao_ordenada.sort()
    duplas = 0
    trincas = 0
    quadras = 0
    quinas = 0
    
    carta_anterior = None
    status = 1
    for carta_atual in mao_ordenada:
        if not (carta_anterior is None):
            if carta_anterior == carta_atual:
                status += 1
                if status == 2:
                    duplas += 1
                elif status == 3:
                    duplas -= 1
                    trincas += 1
                elif status == 4:
                    trincas -= 1
                    quadras += 1
                else:
                    quadras -= 1
                    quinas += 1
            else:
                status = 1
        carta_anterior = carta_atual
    if duplas == 1 and trincas == 0:
        return 1
    elif duplas == 2:
        return 2
    elif trincas == 1 and duplas == 0:
        return 3
    elif trincas == 1 and duplas == 1:
        return 5
    elif quadras == 1:
        return 10
    elif quinas == 1:
        return 50
    return 0

#
# Questão 1 - b)
#

def duas_maos(mao1, mao2):

    """função que recebe duas mãos e retorna uma tupla, com o número de pontos 
    que cada jogador vai receber.
        >>> duas_maos(["A","A","K","K","K"],["J","K","J","7","A"])
        (5, 1)
        >>> duas_maos(["Q","Q","Q","Q","7"],["7","7","J","K","A"])
        (10, 1)
        """
    return (valor_mao(mao1), valor_mao(mao2))
doctest.testmod()
#
# Questão 1 - c) Função auxiliar
#
import doctest
def contagem_cartas(mao): # pythonTutor
    """ Função auxiliar que irá contar as cartas disposto na mão e retorna uma dicionário
    com o a quantidade de cartas dispostas na mão.
        >>> contagem_cartas(["A","J","K","Q","Q"])
        {'A': 1, 'J': 1, 'K': 1, 'Q': 2}
        >>> contagem_cartas(["A","A","Q","K","Q"])
        {'A': 2, 'Q': 2, 'K': 1}
    """
    cartas_hash = dict()
    for i in mao:
        if i in cartas_hash:
            cartas_hash[i] += 1
        else:
            cartas_hash[i] = 1
    return cartas_hash
doctest.testmod()
#
# Questão 1 - c) Função principal
#
def nao_contribui(mao):
    """ Função principal que recebe a mão e análisa as cartas que não contribui para o deck.
        >>> nao_contribui(['J', '7', '7', 'K', 'Q'])
        ['J', 'K', 'Q']
        >>> nao_contribui(['A', 'J', 'K', 'Q', 'Q'])
        ['A', 'J', 'K']
    """
    mao_hash = contagem_cartas(mao)
    return [k for k,v in mao_hash.items() if v == 1]
doctest.testmod()
#
# Questão 1 - d)
#
import doctest
def nao_contribui_max_3(mao):
    """ função que recebe uma mão e retorna uma lista de no máximo 3 cartas
que não contribuem para o valor da mão.
        >>> nao_contribui_max_3(["A","J","K","Q","Q"])
        ['A', 'J', 'K']
        >>> nao_contribui_max_3(["J","7","A","K","Q"])
        ['J', '7', 'A']
    """
    return nao_contribui(mao)[:3]
doctest.testmod()
#
# Questão 2 - a)
#
def possibilidades(mao_parcial, num_cartas, cartas_restantes): # **  **
    combinacoes_restantes = itertools.combinations(cartas_restantes, num_cartas)
    for c in combinacoes_restantes:
        yield list(mao_parcial) + list(c)

#
# Questão 2 - b) Função Auxiliar
#
def diferenca_de_lista(lista_original, itens_a_remover): # ** **
    itens_a_remover_hash = dict()
    for i in itens_a_remover:
        if i in itens_a_remover_hash:
            itens_a_remover_hash[i] += 1
        else:
            itens_a_remover_hash[i] = 1
    lista_a_retornar = list()
    for l in lista_original:
        if not l in itens_a_remover_hash:
            lista_a_retornar.append(l)
        else:
            if itens_a_remover_hash[l] == 0:
                lista_a_retornar.append(l)
            else:
                itens_a_remover_hash[l] -= 1
    return lista_a_retornar

#
# Questão 2 - b) Função Auxiliar
#
def possibilidades_da_mao(cartas_mao, cartas_a_remover):
    if len(cartas_a_remover) > 3:
        raise NumeroDeRemocaoErrado
    if len(cartas_mao) != 5:
        raise CartasMaoNumeroErrado
        
    cartas = ["A", "A", "A", "A", "A",
              "7", "7", "7", "7", "7",
              "K", "K", "K", "K", "K",
              "Q", "Q", "Q", "Q", "Q",
              "J", "J", "J", "J", "J"]
    
    # As cartas restantes estão dadas aqui, são aquelas que não são a mão
    # original
    cartas_restantes = diferenca_de_lista(cartas, cartas_mao)
    # Essa é a mão parcial
    mao_parcial = diferenca_de_lista(cartas_mao, cartas_a_remover)
    return possibilidades(
        mao_parcial, 
        len(cartas_a_remover), 
        cartas_restantes)

#
# Questão 2 - b) Função Auxiliar
#
def calcula_possibilidades(cartas_mao, cartas_a_remover):
    if len(cartas_a_remover) > 3:
        raise NumeroDeRemocaoErrado
    if len(cartas_mao) != 5:
        raise CartasMaoNumeroErrado
        
    todas_possibilidades = possibilidades_da_mao(cartas_mao, cartas_a_remover)
    possibilidades_totais = 0
    possibilidades_de_melhora = 0
    possibilidades_de_nao_alteracao_ou_piora = 0
    for p in todas_possibilidades:
        if valor_mao(p) > valor_mao(cartas_mao):
            possibilidades_de_melhora += 1
        else:
            possibilidades_de_nao_alteracao_ou_piora += 1
        possibilidades_totais += 1
    return {
        "possibilidades_totais": possibilidades_totais,
        "possibilidades_de_melhora": possibilidades_de_melhora,
        "possibilidades_de_nao_alteracao_ou_piora": possibilidades_de_nao_alteracao_ou_piora,
        "probabilidade_de_melhora": float(possibilidades_de_melhora) / float(possibilidades_totais),
        "probabilidade_de_nao_alteracao_ou_piora":float(possibilidades_de_nao_alteracao_ou_piora) / float(possibilidades_totais)
        }

#
# Questão 2 - b) Função Principal
#
# Se você executar essa função, verá que a probabilidade de melhora é igual a 73,3%,
# enquanto a probabilidade de não alteração dos pontos é igual a 26.7%, aproximadamente,
# nos dois casos. 
#
# Considerando os casos absolutos, existem 836 combinações possíveis de cartas, com a troca
# que melhoram a pontuação da mão, enquanto existem 304 casos possíveis de não alteração.
#
# Veja o DocTest.
#

def calcula_probabilidades_par_troca_tres(): # ** **
    """Calcula as probabilidades de melhoria da pontuação de uma mão, 
    com uma dupla, ao se trocar as três cartas que não pertencem à dupla:
    
    >>> calcula_probabilidades_par_troca_tres()
    {'possibilidades_totais': 1140, 'possibilidades_de_melhora': 836, 'possibilidades_de_nao_alteracao_ou_piora': 304, 'probabilidade_de_melhora': 0.7333333333333333, 'probabilidade_de_nao_alteracao_ou_piora': 0.26666666666666666}
    """
    # Lista de cartas com um par qualquer, sem perda de genericidade:
    cartas_mao = ["A", "A", "K", "Q", "J"]
    cartas_a_remover = ["K", "Q", "J"]
    return calcula_possibilidades(cartas_mao, cartas_a_remover)
    
#
# Questão 2 - c)
#
# Fazendo os cálculos para trocar apenas duas cartas, ou apenas uma carta, fica claro que,
# com apenas um par na mão, vale mais a pena, considerando apenas a possibilidade de melhora,
# trocar três cartas, mas não sabemos, em qual caso, a probabilidade de melhora representa
# o maior ganho.
#
# Se trocar duas cartas, temos os seguintes resultados:
# - quantidade de jogos que melhoram valor da mão: 134
# - quantidade de jogos que não representam melhoria: 56
# - Probabilidade de melhora: 70,5%
# - Probabiliade de não alteração: 29,5%
#
# Se trocar uma única carta, temos os seguintes resultados:
# - quantidade de jogos que melhoram valor da mão: 11
# - quantidade de jogos que não representam melhoria: 9
# - Probabilidade de melhora: 55%
# - Probabiliade de não alteração: 45%
#
# Veja o DocTest.
def calcula_probabilidades_par_troca_dois_e_um():
    """Calcula as probabilidades de melhoria da pontuação de uma mão, 
    com uma dupla, ao se trocar as duas cartas que não pertencem à dupla,
    ou uma carta que não pertence à dupla. Esses casos, se forem avaliados
    especificamente, não reduzem a genericidade da solução do problema:
    
    >>> calcula_probabilidades_par_troca_dois_e_um()
    {'dois': {'possibilidades_totais': 190, 'possibilidades_de_melhora': 134, 'possibilidades_de_nao_alteracao_ou_piora': 56, 'probabilidade_de_melhora': 0.7052631578947368, 'probabilidade_de_nao_alteracao_ou_piora': 0.29473684210526313}, 'um': {'possibilidades_totais': 20, 'possibilidades_de_melhora': 11, 'possibilidades_de_nao_alteracao_ou_piora': 9, 'probabilidade_de_melhora': 0.55, 'probabilidade_de_nao_alteracao_ou_piora': 0.45}}
    """
    # Lista de cartas com um par qualquer, sem perda de genericidade:
    cartas_mao = ["A", "A", "K", "Q", "J"]
    # Remove cartas que não pertencem à dupla, sem perda de genericidade:
    cartas_a_remover = ["K", "Q"]
    possibilidades_dois = calcula_possibilidades(cartas_mao, cartas_a_remover)
    
    # Agora remove apenas uma carta que não pertence à dupla, sem perda de genericidade:
    cartas_a_remover = ["K"]
    possibilidades_um = calcula_possibilidades(cartas_mao, cartas_a_remover)
    
    
    return { "dois": possibilidades_dois, "um": possibilidades_um }

#
# Questão 2 - d)
#
# O valor esperado da mão com as trocas é a média de todos os valores de todas
# as novas mãos possíveis.
#
def valor_medio_troca(mao, trocas):
    """Calcula o valor médio de uma mão, assumindo que as cartas em trocas serão trocadas.
    
    >>> valor_medio_troca(["A", "A", "K", "Q", "J"], ["K", "Q", "J"])
    2.6964912280701756
    
    >>> valor_medio_troca(["A", "A", "A", "Q", "J"], ["Q", "J"])
    4.910526315789474
    
    >>> valor_medio_troca(["A", "A", "A", "Q", "J"], ["Q"])
    4.1
    """
    possibilidades = possibilidades_da_mao(mao, trocas)
    soma_de_valores = 0
    numero_de_valores = 0
    for p in possibilidades:
        soma_de_valores += valor_mao(p)
        numero_de_valores += 1
    return float(soma_de_valores)/float(numero_de_valores)


doctest.testmod()

#
# A partir daqui são implementados os jogadores. Eles podem ser carregados
# de acordo com parâmetros de entrada do programa.
#

# Função de Suporte aos Jogadores:
def elemento_menos_numeroso(mao): # ** **
    """
    """# Cópia de segurança de mão:
    mao_ordenada = mao.copy()
    mao_ordenada.sort()
    contador = 0
    menor_elemento = mao_ordenada[0]
    menor_quantidade = len(mao_ordenada) + 100
    antigo_elemento = mao_ordenada[0]
    for elemento in mao_ordenada:
        if elemento == antigo_elemento:
            contador += 1
        else:
            if contador <= menor_quantidade:
                menor_elemento = antigo_elemento
                menor_quantidade = contador
            contador = 1
        antigo_elemento = elemento    
    if contador <= menor_quantidade:
        menor_elemento = antigo_elemento
        menor_quantidade = contador
    return menor_elemento

# Função de Suporte aos Jogadores:
def elemento_mais_numeroso(mao): # ** **
    """"
    """
    # Cópia de segurança de mão:
    mao_ordenada = mao.copy()
    mao_ordenada.sort()
    contador = 0
    maior_elemento = mao_ordenada[0]
    maior_quantidade = 0
    antigo_elemento = mao_ordenada[0]
    for elemento in mao_ordenada:
        if elemento == antigo_elemento:
            contador += 1
        else:
            if contador >= maior_quantidade:
                maior_elemento = antigo_elemento
                maior_quantidade = contador
            contador = 1
        antigo_elemento = elemento    
    if contador >= maior_quantidade:
        maior_elemento = antigo_elemento
        maior_quantidade = contador
    return maior_elemento

# Funções do Jogador Aleatório:
import doctest
def trocas_aleatorio(mao, trocas1=None):# ** ** 
    """ O jogador aleatório tem 50% de chance de trocar as cartas da mao por outras carta que possa favorecer 
    o jogo tendo no máximo 3 cartas permitida para a troca, contudo suas chance de desistencia também é de 50%.
         >>> trocas_aleatorio(["A","J","K","Q","Q"],["K","Q","J"])
         ['A', 'J', 'K']
         >>> trocas_aleatorio(["A","J","K","Q","Q"],["K"])
         ['J', 'K', 'Q']
    """
    trocar = []
    for c in mao:
        if random.random() >= 0.5:
            trocar.append(c)
            if len(trocar) >= 3:
                return trocar
doctest.testmod()

def desistir_aleatorio(mao_atual, mao_original, trocas_minhas, trocas_outro=None, segundo=False): # ** **
   return random.random() >= 0.5

# funções do Jogador Humano:
import doctest
def trocas_humano(mao, trocas1=None):
    """ O jogador humano mostra as cartas da sua mão e lhe é feito a pergunta de quais cartas de no máximo
    3 ele deseja trocar,ele digita as cartas e é impresso quais cartas ele digitou , caso passe da quantidade de carta delimitada, o jogo pede pra ele tentar novamente.
        >>> trocas_humano(["A","J","K","Q","Q"])
        ['A', 'J', 'Q']
    """
    mao_ordenada = mao.copy()
    mao_ordenada.sort()
    print("Você possui essa mão: {}".format("".join(mao_ordenada)))
    novas_cartas = ""
    repeat = True
    cartas_aceitaveis = set(mao)
    while repeat:
        novas_cartas = input("Quais você deseja trocar? (Digite até três cartas e aperte <Enter> no final): ")
        repeat = False
        if len(novas_cartas) > 3:
            repeat = True
        for c in novas_cartas:
            if not c.upper() in cartas_aceitaveis:
                repeat = True
        if repeat:
            print("Você pode trocar, no máximo, três cartas e essas cartas devem estar na sua mão. Tente novamente.")
            novas_cartas = ""
    return list(novas_cartas.upper())
doctest.testmod()

def desistir_humano(mao_atual, mao_original, trocas_minhas, trocas_outro=None, segundo=False): # ** ** 
    mao_ordenada = mao_atual.copy()
    mao_ordenada.sort()
    print("A sua mão atual é: {}".format("".join(mao_ordenada)))
    print("Atenção, o seu adversário trocou {} carta(s)!".format(trocas_outro))
    repeat = True
    resposta = None
    while repeat:
        resposta = input("Você deseja desistir? [S - para sim, N - para não]: ")
        print("Sua resposta é: [{}]".format(resposta))
        repeat = False
        if resposta.upper() != "S" and resposta.upper() != "N":
            print("Insira apenas S ou N, para dizer sim ou não. Tente novamente.")
            repeat = True
    if resposta.upper() == 'S':
        return True
    return False

# funções do Jogador Ganancioso:
import doctest
def trocas_ganancioso(mao, trocas1=None):
   """ ele sempre troca as cartas que não contribuem para o valor da mão. 
   Se uma mão não tem nem um par, ele troca as 3 menores.
    >>> trocas_ganancioso(["A","J","K","Q","Q"],["J","K"])
    ['K', 'J', 'A']
   """ 
   mao_desordenada = mao.copy()
   random.shuffle(mao_desordenada)
   return nao_contribui_max_3(mao_desordenada)
doctest.testmod()
def desistir_ganancioso(mao_atual, mao_original, trocas_minhas, trocas_outro=None, segundo=False):
  """ ele desiste se tem um par ou menos e é o primeiro jogador, e ele desiste
se tem não tem uma tripla e é o segundo jogador.
  """ 
  if segundo:
        if(valor_mao(mao_atual) < 3):
            return True
  else:
        if(valor_mao(mao_atual)) < 2:
            return True
  return False 

# funções do Jogador Cauteloso:
def trocas_cauteloso(mao, trocas1=None):
    return trocas_ganancioso(mao, trocas1)

def desistir_cauteloso(mao_atual, mao_original, trocas_minhas, trocas_outro=None, segundo=False):
    """ se o adversário trocou apenas uma carta, ele assume que o oponente tem ao menos uma quadra;
    se o adversário trocou apenas duas cartas, ele assume que o oponente tem uma tripla.
    """
    if trocas_outro == 1:
        if valor_mao(mao_atual) < 10:
            return True
    elif trocas_outro == 2:
        if valor_mao(mao_atual) < 3:
            return True
    return False
    
# funções do Jogador Blefe:
def trocas_blefe(mao, trocas1=None):
    """
    """
    carta_menos_numerosa = elemento_menos_numeroso(mao)
    if random.random() >= 0.5:
        return [carta_menos_numerosa]
    return []

def desistir_blefe(mao_atual, mao_original, trocas_minhas, trocas_outro=None, segundo=False):
    """ se o adversário trocou apenas uma carta, ele assume que o oponente tem ao menos uma quadra;
    se o adversário trocou apenas duas cartas, ele assume que o oponente tem uma tripla.
    """
    return desistir_ganancioso(mao_atual, mao_original, trocas_minhas, trocas_outro, segundo)

# funções do Jogador Burro:
def trocas_burro(mao, trocas1=None):
    """ O jogador Burro é o jogador que não sabe jogar, ele sempre trocas suas cartas independentemente
    de ser boa ou não ele as descartas, em relação aos outros jogadores ele nunca desiste mais, fatidicamente
    sempre perde.
    """
    mao_temporaria = mao.copy()
    trocas = list()
    repeat = True
    while repeat:
        trocas.append(elemento_mais_numeroso(mao_temporaria))
        mao_temporaria = diferenca_de_lista(mao_temporaria, trocas)
        if random.random() >= 0.4:
            repeat = False
        if len(trocas) >= 3:
            repeat = False
    return trocas

def desistir_burro(mao_atual, mao_original, trocas_minhas, trocas_outro=None, segundo=False):
    if valor_mao(mao_atual) <= valor_mao(mao_original):
        return False
    return True

# Funções do Jogo:
def rodada(estado, tipo="completa"):
    if not tipo in ["estrategica", "completa", "rapida"]:
        raise TipoRodadaErrado
        
    if estado["rodada"] > 5:
        # Todas as rodadas já foram executadas. Finalizando.
        return False
    
    print("Rodada {}:".format(estado["rodada"]))
    print("Jogador 1: ", estado["jogador1"]["nome"])
    print("Jogador 2: ", estado["jogador2"]["nome"])
    print()
    
    # Inicia as cartas, repondo o baralho e o embaralhando:
    print("Embaralhando as cartas")
    estado["cartas_restantes"] = [
        "A", "A", "A", "A", "A",
        "7", "7", "7", "7", "7",
        "K", "K", "K", "K", "K",
        "Q", "Q", "Q", "Q", "Q",
        "J", "J", "J", "J", "J"]
    random.shuffle(estado["cartas_restantes"])
    
    # Inicia a rodada dando cinco cartas aleatórias para cada jogador:
    print("Distribuindo as cartas")
    estado["jogador1"]["mao_atual"] = []
    estado["jogador2"]["mao_atual"] = []
    for i in range(5):
        estado["jogador1"]["mao_atual"].append(estado["cartas_restantes"].pop())
        estado["jogador2"]["mao_atual"].append(estado["cartas_restantes"].pop())
    
    if tipo in ["estrategica", "completa"]:
        print("Jogador 1 está verificando as suas trocas")
        cartas_a_trocar1 = estado["jogador1"]["trocas"](estado["jogador1"]["mao_atual"])
        mao_original1 = estado["jogador1"]["mao_atual"]
        mao_atual1 = diferenca_de_lista(mao_original1, cartas_a_trocar1)
        for i in cartas_a_trocar1:
            # Substitui a carta antiga na mão atual:
            mao_atual1.append(estado["cartas_restantes"].pop())
            # Retorna a carta antiga ao baralho:
            estado["cartas_restantes"].insert(0, i)
        print("Jogador 1 trocou {} carta(s)".format(len(cartas_a_trocar1)))
        
        print("Jogador 2 está verificando as suas trocas")
        cartas_a_trocar2 = estado["jogador2"]["trocas"](estado["jogador2"]["mao_atual"], len(cartas_a_trocar1))
        
        mao_original2 = estado["jogador2"]["mao_atual"]
        mao_atual2 = diferenca_de_lista(mao_original2, cartas_a_trocar2)
        for i in cartas_a_trocar2:
            # Substitui a carta antiga na mão atual:
            mao_atual2.append(estado["cartas_restantes"].pop())
            # Retorna a carta antiga ao baralho:
            estado["cartas_restantes"].insert(0, i)
        print("Jogador 2 trocou {} carta(s)".format(len(cartas_a_trocar2)))
            
        estado["jogador1"]["mao_atual"] = mao_atual1
        estado["jogador2"]["mao_atual"] = mao_atual2
        
        if tipo == "completa":
            print("Jogador 1 está verificando se desiste")
            if estado["jogador1"]["desistir"](mao_atual1, mao_original1, len(cartas_a_trocar1), len(cartas_a_trocar2)):
                print("Jogador 1 desistiu. Jogador 2 ganhou pontos da rodada.")
                estado["jogador1"]["pontos"] += 1
                # Continua jogando
                return True
            
            print("Jogador 2 está verificando se desiste")
            if estado["jogador2"]["desistir"](mao_atual2, mao_original2, len(cartas_a_trocar2), len(cartas_a_trocar1), True):
                print("Jogador 2 desistiu. Jogador 1 ganhou pontos da rodada.")
                estado["jogador2"]["pontos"] += 1
                # Continua jogando
                return True
    
    print("Os jogadores baixaram as cartas!")
    estado["jogador1"]["mao_atual"].sort()
    estado["jogador2"]["mao_atual"].sort()
    print("Jogador 1: ", "".join(estado["jogador1"]["mao_atual"]))
    print("Jogador 2: ", "".join(estado["jogador2"]["mao_atual"]))
    
    pontos1 = valor_mao(estado["jogador1"]["mao_atual"])
    pontos2 = valor_mao(estado["jogador2"]["mao_atual"])
    
    if pontos1 == pontos2:
        pontos = float(pontos1)/2.0
        print("A rodada empatou! Os dois jogadores ganharam {} pontos!".format(pontos))
        estado["jogador1"]["pontos"] += pontos
        estado["jogador2"]["pontos"] += pontos
    elif pontos1 > pontos2:
        print("A rodada foi ganha pelo jogador 1 que ganhou {} pontos!".format(pontos1))
        estado["jogador1"]["pontos"] += pontos1
    else:
        print("A rodada foi ganha pelo jogador 2 que ganhou {} pontos!".format(pontos2))
        estado["jogador2"]["pontos"] += pontos2
    # Continua jogando
    return True

# Função temporária para estruturar o jogo.
def jogo(tipo="completa", tipo1="aleatorio", tipo2="aleatorio"):
    jogador1 = {}
    jogador2 = {}
    
    if tipo1 == "aleatorio":
        jogador1 = {"nome": "Aleatorio 1", "trocas": trocas_aleatorio, 
                    "desistir": desistir_aleatorio, "mao_atual": [], 
                    "pontos": 0}
    elif tipo1 == "humano":
        jogador1 = {"nome": "Humano", "trocas": trocas_humano, 
                    "desistir": desistir_humano, "mao_atual": [], 
                    "pontos": 0}
    elif tipo1 == "ganancioso":
        jogador1 = {"nome": "Ganancioso 1", "trocas": trocas_ganancioso, 
                    "desistir": desistir_ganancioso, "mao_atual": [], 
                    "pontos": 0}
    elif tipo1 == "cauteloso":
        jogador1 = {"nome": "Cauteloso 1", "trocas": trocas_cauteloso, 
                    "desistir": desistir_cauteloso, "mao_atual": [], 
                    "pontos": 0}
    elif tipo1 == "blefe":
        jogador1 = {"nome": "Blefe 1", "trocas": trocas_blefe, 
                    "desistir": desistir_blefe, "mao_atual": [], 
                    "pontos": 0}
    elif tipo1 == "burro":
        jogador1 = {"nome": "Burro 1", "trocas": trocas_burro, 
                    "desistir": desistir_burro, "mao_atual": [], 
                    "pontos": 0}
    else:
        raise TipoJogador1Errado
    
    if tipo2 == "aleatorio":
        jogador2 = {"nome": "Aleatorio 2", "trocas": trocas_aleatorio, 
                    "desistir": desistir_aleatorio, "mao_atual": [], 
                    "pontos": 0}
    elif tipo2 == "humano":
        if tipo1 == "humano":
            raise DoisTiposJogadoresHumanosÉErrado
        jogador2 = {"nome": "Humano", "trocas": trocas_humano, 
                    "desistir": desistir_humano, "mao_atual": [], 
                    "pontos": 0}
    elif tipo2 == "ganancioso":
        jogador2 = {"nome": "Ganancioso 2", "trocas": trocas_ganancioso, 
                    "desistir": desistir_ganancioso, "mao_atual": [], 
                    "pontos": 0}
    elif tipo2 == "cauteloso":
        jogador2 = {"nome": "Cauteloso 2", "trocas": trocas_cauteloso, 
                    "desistir": desistir_cauteloso, "mao_atual": [], 
                    "pontos": 0}
    elif tipo2 == "blefe":
        jogador2 = {"nome": "Blefe 2", "trocas": trocas_blefe, 
                    "desistir": desistir_blefe, "mao_atual": [], 
                    "pontos": 0}
    elif tipo2 == "burro":
        jogador2 = {"nome": "Burro 2", "trocas": trocas_burro, 
                    "desistir": desistir_burro, "mao_atual": [], 
                    "pontos": 0}
    else:
        raise TipoJogador2Errado
        
    # Inicia o estado do jogo:
    estado = {
        "jogador1": jogador1,
        "jogador2": jogador2,
        "vencedor": None,
        "rodada": 1,
        "cartas_restantes": []
        }
    
    while rodada(estado, tipo): 
        estado["rodada"] += 1
        print("\n")
    
    if estado["jogador1"]["pontos"] == estado["jogador2"]["pontos"]:
        print("O jogo empatou, não houve vencedores! Pontos de cada jogador: {}.".format(estado["jogador2"]["pontos"]))
    elif estado["jogador1"]["pontos"] > estado["jogador2"]["pontos"]:
        print("O jogador 1 venceu com {} ponto(s)! O jogador 2 teve apenas {} ponto(s). Parabéns Jogador 1!".format(estado["jogador1"]["pontos"] , estado["jogador2"]["pontos"] ))
    else:
        print("O jogador 2 venceu com {} ponto(s)! O jogador 1 teve apenas {} ponto(s). Parabéns Jogador 2!".format(estado["jogador2"]["pontos"] , estado["jogador1"]["pontos"] ))

#
# Esse é a função principal, utilizada para testar os jogadores a partir da
# linha de comando.
#
def main():
    pass

if __name__ == "__main__":
    main()
    


# Uses draw() to take cards from a list of cards
#      points() to calculate the number of points in a given hand
#      validate_change() to make sure the players' moves are valid

def validate_change(hand, cards):
    # A verdadeira função é mais complexa :-)
    return True

def round(deck, player1, player2):
    p1_change, p1_quit = player1
    p2_change, p2_quit = player2

    remaining = deck.copy()
    hand1 = draw(remaining, 5)
    hand2 = draw(remaining, 5)

    hand1_orig = hand1.copy()
    hand2_orig = hand2.copy()

    c1 = p1_change(hand1.copy())
    if not validate_change(hand1, c1):
        print(f"""Player 1: Invalid move!
Hand {hand1} does not contain all cards to change in {c1}""")
        return (0, 100)

    c2 = p2_change(hand2.copy(), len(c1))
    if not validate_change(hand2, c2):
        print(f"""Player 2: Invalid move!
Hand {hand2} does not contain all cards to change in {c2}""")
        return (100, 0)

    hand1 += draw(remaining, len(c1))
    hand2 += draw(remaining, len(c2))

    if p1_quit(hand1.copy(), hand1_orig.copy(), c1.copy(),
            trocas_outro=len(c2)):
        return (0, 2)
    if p2_quit(hand2.copy(), hand2_orig.copy(), c2.copy(),
            trocas_outro=len(c1), segundo=True):
        return (3, 0)

    points1 = points(hand1)
    points2 = points(hand2)

    if points1 == points2:
        return (points1/2, points2/2)
    if points1 > points2:
        return (points1, 0)
    return (0, points2)

