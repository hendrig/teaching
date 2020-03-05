class Prato:
    capacidade = 0
    quantidadeNoPrato = 0
    cor = ""
    estaSujo = False

    def __init__ (self, capacidade, cor):
        self.cor = cor
        self.capacidade = capacidade

    def encherPrato(self):
        self.quantidadeNoPrato = self.capacidade

    def esvaziarPrato(self):
        self.quantidadeNoPrato = 0
        self.estaSujo = True

    def limparPrato(self, detergente):
        quantidadeNecessariaParaLimpar = self.capacidade * 0.1

        if(self.quantidadeNoPrato > 0):
            return "O prato ainda está cheio"

        if(not self.estaSujo):
            return "O prato já está limpo"

        detergente.usarDetergente(quantidadeNecessariaParaLimpar)
        self.estaSujo = False
