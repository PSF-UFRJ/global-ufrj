#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:03:54 2022

@author: paulo
"""

import doctest
import datetime

#
# Questão 1:
#
def linhas_grandes(arquivo):
    """Conta o número de linhas em arquivo que tenha mais de dez caracteres,
    excluindo o \n final de cada linha.
    
    >>> linhas_grandes("T7_q1_arq1.txt")
    4
    
    >>> linhas_grandes("T7_q1_arq2.txt")
    3
    
    >>> linhas_grandes("T7_q1_arq3.txt")
    4
    """
    count = 0
    with open(arquivo, mode="r") as f:
        for line in f:
            if len(line) > 0:
                ll = line
                if ll[-1] == '\n':
                    ll = ll[:-1]
                if(len(ll) > 10):
                    count += 1
    return count
        

#
# Questão 2:
#
def gerar_estatisticas(arquivo):
    """Calcula estatísticas de um arquivo.
    
    >>> gerar_estatisticas("T7_q2_arq1.txt")
    {'quantidade': 20, 'media': 10.5, 'maior': 20.0, 'menor': 1.0}
    
    >>> gerar_estatisticas("T7_q2_arq2.txt")
    {'quantidade': 14, 'media': 628.1428571428571, 'maior': 944.0, 'menor': 39.0}
    
    >>> gerar_estatisticas("T7_q2_arq3.txt")
    {'quantidade': 11, 'media': 5337.545454545455, 'maior': 9795.0, 'menor': 1342.0}
    """
    quantidade = 0
    soma = 0
    maior = None
    menor = None
    with open(arquivo, mode="r") as f:
        for line in f:
            number = float(line.strip())
            if maior is None or maior < number:
                maior = number
            if menor is None or menor > number:
                menor = number
            soma += number
            quantidade += 1
    return {"quantidade": quantidade, "media": soma/quantidade, "maior": maior, "menor": menor}


#
# Questão 3: Arquivos dos testes das funções linhas_grandes e gerar_estatisticas já foram fornecidas
#

#
# Questão 4: A função linhas_grandes e gerar_estatisticas já consultam os arquivos linha
#            a linha e não jogam todos os dados na memória.
#

#
# Questão 5:
#
def ler_nomes_numeros(arquivo):
    """Carrega arquivo e apresenta tupla com nomes e idade.
    
    >>> ler_nomes_numeros("T7_q5_arq.txt")
    [('Paulo Roberto Rodrigues da Silva Filho', 1979), ('Joao das Couves', 2012), ('Maria Cenoura', 2015), ('Joao Castelo dos Santos', 1990), ('Maria Fernanda Candido', 1974)]
    
    """
    res = []
    with open(arquivo, mode="r") as f:
        for line in f:
            parts = line.split()
            if(len(parts) > 1):
                idade = int(parts[-1])
                nome = " ".join(parts[:-1])
                res.append((nome, idade))
    return res
   
#
# Questão 6:
#
def maiores_de_18(arquivo):
    """Carrega arquivo e apresenta apenas tuplas com nomes que tenham mais que 18 anos.
    
    >>> maiores_de_18("T7_q5_arq.txt")
    [('Paulo Roberto Rodrigues da Silva Filho', 1979), ('Joao Castelo dos Santos', 1990), ('Maria Fernanda Candido', 1974)]
    """
    nomes = ler_nomes_numeros(arquivo)
    year = datetime.date.today().year
    maiores = [x for x in nomes if x[1] < year - 18]
    return maiores

#
# Questão 7:
#
def alfabetizar(arquivo, novo_arquivo):
    """Carrega arquivo e posiciona linhas em ordem alfabética, salvando em novo_arquivo.
    
    >>> alfabetizar("T7_q5_arq.txt", "alfabetizado_T7_q5_arq.txt")
    
    """
    linhas = []
    with open(arquivo, mode="r") as f:
        for line in f:
            if(line.strip() != ""):
                linhas.append(line)
    linhas.sort()
    
    with open(novo_arquivo, mode="w") as f:
        f.writelines(linhas)

doctest.testmod()