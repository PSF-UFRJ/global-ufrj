#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:12:42 2022

@author: paulo
"""
import doctest

#
# Questão 1:
# (Questão 2 é a docstring dessa função)
#
def fatorial_impar(num):
    """Retorna o fatorial impar de um número, que é o fatorial calculado apenas
    com números impares. Exemplos:
    fatorial_impar(10) = 9 * 7 * 5 * 3 * 1
    fatorial_impar(17) = 17 * 15 * 13 * 11 * 9 * 7 * 5 * 3 * 1
    
    Mais exemplos:
    >>> fatorial_impar(11)
    10395
    >>> fatorial_impar(19)
    654729075
    >>> fatorial_impar(0)
    1
    """
    i = abs(num)
    res = 1
    
    if i == 0 or i == 1:
        return 1
    
    if i % 2 == 0: 
        i = i - 1
        
    while i >= 1:
        res *= i
        i = i - 2
    
    return res

#
# Questão 3:
#
def fatorial_par(num):
    """Retorna o fatorial par de um número, que é o fatorial calculado apenas
    com números pares. Exemplos:
    fatorial_par(10) = 10 * 8 * 6 * 4 * 2
    fatorial_par(17) = 16 * 14 * 12 * 10 * 8 * 6 * 4 * 2
    
    Mais exemplos:
    >>> fatorial_par(11)
    3840
    >>> fatorial_par(18)
    185794560
    >>> fatorial_par(0)
    1
    """
    i = abs(num)
    res = 1
    
    if i == 0 or i == 1:
        return 1
    
    if i % 2 == 1: 
        i = i - 1
        
    while i >= 2:
        res *= i
        i = i - 2
    
    return res

#
# Questão 4: Sendo I(x) o fatorial ímpar, e P(x) o fatorial par, então o fatorial
# tradicional é dado por x! = P(x) * I(x)
# (Questão 5 é a docstring dessa função)
#
def fatorial_composto(num):
    """Retorna o fatorial de um número, calculado a partir do fatorial impar e 
    do fatorial par
    >>> fatorial_composto(0)
    1
    >>> fatorial_composto(1)
    1
    >>> fatorial_composto(2)
    2
    >>> fatorial_composto(5)
    120
    >>> fatorial_composto(11)
    39916800
    """
    return fatorial_impar(num) * fatorial_par(num)

#
# Questão 6: Fatorial geral
#
def fatorial_geral(k, r, num):
    """Retorna o fatorial geral de um número, multiplicando apenas os números
    múltiplos de um determinado fator
    >>> fatorial_geral(1, 1, 5)
    120
    >>> fatorial_geral(2, 2, 5)
    8
    >>> fatorial_geral(3, 1, 15)
    3640
    """
    i = abs(num)
    kk = abs(k)
    
    if i == 0 or i == 1:
        return 1
    
    res = 1
    
    while i >= 1:
        if (i - r) % kk == 0:
            res *= i
        i = i - 1
        
    return res

#
# Questão 7: Os valores padrão, na função fatorial_geral(k, r, num) seriam:
# - k = 1
# - r = 0 ou r = 1
# - num -> Qualquer número inteiro, não negativo, que pode ter seu fatorial calculado.
#

#
# Questão 8:
#
def fatorial_recursivo(num):
    """Calcula o fatorial usando um algoritmo recursivo.
    >>> fatorial_recursivo(0)
    1
    >>> fatorial_recursivo(1)
    1
    >>> fatorial_recursivo(2)
    2
    >>> fatorial_recursivo(5)
    120
    >>> fatorial_recursivo(11)
    39916800
    """
    if num == 0 or num == 1:
        return 1
    return num * fatorial_recursivo(num - 1)

doctest.testmod()