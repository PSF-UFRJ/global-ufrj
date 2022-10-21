#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:47:52 2022

@author: paulo
"""
import doctest

#
# Questão 1: Código [int(input()) for i in range(1000000) if input()] no REPL
# Resposta: 
#  Esse código chama, para cada elemento do range(1000000) a função input,
#  que abre uma entrada de dados do teclado, a serem inseridos pelo usuário, e, a
#  cada <Enter>, captura o texto da entrada e chama o input novamente e converte 
#  essa nova entrada (também finalizada com <Enter>) para um int, se for possível, 
#  armazenando sequencialmente os inteiros convertidos do input, em uma lista.
# 
#  Depois de repetir esse procedimento 1000000 de vezes (o comprimento do range),
#  o array que estava sendo montado é retornado.
# 
#  Deve-se perceber que se o o range tem 1000000 elementos, o input será chamado
#  2 * 1000000, para retornar o array apenas dos inputs chamados em uma posição
#  par da sequencias de interações do usuário, finalizadas com <Enter>
#

#
# Questão 2:
#
def largura(l):
    """Calcula a largura necessária para imprimir os números na lista l, 
    verticalmente, de forma alinhada.
    
    >>> largura([1,2,-35])
    3
    
    >>> largura([1,2,-35, 2, 6252, -192, 2, 3])
    4
    """
    if(not type(l) is list):
        return
    final_len = -1
    for item in l:
        item_str = "{}".format(item)
        item_str_len = len(item_str)
        if(final_len < item_str_len):
            final_len = item_str_len
    return final_len

#
# Questão 3:
#
def largura_de_funcao(l, f):
    """Calcula a largura necessária para imprimir os números na lista l, 
    verticalmente, de forma alinhada, e coloca como primeiro elemento da dupla 
    de resposta; e também calcula a largura necessária para imprimir, verticalmente, 
    os resultados da função f aplicada aos números da lista, e coloca como o 
    segundo elemento da dupla de resposta.
    
    >>> largura_de_funcao([-900, -888, -899, -900], lambda a: a + 900)
    (4, 2)
    
    >>> largura_de_funcao([1, 2, -10, 10000], lambda a: a + 10000)
    (5, 5)
    
    """
    if(not type(l) is list):
        return
    final_len = -1
    final_func_len = -1
    for item in l:
        item_str = "{}".format(item)
        item_str_len = len(item_str)
        if(final_len < item_str_len):
            final_len = item_str_len
        func_item = f(item)
        func_item_str = "{}".format(func_item)
        func_item_str_len = len(func_item_str)
        if(final_func_len < func_item_str_len):
            final_func_len = func_item_str_len
    return final_len, final_func_len

#
# Questão 5:
#
def e_tabela(ll):
    """Verifica se uma lista ll data é uma tabela, ou seja, se ela é uma lista
    de listas e se todas essas listas possuem o mesmo tamanho.
    
    >>> e_tabela([1, 2, 3])
    False
    
    >>> e_tabela([[1], [2], ["Lalala"]])
    True
    
    >>> e_tabela([[1, 2], [1, 2, 3], [1]])
    False
    
    >>> e_tabela([])
    False
    
    >> e_tabela([[], [], []])
    False
    """
    if not type(ll) is list:
        return False
    if len(ll) == 0:
        return False
    
    list_line_len = -1
    for l in ll:
        if not type(l) is list:
            return False
        if list_line_len == -1:
            list_line_len = len(l)
            if list_line_len == 0:
                return False
        if len(l) != list_line_len:
            return False
    return True

#
# Questão 7:
#
def transposta(ll):
    """Mostra a transporta de uma tabela.
    
    >>> transposta([[0]])
    [[0]]
    
    >>> transposta([[0], [1]])
    [[0, 1]]
    
    >>> transposta([[0, 0], [1, 1]])
    [[0, 1], [0, 1]]
    
    >>> transposta([[1, 2, 3], [3, 6, 9]])
    [[1, 3], [2, 6], [3, 9]]
    """
    if not e_tabela(ll):
        return
    
    num_colunas = len(ll[0])
    num_linhas = len(ll)
    
    colunas = list()
    for i in range(num_colunas):
        coluna = list()
        for j in range(num_linhas):
            coluna.append(ll[j][i])
        colunas.append(coluna)

    return colunas

#
# Questão 6:
#
def mostra_tabela(ll, transpor=False):
    """Mostra tabela formatada para saída padrão. Se o parâmetro ""transpor" for
    True, mostra a tabela transposta.
    
    >>> mostra_tabela([[1,222],[3,"texto exemplo"]])
    │ 1 │           222 │
    │ 3 │ texto exemplo │
    
    >>> mostra_tabela([[1,222],[3,-1]])
    │ 1 │ 222 │
    │ 3 │  -1 │
    
    >>> mostra_tabela([[1,222],[3,-1]], True)
    │   1 │  3 │
    │ 222 │ -1 │
    
    >>> mostra_tabela([[1,222],[3,-1]], False)
    │ 1 │ 222 │
    │ 3 │  -1 │
    """
    if not e_tabela(ll):
        print("Não é uma tabela. Não é possível mostrá-la")
        return
    
    if transpor:
        lll  = transposta(ll)
        t = ll
    else:
        lll  = ll
        t = transposta(ll)
        
    tamanhos_colunas = [largura(i) for i in t]
    
    for i in range(len(lll)):
        for j in range(len(lll[i])):
            print(("\N{BOX DRAWINGS LIGHT VERTICAL} {:>" + 
                   str(tamanhos_colunas[j]) + "} ").format(lll[i][j]), end='')
        print("\N{BOX DRAWINGS LIGHT VERTICAL}")
        
#
# Questão 7 - Retorno:
# Resposta da pergunta: A função mostra_trasnposta é muito mais simples do que
# a função mostra tabela, porque a função mostra_tabela já possui internamente
# a opção de mostrar a transposta (foi utilizada a transposta para calcular a
# largura das colunas, então bastou ajustar essa utilização para implementar
# a impressao da transposta). Na realidade, a impressão da tabela e de sua
# transposta têm o mesmo grau de complexidade, porque são praticamente a mesma 
# função.
#   
def mostra_transposta(ll):
    """Mostra a transposta da tabela ll data formatada na saída padrão.
    
    >>> mostra_transposta([[1,222],[3,-1]])
    │   1 │  3 │
    │ 222 │ -1 │
    """
    mostra_tabela(ll, True)

doctest.testmod()