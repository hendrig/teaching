import unittest
import Prato
import Garrafa
import Detergente

class TestesUnitarios(unittest.TestCase):

    capacidadePrato = 200
    capacidadeGarrafa = 500
    quantidadeDeDetergente = 300

    prato = Prato.Prato(capacidadePrato, "PratoTeste")
    garrafa = Garrafa.Garrafa(capacidadeGarrafa)
    detergente = Detergente.Detergente(quantidadeDeDetergente)

    #Testes do Prato
    def testEncherPrato(self):
        self.prato.encherPrato()
        self.assertEqual(int(self.prato.quantidadeNoPrato), self.capacidadePrato)

    def testTentarLimparPratoComComida(self):
        self.prato.encherPrato()
        retorno = self.prato.limparPrato(self.detergente)
        self.assertEqual(retorno, "O prato ainda está cheio")

    def testTentarLimparPratoQueJaEstaLimpo(self):
        self.prato.encherPrato()
        self.prato.esvaziarPrato()
        self.prato.limparPrato(self.detergente)
        retorno = self.prato.limparPrato(self.detergente)
        self.assertEqual(retorno, "O prato já está limpo")
        self.assertFalse(self.prato.estaSujo)

    def testEsvaziarPrato(self):
        self.prato.encherPrato()
        self.prato.esvaziarPrato()
        self.assertEqual(int(self.prato.quantidadeNoPrato), 0)
        self.assertTrue(self.prato.estaSujo)

    #Testes da Garrafa
    def testEncherGarrafaComCapacidadeTotal(self):
        self.garrafa.encherGarrafa()
        self.assertEqual(int(self.garrafa.quantidadeNaGarrafa), self.capacidadeGarrafa)

if __name__ == '__main__':
    unittest.main()