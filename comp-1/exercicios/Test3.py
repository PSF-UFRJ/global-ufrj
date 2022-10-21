#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:00:14 2022

@author: paulo
"""

import doctest
from random import randint

def fibo(n):
    """n-ésimo número de Fibonacci
    >>> fibo(0)
    0
    
    >>> fibo(1)
    1
    
    >>> fibo(5)
    5
    
    >>> fibo(8)
    21
    """
    if n < 0 or not(isinstance(n, int)):
        return
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    

#
# Questão 1: Tri-bonacci
# Questão 2: Docstring incluída na função abaixo.
#
def tribo(n):
    """Calcula o Tri-bonacci, definido por:
    T0 = 0, T1 = 1, T2 = 0, Tn+3 = Tn+2 + Tn+1 + Tn.
    >>> tribo(0)
    0
    
    >>> tribo(1)
    1
    
    >>> tribo(2)
    0
    
    >>> tribo(3)
    1
    
    >>> tribo(4)
    2
    
    >>> tribo(10)
    68
    """
    if n < 0 or not(isinstance(n, int)):
        return
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 0
    else:
        return tribo(n-1) + tribo(n-2) + tribo(n-3)
    
#
# Questão 3: 
# A série de Fibonacci, dada pela função "fibo", acima, e o Tribonacci, dado
# pela função tribo, acima, apresentam as seguintes sequencias:
#
# Indice:       0   1   2   3   4   5   6   7   8   9   10
# Fibonacci:    0   1   1   2   3   5   8  13  21  34   55
# Tribonacci:   0   1   0   1   2   3   6  11  20  37   68
#
# A partir do indice n = 9, então todos os Tribonaccis serão maiores do que o
# número de Fibonacci correspondente.
#
# Assim, para n > 8, os valores de Tn (Tribonacci) são sempre maiores 
# que os de Fn (Fibonacci).
#
#


#
# Questão 4:
# (Questão 6 é o Docstring)
# (Questão 7 é o teste aleatório)
#
def proximo_fibo(n):
    """Calcula o próximo número de fibonacci a partir de n, ou seja, que 
    retorna o menor número de Fibonacci que é estritamente maior do que n:
    >>> proximo_fibo(0)
    1
    >>> proximo_fibo(1)
    2
    >>> proximo_fibo(4)
    5
    >>> proximo_fibo(11)
    13
    
    Esse é um teste randômico para o proximo_fibo:
    >>> n = randint(0, 20) ; proximo_fibo(fibo(n)) == fibo(n+1)
    True
    """ 
    index = 0
    while fibo(index) <= n:
        index = index + 1
    return fibo(index)

#
# Questão 5:
# (Questão 6 é o Docstring)
# (Questão 7 é o teste aleatório)
#
def contar_fibonacci(a, b):
    """Retorna a quantidade de números de Fibonacci presentes 
    dentro do intervalo [a, b]
    >>> contar_fibonacci(-1, 0)
    1
    >>> contar_fibonacci(0, 0)
    1
    >>> contar_fibonacci(0, 3)
    4
    >>> contar_fibonacci(4, 9)
    2
    
    Esse é o teste randômico para contar_fibonacci:
    >>> n = randint(1, 20) ; contar_fibonacci(fibo(n), fibo(n+2)) == 3
    True
    
    Outro teste mais randomico ainda:
    >>> n = randint(1, 20); j = randint(1,4) ; contar_fibonacci(fibo(n), fibo(n+j)) == j+1
    True
    """
    index = 0
    num = 0
    prev = -1
    f = fibo(index)
    while f <= b:
        if f >= a and f != prev:    
            num = num + 1
        index = index + 1
        prev = f
        f = fibo(index)
    return num


#
# Questão 8:
#
# Considere os tempos das seguintes chamadas de fibo:
#    
# %time fibo(10)
# CPU times: user 28 µs, sys: 7 µs, total: 35 µs
# Wall time: 38.4 µs
# Out[104]: 55
#
# %time fibo(20)
# CPU times: user 4.03 ms, sys: 0 ns, total: 4.03 ms
# Wall time: 4.03 ms
# Out[105]: 6765
#
# %time fibo(30)
# CPU times: user 414 ms, sys: 0 ns, total: 414 ms
# Wall time: 413 ms
# Out[106]: 832040
#
# %time fibo(40)
# CPU times: user 50.8 s, sys: 0 ns, total: 50.8 s
# Wall time: 50.7 s
# Out[107]: 102334155
#
# A gente percebe o aumento enorme do tempo de execução.
#
# Isso acontece, porque para cada n chamado em fibo(n), o número de vezes
# que fibo(.) é chamada recursivamente é igual a 2^(n-1),
# pois, se chamamos fibo(0) ou fibo(1), não há recursão. Se chamarmos fibo(2), 
# chamamos fibo, recursivamente, duas vezes. Se chamarmos fibo(3), chamaremos
# fibo(2) recursivamente duas vezes, num total de quatro vezes. Se chamarmos
# fibo(4), chamaremos fibo(3) recursivamente duas vezes, chamando fibo num total
# de oito vezes e assim por diante.
#
# Isso quer dizer que fibo conforme foi implementado possui complexidade c exponencial
# com c(n) = 2^(n-1)
#

doctest.testmod()
