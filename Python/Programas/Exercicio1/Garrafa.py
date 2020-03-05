class Garrafa:
    capacidade = 0
    quantidadeNaGarrafa = 0
    estaSuja = False

    def __init__ (self, capacidade):
        self.capacidade = capacidade

    def encherGarrafa(self):
        self.quantidadeNaGarrafa = self.capacidade

    def esvaziarGarrafa(self):
        self.quantidadeNaGarrafa = 0
        self.estaSuja = True

    def limparGarrafa(self, detergente):
        quantidadeNecessariaParaLimpar = self.capacidade * 0.2

        if(self.quantidadeNaGarrafa > 0):
            print("O garrafa ainda está cheia")
            return

        if(not self.estaSuja):
            print("O garrafa já está limpa")

        detergente.usarDetergente(quantidadeNecessariaParaLimpar)
        self.estaSuja = False