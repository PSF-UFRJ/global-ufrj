#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:03:54 2022

@author: paulo
"""

import doctest
import random

#
# Questão 1: Sendo d um dicionário, o bloco de código apresentado inverte 
# chaves e valores desse dicionário d. Se houver valores repetidos, ele, no
# novo dicionário, apresentará como uma única chave, apontando para a última
# chave apresentada no dicionário d original.
#
# Exemplos: 
#    - Se d = {1: 2, 2: 4, 3: 9}, o resultante será: {2: 1, 4: 2, 9: 3}
#    - Se d = {1: 2, 2: 4, 7: 2, 3: 9}, o resultante será: {2: 7, 4: 2, 9: 3}
#

#
# Questão 2:
#
def nao_quadrados(l, l2):
    """Função que retorna os elementos de l cujos quadrados não estão em l2
    >>> nao_quadrados([1,2,3,4], [1,4,16,25])
    [3]
    
    >>> nao_quadrados([1,2,3,4], [4,16,25])
    [1, 3]
    
    >>> nao_quadrados([1,2,3,4], [1,9,4,16,25])
    []
    """
    s = set(l)
    s2 = set(l2)
    return [x for x in s if not(x**2 in s2)]

#
# Questão 3:
#
def comprimento_da_cadeia(d, k):
    """Função que retorna o tamanho da cadeia do dicionário d, dado a chave 
    inicial k. A cadeia existe quando o valor de uma chave também é uma chave
    no mesmo dicionário. Se a cadeia for infinita (loop), a função retorna -1.
    
    >>> comprimento_da_cadeia({1:2, 2:3, 3:4, 5: 6, 6: 7, 8:8}, 1)
    3

    >>> comprimento_da_cadeia({1:2, 2:3, 3:4, 5: 6, 6: 7, 8:8}, 2)
    2

    >>> comprimento_da_cadeia({1:2, 2:3, 3:4, 5: 6, 6: 7, 8:8}, 3)
    1

    >>> comprimento_da_cadeia({1:2, 2:3, 3:4, 5: 6, 6: 7, 8:8}, 4)
    0

    >>> comprimento_da_cadeia({1:2, 2:3, 3:4, 5: 6, 6: 7, 8:8}, 5)
    2

    >>> comprimento_da_cadeia({1:2, 2:3, 3:4, 5: 6, 6: 7, 8:8}, 6)
    1

    >>> comprimento_da_cadeia({1:2, 2:3, 3:4, 5: 6, 6: 7, 8:8}, 7)
    0

    >>> comprimento_da_cadeia({1:2, 2:3, 3:4, 5: 6, 6: 7, 8: 9, 9: 8}, 8)
    inf
    
    >>> comprimento_da_cadeia({1:2, 2:3, 3:4, 5: 6, 6: 7, 8: 9, 9: 8}, 9)
    inf
    """
    keys = set(d.keys())
    prevs = set()
    count = 0
    index = k
    prevs.add(index)
    while index in keys:
        count += 1
        index = d[index]
        if index in prevs:
            return float('inf')
        prevs.add(index)
    return count

doctest.testmod()

#
# Questão 4: Implementado acima na função comprimento_da_cadeia.
#

#
# Questão 5:
#
def tempo_de_espera(n=100):
    """Retorna o número de vezes que um dado honesto deve ser jogado até que
    a soma de todos os resultados das jogadas seja igual ou maior ao n passado 
    como parâmetro.
    
    >>> tempo_de_espera() < 100
    True
    
    >>> tempo_de_espera(7) > 1
    True
    
    >>> tempo_de_espera(5) >= 1
    True
    
    >>> tempo_de_espera(5) <= 5
    True
    """
    count = 0
    total = 0
    while total < n:
        count += 1
        total += random.randint(1, 6)
    return count

#
# Questão 6:
#
def histograma(n, repeticoes=1000):
    """Apresenta um dicionário com o número de vezes que um determinado evento
    de "tempo_de_espera" ocorreu. As chaves são o número de sorteios 
    necessários a cada experimento, e os valores são o número de experimentos 
    em que realizamos estes sorteios"""
    hist = dict()
    for r in range(repeticoes):
        t = tempo_de_espera(n)
        if t in hist.keys():
            hist[t] += 1
        else:
            hist[t] = 1
    return hist

#
# Questão 7:
#
def imprime_histograma(n, repeticoes=1000):
    """Imprime tabela dos dados de "histograma", apresentando na primeira coluna
    o numero de vezes que um determinado evento de "tempo_de_espera" ocorreu e,
    na segunda coluna, o número de sorteios necessários àquele experimento."""
    hist = histograma(n, repeticoes=1000)
    t_num = "Jogadas"
    t_valor = "Número de Eventos"
    c_num = len(t_num)
    c_valor = len(t_valor)
    for i in hist.keys():
        num = len(str(i))
        val = len(str(hist[i]))
        if num > c_num:
            c_num = num
        if val > c_valor:
            c_valor = val
    
    k = list(hist.keys())
    k.sort()
    print(("\N{BOX DRAWINGS LIGHT VERTICAL} {:>" + str(c_num) +
           "} \N{BOX DRAWINGS LIGHT VERTICAL}  {:>"+ str(c_valor) +
           "} \N{BOX DRAWINGS LIGHT VERTICAL} ").format(t_num, t_valor))
    for i in k:
        print(("\N{BOX DRAWINGS LIGHT VERTICAL} {:>" + str(c_num) +
               "} \N{BOX DRAWINGS LIGHT VERTICAL}  {:>"+ str(c_valor) +
               "} \N{BOX DRAWINGS LIGHT VERTICAL} ").format(i, hist[i]))

#
# Questão 8: O código poderia funcionar para uma lista, se os valores da lista
# forem limitados aos valores dos indices da lista. Por exemplo, todas as listas
# a seguir permitem o funcionamento adequado do código da primeira questão:
#
# d = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# {d[k]:k for k in d}
# Out[14]: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
#
# d = [8, 7, 6, 5, 4, 3, 2, 1, 0]
# {d[k]:k for k in d}
# Out[15]: {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}
#
# d = [5, 3, 6, 2, 1, 0, 7, 4, 8]
# {d[k]:k for k in d}
# Out[16]: {0: 5, 2: 3, 7: 6, 6: 2, 3: 1, 5: 0, 4: 7, 1: 4, 8: 8}
#
# d = [0, 6, 8, 4, 2, 1, 7, 5, 3]
# {d[k]:k for k in d}
# Out[17]: {0: 0, 7: 6, 3: 8, 2: 4, 8: 2, 6: 1, 5: 7, 1: 5, 4: 3}
#
# Basta existir um valor que não represente um indice dentro da lista, que o código
# não vai funcionar. Na lista abaixo, não há o valor para o índice 0 (Zero):
# d = [1,2,3,4,5,6,7,8]
# 
# {d[k]:k for k in d}
# Traceback (most recent call last):
#
#  File "/tmp/ipykernel_14767/2553462595.py", line 1, in <cell line: 1>
#    {d[k]:k for k in d}
#
#  File "/tmp/ipykernel_14767/2553462595.py", line 1, in <dictcomp>
#    {d[k]:k for k in d}
#
# IndexError: list index out of range
# E o código não funciona.
    