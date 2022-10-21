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

doctest.testmod()