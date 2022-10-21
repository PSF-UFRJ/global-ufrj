#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:18:07 2022

@author: paulo
"""
import doctest

#
# Questão 1 - a:
#
def proximo_collatz(n):
    """Retorna o número seguinte da sequência de Collatz, dado que o número
    inicial é dado por n:
    
    >>> proximo_collatz(1)
    4
    
    >>> proximo_collatz(2)
    1
    
    >>> proximo_collatz(3)
    10
    """
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n + 1

#
# Questão 1 - b:
#
def comprimento_collatz(n):
    """Retorna estritamente o número de elementos da sequencia de collatz
    entre um dado n e o próximo valor 1 subsequente.
    
    Para sequencia de collatz de 45:
    [45, 136, 68, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    >>> comprimento_collatz(45)
    15
    
    Para a sequencia de collatz de 8:
    [8, 4, 2, 1]
    >>> comprimento_collatz(8)
    2
    
    Para a sequencia de collatz de 1:
    [1, 4, 2, 1]
    >>> comprimento_collatz(1)
    2
    
    Para a sequencia de collatz de 3:
    [3, 10, 5, 16, 8, 4, 2, 1]
    >>> comprimento_collatz(3)
    6
    
    Para a sequencia de collatz de 0:
    [0, 0, 0, 0, ...]
    >>> comprimento_collatz(0)
    inf
    """
    if n == 0:
        return float("Inf")
    contador = 0
    valor_proximo_collatz = proximo_collatz(n)
    while valor_proximo_collatz != 1:
        valor_proximo_collatz = proximo_collatz(valor_proximo_collatz)
        contador += 1
    return contador

#
# Questão 2 - a:
#
def mediana(lista):
    """Retorna o valor mediano para os elementos de uma lista data. 
    Apenas o valor da mediana, se a lista tiver um número ímpar de elementos, ou uma
    tupla com os dois valores centrais, se a lista tiver um número par de elementos.
    
    >>> mediana([2,3,1,4])
    (2, 3)
    
    >>> mediana([5,2,1,4,3])
    3
    
    >>> mediana([2,4,6,8,10])
    6
    
    >>> mediana([2,4,6,8,10,12])
    (6, 8)
    """
    comprimento = len(lista)
    if comprimento == 0:
        return None
    lista_ordenada = lista.copy()
    lista_ordenada.sort()
    meio = int(comprimento/2)
    if comprimento % 2 == 0:
        return (lista_ordenada[meio-1], lista_ordenada[meio])
    else:
        return lista_ordenada[meio]

#
# Questão 2 - b:
#
def k_mediana(lista, k):
    """Calcula a k mediana de uma lista, retornando os k números centrais de uma lista,
    de forma que existam n números menores que o valor mínimo da lista e a mesma quantidade
    de n números maiores que o maior valor da lista.
    
    >>> k_mediana([1,2,3,4,5,6,8,7], 8)
    (1, 2, 3, 4, 5, 6, 7, 8)
    
    >>> k_mediana([1,2,3,4,5,6,7], 3)
    (3, 4, 5)
    
    >>> k_mediana([1,3,2,4,5,7,6], 1)
    (4, 4)
    """
    comprimento = len(lista)
    if comprimento < k:
        return None
    if (comprimento - k) % 2 != 0:
        return None
    lista_ordenada = lista.copy()
    lista_ordenada.sort()
    n = int((comprimento - k)/2)
    sublista = lista_ordenada[n:(comprimento-n)]
    if len(sublista) == 1:
        return (sublista[0],sublista[0])
    return tuple(sublista)

#
# Questão 3 - a:
#
def grupos(nome_do_arquivo):
    """Carrega grupos de alunos a partir de arquivo organizado linha a linha como <nome> <numero do grupo>.
    
    >>> grupos("grupos_lista.txt")
    [('Andrea Beltrao', 'Juca de Oliveira', 'Marieta Severo', 'Paulo Silva Filho'), ('José Silva', 'Vera Fischer'), ('Alberto de Oliveira', 'Beth Carvalho', 'Felipe Neto', 'Thayla Ayalla'), ('Aretha Franklin', 'Luís Fernando Guimaraes', 'Tony Ramos')]
    """
    with open(nome_do_arquivo, "r") as f:
        grupos = dict()
        for nome_grupo in f:
            if nome_grupo[-1] == '\n':
                nome_grupo = nome_grupo[:-1]
                
            nome_grupo
            lista_elementos = nome_grupo.split(" ")
            grupo = int(lista_elementos[-1])
            nome = " ".join(lista_elementos[:-1])
            if grupo in grupos:
                grupos[grupo].append(nome)
            else:
                grupos[grupo] = list()
                grupos[grupo].append(nome)
                chaves_ordenadas = list(grupos.keys())
                chaves_ordenadas.sort()
        
        for k in grupos:
            grupos[k].sort()
        
        return [tuple(grupos[k]) for k in chaves_ordenadas]

#
# Questão 3 - b:
#
def tabela_grupos(lista):
    """Formata tabela de grupos apresentados no parametro lista, dado.
    >>> tabela_grupos([('Andrea Beltrao', 'Juca de Oliveira', 'Marieta Severo', 'Paulo Silva Filho'), ('José Silva', 'Vera Fischer'), ('Alberto de Oliveira', 'Beth Carvalho', 'Felipe Neto', 'Thayla Ayalla'), ('Aretha Franklin', 'Luís Fernando Guimaraes', 'Tony Ramos')])
      1: │ Andrea Beltrao       │ Juca de Oliveira         │ Marieta Severo  │ Paulo Silva Filho  │ 
      2: │ José Silva           │ Vera Fischer             │                 │                    │ 
      3: │ Alberto de Oliveira  │ Beth Carvalho            │ Felipe Neto     │ Thayla Ayalla      │ 
      4: │ Aretha Franklin      │ Luís Fernando Guimaraes  │ Tony Ramos      │                    │ 
    """
    comprimento_colunas = list()
    numero_colunas = max([len(l) for l in lista])
    for i in range(numero_colunas):
        comprimento = 0
        for nomes in lista:
            if i < len(nomes):
                comprimento_nome = len(nomes[i])
                if comprimento_nome > comprimento:
                    comprimento = comprimento_nome
        comprimento_colunas.append(comprimento)
    for i in range(len(lista)):
        linha_imprimivel = "{:>3}: \N{BOX DRAWINGS LIGHT VERTICAL} ".format(i+1)
        for j in range(len(comprimento_colunas)):
            elemento_a_imprimir = ""
            if j < len(lista[i]):
                elemento_a_imprimir = lista[i][j]
            linha_imprimivel += ("{:<" + str(comprimento_colunas[j] + 1) + "} \N{BOX DRAWINGS LIGHT VERTICAL} ").format(elemento_a_imprimir)            
        print(linha_imprimivel)
        
doctest.testmod()