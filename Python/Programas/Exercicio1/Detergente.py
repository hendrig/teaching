class Detergente:
    quantidade = 0

    def __init__ (self, quantidade):
        self.quantidade = quantidade

    def usarDetergente(self, quantidadeASerUsada):
        if (self.quantidade < quantidadeASerUsada):
            print("Não dá pra usar tudo isso de detergente...")
            return
        
        self.quantidade = self.quantidade - quantidadeASerUsada