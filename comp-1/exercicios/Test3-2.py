#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:57:58 2022

@author: paulo
"""
import doctest

def tribonacci(n):
    """Retorna numero de Tribonacci, definido por:
        T(0) = 0, T(1) = 1, T(2) = 0,T(n+3) = T(n+2) + T(n+1) + T(n).
        >>> tribonacci(0)
        0
        >>> tribonacci(1)
        1
        >>> tribonacci(2)
        0
        >>> tribonacci(10)
        68
        >>> tribonacci(7)
        11
    """
    if n < 0:
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 0
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

doctest.testmod()        