# -*- coding: utf-8 -*-
1 + 1
x = 422

def quadrado(x):
    return x * x

def hipotenusa(b,c):
    return (b**2 + c**2)**(0.5)

# Comentário
# hipotenusa(3+quadrado(x), 9 - y)
#   Dá NameError: name 'y' is not defined

y = 37

hipotenusa(3+quadrado(x), 9 - y)

pão = 37
