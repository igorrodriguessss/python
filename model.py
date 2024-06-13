class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome  
        self.idade = idade  

    def mostrar_info(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')


pessoa1 = Pessoa('giancarlo', 25)
pessoa1.mostrar_info()  
pessoa2 = Pessoa('ivo', 86)
pessoa2.mostrar_info()  