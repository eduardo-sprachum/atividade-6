from animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def mostrar(self):
        return f"Gato - Nome: {self.nome}, Idade: {self.idade}, Raça: {self.raca}"

    def __str__(self):
        return f"Gato - {super().__str__()}, Raça: {self.raca}"
