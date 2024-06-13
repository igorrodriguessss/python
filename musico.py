class Musico:
    def __init__(self, nome, instrumento):
       self.nome = nome
       self.instrumento = instrumento
    def mostrar_info(self):
       print(f'Músico: {self.nome}, Instrumento: {self.instrumento}') 