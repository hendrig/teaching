texto = "esse esse é o meu texto texto texto"

class Palavra():
    def __init__(self, palavra, traducao):
        self.palavra = palavra
        self.traducao = traducao
        self.vezes = 0

class Dicionario():
    def __init__(self):
        self.dicionario = list()

    def adicionarPalavra(self, palavra):
        existe = False
        for p in self.dicionario:
            if p.palavra == palavra.palavra:
                existe = True
                p.vezes += 1

        if not existe:
            palavra.vezes += 1
            self.dicionario.append(palavra)

    def ordenarPorOcorrenciaDecrescente(self):
        self.dicionario.sort(key=lambda p: p.vezes, reverse=True)



palavras = texto.split()
d = Dicionario()

for palavra in palavras:
    a_palavra = Palavra(palavra, '')
    d.adicionarPalavra(a_palavra)

d.ordenarPorOcorrenciaDecrescente()

for p in d.dicionario:
    print(p.palavra + ': ' + str(p.vezes) + ' vezes')