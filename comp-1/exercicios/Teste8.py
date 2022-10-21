#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:07:41 2022

@author: paulo
"""
import doctest

#
# Questão 1:
#        
def pares(gerador):
    """Dado o parâmetro gerador, retorna os elementos de índice par desse gerador.
    >>> for i in pares((i for i in [0,100,200,300,400,500,600])): print(i)
    0
    200
    400
    600
    """
    i = 0
    n = next(gerador, None)
    while not n is None:
        if i % 2 == 0:
            yield n
        i += 1
        n = next(gerador, None)

#
# Questão 2:
#
def comprimentos(nome_do_arquivo):
    """Retorna um gerador com o tamanho das linhas do arquivo dado por nome_do_arquivo.
    Cada elemento do gerador é o tamanho de uma linha do arquivo.
    
    >>> list(comprimentos("T8_q2_arq.txt"))
    [23, 15, 13, 22, 38, 0]
    """
    with open(nome_do_arquivo, mode="r") as f:
        for line in f:
            comprimento = len(line)
            if comprimento > 0 and line[-1] == '\n':
                comprimento -= 1
            yield comprimento
            
#
# Questão 3:
#
def dois_maiores(conj):
    """Retorna, como uma tupla, os dois maiores elementos de um conjunto:
    >>> dois_maiores([1,2,3,2,3,4,53,5,56,4,3,2,2,3,91])
    (91, 56)
    
    >>> dois_maiores(set([1,2,3,2,3,4,53,5,56,4,3,2,2,3,91]))
    (91, 56)
    
    >>> dois_maiores(set([1]))
    (1,)
    
    >>> dois_maiores(set([]))
    ()
    """
    # Garante que conj é um conjunto:
    conjunto_de_seguranca = set(conj)
    conjunto = list(conjunto_de_seguranca)
    conjunto.sort()
    conjunto.reverse()
    tamanho = len(conjunto)
    if tamanho > 1:
        return (conjunto[0],conjunto[1])
    elif tamanho == 1:
        return (conjunto[0],)
    else:
        return tuple()

#
# Questão 4:
#
def maiores(conj, k=1):
    """Retorna, como uma tupla, os k maiores elementos de um conjunto:
    >>> maiores([5, 3, 2, 6, 1, 7, 4])
    (7,)
    
    >>> maiores([5, 3, 2, 6, 1, 7, 4], 2)
    (7, 6)
    
    >>> maiores([5, 3, 2, 6, 1, 7, 4], 3)
    (7, 6, 5)
    
    >>> maiores([5, 3, 2, 6, 1, 7, 4], 10)
    (7, 6, 5, 4, 3, 2, 1)
    """
    conjunto_de_seguranca = set(conj)
    conjunto_retorno = set()
    for i in range(k):
        if len(conjunto_de_seguranca) > 0:
            m = max(conjunto_de_seguranca)
            conjunto_retorno.add(m)
            conjunto_de_seguranca.remove(m)
    lista_retorno = list(conjunto_retorno)
    lista_retorno.sort()
    lista_retorno.reverse()
    return tuple(lista_retorno)

#
# Questão 5:
#
def maiores_recur(conj, k=1):
    """Implementação recursiva de maiores, definida acima.
    Retorna, como uma tupla, os k maiores elementos de um conjunto:
    >>> maiores_recur([5, 3, 2, 6, 1, 7, 4])
    (7,)

    >>> maiores_recur([5, 3, 2, 6, 1, 7, 4], 2)
    (7, 6)

    >>> maiores_recur([5, 3, 2, 6, 1, 7, 4], 3)
    (7, 6, 5)

    >>> maiores_recur([5, 3, 2, 6, 1, 7, 4], 10)
    (7, 6, 5, 4, 3, 2, 1)
    """
    conjunto_de_seguranca = set(conj)
    if k < 1 or len(conjunto_de_seguranca) < 1:
        return ()
    m = max(conjunto_de_seguranca)
    conjunto_de_seguranca.remove(m)
    return (m,) + maiores_recur(conjunto_de_seguranca, k-1)
        
#
# Questão 6:
#
def nome_e_número(linha):
    """Verifica se o valor passado em linha corresponde a um nome e um número:
    >>> nome_e_número("Paulo Roberto 123456")
    True
    
    >>> nome_e_número("Paulo 123 Roberto 456")
    False
    
    >>> nome_e_número("Josefina Pao e Vinho 4445556766")
    True
    """
    linha_lista = linha.split(" ")
    if len(linha_lista) < 2:
        return False
    numero = linha_lista[-1]
    nome = linha_lista[:-1]
    return numero.isnumeric() and "".join(nome).isalpha()

#
# Questão 7:
#
def união(d1, d2):
    """Une dois dicionarios:
    >>> união({"1": "a", "2": "b", "3": "c"}, {"a":"1", "b":"2", "c":"3"})
    {'1': 'a', '2': 'b', '3': 'c', 'a': '1', 'b': '2', 'c': '3'}
    
    >>> união({"1": "a", "2": "b", "3": "c"}, {"a":"1", "b":"2", "c":"3", "1": "d"})
    {'1': ('a', 'd'), '2': 'b', '3': 'c', 'a': '1', 'b': '2', 'c': '3'}
    """
    novo_dict = {}
    for k in d1.keys():
        novo_dict[k] = d1[k]
    for l in d2.keys():
        if l in novo_dict:
            novo_dict[l] = (novo_dict[l], d2[l])
        else:
            novo_dict[l] = d2[l] 
    return novo_dict
doctest.testmod()
    