

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print('Au Au!')

class Gato(Animal):
    def fazer_som(self):
        print('Miau!')

cachorro = Cachorro('Rex')
gato = Gato('Felix')

cachorro.fazer_som()  # Output: Au Au!
gato.fazer_som()  # Output: Miau!
