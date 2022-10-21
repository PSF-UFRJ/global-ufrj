#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:39:46 2022

@author: Paulo Roberto Rodrigues da Silva Filho - Matrícula: 122065831
"""

#
# Questão 1: 
#
# A resposta dessa questão é esse próprio arquivo.
#

UM = 1

def f(x,y):
    return x - (2 * y)

def g(x):
    return 2 * x

#
# Questão 2: 
#
# A resposta é retF = -15
#
retF = f(f(UM, g(UM)), g(f(UM, f(UM, UM))))

#
# Questão 3: 
#
# Seguindo a sequência de execução do Python, temos:
# (1) retF = f(f(UM, g(UM)), g(f(UM, f(UM, UM))))
# (2) retF = f(f(1, g(1)), g(f(1, f(1, 1)))), 
#       pois as constantes UM foram substituídas por 1
# (3) retF = f(f(1, g(1)), g(f(1, -1))), 
#       pois f(1, 1) = 1 - (2 * 1) = -1
# (4) retF = f(f(1, g(1)), g(3)),
#       pois f(1, -1) = 1 - (2 * (-1)) = 3
# (5) retF = f(f(1, g(1)), 6),
#       pois g(3) = 2 * 3 = 6
# (6) retF = f(f(1, 2), 6), 
#       pois g(1) = 2 * 1 = 2
# (7) retF = f(-3, 6), 
#       pois f(1, 2) = 1 - (2 * 2) = -3
# (8) retF = ,
#       pois f(-3, 6) = -3 - (2 * 6) = -15
#

#
# Questão 4: 
#
# São 6 formas, que são:
# f1 = g(g(1))
# f2 = g(f(1, 1))
# f3 = f(g(1),1)
# f4 = f(1, g(1))
# f5 = f(f(1, 1), 1)
# f6 = f(1, f(1, 1))

#
# Questão 5: 
#
# São 18 formas, que são:
#
# f[1 a 6]: g(.), chamando em . todas as formas da questão 4, acima.
# f[7 a 12], f(., 1), chamando em . todas as formas da questão 4, acima.
# f[13 a 18], f(1, .), chamando em . todas as formas da questão 4 acima.

#
# Questão 6: 
#
# abaixo, ret18 = 18
ret18 = f(g(g(g(g(UM)))),f(UM,UM))
# E, abaixo, ret444 = 444
ret444 = f(f(g(g(g(g(g(g(g(g(g(UM))))))))), g(g(g(g(g(UM)))))),g(UM))

#
# Questão 7:
#
# Sim, é possível obter qualquer número inteiro com esta linguagem.
# Vamos considerar as seguintes funções, como base para cálculo de todos os
# números:

MENOS_UM = f(UM, UM)
ZERO = f(g(UM), UM)
UM = 1 # A constante já dada na linguagem
DOIS = g(UM)

# Todo número impar positivo pode ser dado por:
# QUALQUER_IMPAR_POSITIVO = f(f...f(f(UM, MENOS_UM), MENOS_UM)...), MENOS_UM)
# Exemplos:
TRES = f(f(f(UM, f(UM, UM)), UM), f(UM, UM))
CINCO = f(f(f(f(UM, f(UM, UM)), UM), f(UM, UM)), f(UM, UM))
SETE = f(f(f(f(f(UM, f(UM, UM)), UM), f(UM, UM)), f(UM, UM)), f(UM, UM))
NOVE = f(f(f(f(f(f(UM, f(UM, UM)), UM), f(UM, UM)), f(UM, UM)), f(UM, UM)), f(UM, UM)) 
# E assim por diante

# Todo número impar negativo pode ser dado por:
# QUALQUER_IMPAR_NEGATIVO = f(f(...f(f(UM, UM), UM),...), UM)
MENOS_TRES = f(f(UM, UM), UM)
MENOS_CINCO = f(f(f(UM, UM), UM), UM)
MENOS_SETE = f(f(f(f(UM, UM), UM), UM), UM)
MENOS_NOVE = f(f(f(f(f(UM, UM), UM), UM), UM), UM)
# E assim por diante

# Todo número par positivo pode ser dado por:
# QUALQUER_PAR_POSITIVO = f(f...f(g(UM), MENOS_UM)...), MENOS_UM)
# Exemplos:
QUATRO = f(g(UM), f(UM, UM))
SEIS = f(f(g(UM), f(UM, UM)), f(UM, UM))
OITO = f(f(f(g(UM), f(UM, UM)), f(UM, UM)), f(UM, UM))
DEZ = f(f(f(f(g(UM), f(UM, UM)), f(UM, UM)), f(UM, UM)), f(UM, UM))
# E assim por diante

# Todo número par negativo pode ser dado por:
# QUALQUER_PAR_NEGATIVO = f(f(...f(g(UM), UM),...), UM)
MENOS_DOIS = f(f(g(UM), UM), UM)
MENOS_QUATRO = f(f(f(g(UM), UM), UM), UM)
MENOS_SEIS = f(f(f(f(g(UM), UM), UM), UM), UM)
MENOS_OITO = f(f(f(f(f(g(UM), UM), UM), UM), UM), UM)
# E assim por diante

# Lembrando que o -1, 0, 1 e 2 já foram mostrados como base para todos os outros números.

# Agora, pensando em h(x) = 3x:
def h(x):
    return 3*x

# Sabemos que a função f(x,y) permite, através da soma e da subtração, adicionar 
# ou subtrair valores pares de um outro número qualquer, que, por ser sempre derivado
# da h(x) e da primitiva UM, só gera valores ímpares. Assim, f(x, y), a partir de
# h(x) e de UM, só vai também gerar valores ímpares, porque f(x, y), com parâmetros
# ímpares também só vai gerar números ímpares.
# Se h(x) substituir g(x), o universo de números gerados pela Linguagem Minúscula
# vai ser apenas números ímpares, portanto, não gerando todos os números inteiros
# possíveis.

#
# Questão 8:
#
# Considerando que pode-se haver saltos exponenciais em direção aos números 
# escolhidos para serem representados, a menor representação de 444 seria dada
# por uma busca que caminhasse nas potências de 2 (representadas pela recursão de
# g(x)), sempre rodeando o número procurado nas menores diferenças. A resposta
# da questão 6, acima, segue essa abordagem, assim, o menor número de chamadas
# de função para gerar 444, seria o dado na função 6 acima.
#
# Portanto:
retMin444 = f(f(g(g(g(g(g(g(g(g(g(UM))))))))), g(g(g(g(g(UM)))))),g(UM))
#
# e o número de chamadas é 17 (dezessete) chamadas de função.
#