import sys
import pickle

from functools import total_ordering

def nulo_ou_vazio(texto):
    return texto == None or not texto.strip()

def validar_faixa_inteiro(pergunta, inicio, fim, padrao = None):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrao != None:
                entrada = padrao

            valor = int(entrada)

            if inicio <= valor <= fim:
                return valor

        except ValueError:
            print(f'Valor Inválido, favor digitar entre {inicio} e {fim}')

def validar_faixa_inteiro_ou_branco(pergunta, inicio, fim):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada):
                return None

            valor = int(entrada)

            if inicio <= valor <= fim:
                return valor

        except ValueError:
            print(f'Valor Inválido, favor digitar entre {inicio} e {fim}')

class ListaUnica:
    def __init__(self, elem_class):
        self.lista = list()
        self.elem_class = elem_class

    def __len__(self):
        return len(self.lista)

    def __iter__(self):
        return iter(self.lista)

    def __getitem__(self, item):
        return self.lista[item]

    def indiceValido(self, i):
        return i >= 0 and i < len(self.lista)

    def adiciona(self, elem):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)

    def remove(self, elem):
        if len(self.lista>0):
            self.lista.remove(elem)

    def pesquisa(self, elem):
        self.verifica_tipo(elem)
        try:
            return self.lista.index(elem)
        except ValueError:
            return -1

    def verifica_tipo(self, elem):
        if type(elem) != self.elem_class:
            raise TypeError("Tipo Inválido.")

    def ordena(self, chave = None):
        self.lista.sort(key=chave)

@total_ordering
class Nome:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f'<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.__nome} Chave: {self.__chave}'

    def __eq__(self, other):
        return self.nome == other

    def __lt__(self, other):
        return self.nome < other

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if nulo_ou_vazio(valor):
            raise ValueError('Nome não pode ser Numo nem em Branco.')
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)

    @property
    def chave(self):
        return self.__chave

    @staticmethod
    def CriaChave(nome):
        return nome.strip().lower()

