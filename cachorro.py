from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.porte = porte

    def mostrar(self):
        return f"Cachorro - Nome: {self.nome}, Idade: {self.idade}, Porte: {self.porte}"

    def __str__(self):
        return f"Cachorro - {super().__str__()}, Porte: {self.porte}"
