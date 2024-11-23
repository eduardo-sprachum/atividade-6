from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def mostrar(self):
        pass

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
