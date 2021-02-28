import sys
import pickle

from functools import total_ordering

def nulo_ou_vazio(texto):
    return texto == None or not texto.strip()

def validar_faixa_inteiro(pergunta, inicio, fim, padrao = None):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrao ! = None:
                entrada = padrao

            valor = int(entrada)

            if inicio <= valor <= fim:
                return valor

        except ValueError:
            print(f'Valor Inválido, favor digitar entre {inicio} e {fim}')


