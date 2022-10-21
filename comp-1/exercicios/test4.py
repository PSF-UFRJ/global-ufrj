#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 11:18:13 2022

@author: paulo
"""
import doctest

#
# Questão 1/2/3:
#
def soma_e_media(lista_entrada, d=2, r=0):
    """Calcula e retorna a soma e a média dos números pares de uma lista:
    >>> soma_e_media([1,2,3,4])
    (6, 3.0)
    
    Calcula e retorna a soma e a média apenas dos números pares de uma lista:
    >>> soma_e_media([2,3,4,6,8,9,10,12,14,15], 2, 0)
    (56, 8.0)
    
    Calcula e retorna a soma e a média apenas dos números que, dividos por dois,
    restam 1 (números impares):
    >>> soma_e_media([2,3,4,6,8,9,10,12,14,15], 2, 1)
    (27, 9.0)
    
    Calcula e retorna a soma e a média apenas dos números que, divididos por quatro,
    restam 3:
    >>> soma_e_media([2,3,4,6,8,9,10,12,14,15], 4, 3)
    (18, 9.0)
    
    Calcula e retorna a soma e a média apenas dos números que, divididos por quatro,
    restam 3, mas usando uma tupla.
    >>> soma_e_media((2,3,4,6,8,9,10,12,14,15), 4, 3)
    (18, 9.0)
    
    Calcula e retorna a soma e a média de números pares de 1 a 10, mas utilizando
    um range.
    >>> soma_e_media(range(1,11))
    (30, 6.0)
    """
    l = [item for item in lista_entrada if item % d == r]
    comprimento = len(l)
    soma = 0
    for i in l:
        soma += i
    return soma, soma/comprimento
    
#
# Questão 4: A função acima já funciona com tuplas e ranges. Basta ver os dois
# últimos exemplos do DocTest da função anterior.
#

#
# Questão 5: A função já foi originalmente implementada utilizando um 
# list-comprehension. Veja acima.
#

#
# Questão 6: É necessário usar uma função que itere na lista para poder medir
# a performance. Essa função vai ter suporte para ranges e tuplas, também.
#
def soma_e_media2(lista_entrada, d=2, r=0):
    """Calcula e retorna a soma e a média dos números pares de uma lista:
    >>> soma_e_media2([1,2,3,4])
    (6, 3.0)
    
    Calcula e retorna a soma e a média apenas dos números pares de uma lista:
    >>> soma_e_media2([2,3,4,6,8,9,10,12,14,15], 2, 0)
    (56, 8.0)
    
    Calcula e retorna a soma e a média apenas dos números que, dividos por dois,
    restam 1 (números impares):
    >>> soma_e_media2([2,3,4,6,8,9,10,12,14,15], 2, 1)
    (27, 9.0)
    
    Calcula e retorna a soma e a média apenas dos números que, divididos por quatro,
    restam 3:
    >>> soma_e_media2([2,3,4,6,8,9,10,12,14,15], 4, 3)
    (18, 9.0)
    
    Calcula e retorna a soma e a média apenas dos números que, divididos por quatro,
    restam 3, mas usando uma tupla.
    >>> soma_e_media2((2,3,4,6,8,9,10,12,14,15), 4, 3)
    (18, 9.0)
    
    Calcula e retorna a soma e a média de números pares de 1 a 10, mas utilizando
    um range.
    >>> soma_e_media2(range(1,11))
    (30, 6.0)
    """
    comprimento = 0
    soma = 0
    for l in lista_entrada:
        if l % d == r:
            soma = soma + l
            comprimento = comprimento + 1
    return soma, soma/comprimento

#
# Segundo as implementações acima, a diferença de tempo não parece ser relevante,
# mas a segunda implementação (não criando a lista), parece consistentemente mais
# lenta, ainda que marginalmente. Provavelmente o Python otimiza a criação das
# listas ou o conjunto de chamadas no loop representa um peso computacional maior
# do que o cálculo do comprimento direto da lista ou o list-comprehension.
#
# Seguem os dados de tempo:
#    
#  %time soma_e_media(range(1,101))
#  CPU times: user 15 µs, sys: 1 µs, total: 16 µs
#  Wall time: 20.5 µs
#  Out[33]: (2550, 51.0)
#
#  %time soma_e_media2(range(1,101))
#  CPU times: user 12 µs, sys: 1 µs, total: 13 µs
#  Wall time: 15.3 µs
#  Out[34]: (2550, 51.0)
#
#  %time soma_e_media(range(1,1001))
#  CPU times: user 83 µs, sys: 9 µs, total: 92 µs
#  Wall time: 94.4 µs
#  Out[35]: (250500, 501.0)
#
#  %time soma_e_media2(range(1,1001))
#  CPU times: user 117 µs, sys: 12 µs, total: 129 µs
#  Wall time: 133 µs
#  Out[36]: (250500, 501.0)
#
#  %time soma_e_media(range(1,10001))
#  CPU times: user 825 µs, sys: 89 µs, total: 914 µs
#  Wall time: 918 µs
#  Out[37]: (25005000, 5001.0)
#
#  %time soma_e_media2(range(1,10001))
#  CPU times: user 844 µs, sys: 92 µs, total: 936 µs
#  Wall time: 938 µs
#  Out[38]: (25005000, 5001.0)
#
#  %time soma_e_media(range(1,100001))
#  CPU times: user 1.19 ms, sys: 8.21 ms, total: 9.4 ms
#  Wall time: 9.31 ms
#  Out[39]: (2500050000, 50001.0)
#
#  %time soma_e_media2(range(1,100001))
#  CPU times: user 9.83 ms, sys: 0 ns, total: 9.83 ms
#  Wall time: 9.8 ms
#  Out[40]: (2500050000, 50001.0)
#
#  %time soma_e_media(range(1,1000001))
#  CPU times: user 84.8 ms, sys: 4.04 ms, total: 88.9 ms
#  Wall time: 88.4 ms
#  Out[41]: (250000500000, 500001.0)
#
#  %time soma_e_media2(range(1,1000001))
#  CPU times: user 91.4 ms, sys: 0 ns, total: 91.4 ms
#  Wall time: 90.8 ms
#  Out[42]: (250000500000, 500001.0)  
#

#
# Questão 7:
#
def soma_pesos(l, pesos):
    """Soma os itens dados em "l", segundo os pesos dados em "pesos":
    
    Resultado de 1*1 + 1*1 * 1*1:
    >>> soma_pesos([1,1,1],[1,1,1])
    3
    
    Resultado de 1*1 + 2*2 + 3*3:
    >>> soma_pesos([1,2,3], [1,2,3])
    14
    
    Resultado de 2*7 + 3*6 + 4*5 + 5*4:
    >>> soma_pesos([2,3,4,5],[7,6,5,4])
    72
    """
    if len(l) != len(pesos):
        return
    if (not type(l) is list) or (not type(pesos) is list):
        return
    length = len(l)
    r = [l[i]*pesos[i] for i in range(0, length)]
    soma = 0
    for v in r:
        soma = soma + v
    return soma

#
# Questão 8 - a:
#
def junta_lista(l1, l2):
    """Une as listas dadas como uma lista de duplas dos elementos da primeira
    lista pareada com os elementos da segunda lista.
    
    >>> junta_lista([1,2,3,4,5,6], [2,4,6,8,10,12])
    [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12)]
    """
    if len(l1) != len(l2):
        return
    if (not type(l1) is list) or (not type(l2) is list):
        return
    length = len(l1)
    return [(l1[i], l2[i]) for i in range(length)]

#
# Questão 8 - b:
#
def separa_lista(l):
    """Separa lista de duplas à lista do indexado e a do índice.
    
    >>> separa_lista([(1,2),(3,4),(5,6),(7,8)])
    [[1, 3, 5, 7], [2, 4, 6, 8]]
    
    """
    indices = list()
    indexados = list()
    for item in l:
        indices.append(item[0])
        indexados.append(item[1])
    return [indices, indexados]

#
# Questão 8 - b - implementação alternativa
#
def separa_lista2(l):
    """Separa lista de duplas à lista do indexado e a do índice.
    
    >>> separa_lista2([(1,2),(3,4),(5,6),(7,8)])
    [[1, 3, 5, 7], [2, 4, 6, 8]]
    
    """
    indices = [item[0] for item in l]
    indexados = [item[1] for item in l]
    return [indices, indexados]

doctest.testmod()

