import unittest
from Tabela import *
 
class TesteTime(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes do Time
        self.time1 = Time("Corinthians")
        self.time2 = Time("Flamengo")
        self.tabela = Tabela()
        self.tabela.adicionar_time(self.time1)
        self.tabela.adicionar_time(self.time2)
 
    def test_time_existente(self):
        # Testa se os times foram adicionados corretamente à tabela
        self.assertIn("Corinthians", self.tabela.times)
        self.assertIn("Flamengo", self.tabela.times)
 
class TesteJogo(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes do Jogo
        self.time1 = Time("Corinthians")
        self.time2 = Time("Flamengo")
        self.tabela = Tabela()
        self.tabela.adicionar_time(self.time1)
        self.tabela.adicionar_time(self.time2)
 
    def test_rodada(self):
        # Testa se a rodada é adicionada corretamente na tabela
        jogo = Jogo(1, self.time1, self.time2, (7, 1))
        self.tabela.adicionar_jogo(jogo)
        self.assertEqual(len(self.tabela.times), 2)
 
    def test_mandante_e_visitante(self):
        # Testa se os times mandantes e visitantes estão corretos para cada jogo
        for i in range(9):
            jogo = Jogo(i, self.time1, self.time2, (0, 0))
            self.tabela.adicionar_jogo(jogo)
            self.assertEqual(jogo.mandante, "Corinthians")
            self.assertEqual(jogo.visitante, "Flamengo")
 
    def test_resultado_correto(self):
        # Testa se o resultado do jogo é registrado corretamente
        jogo = Jogo(1, self.time1, self.time2, (2, 1))
        self.tabela.adicionar_jogo(jogo)
        self.assertEqual(jogo.resultado, (2, 1))
 
class TesteTabela(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes da Tabela
        self.time1 = Time("Corinthians")
        self.time2 = Time("Flamengo")
        self.tabela = Tabela()
        self.tabela.adicionar_time(self.time1)
        self.tabela.adicionar_time(self.time2)
 
    def test_times_na_tabela(self):
        # Testa se os times na tabela são instâncias corretas da classe Time
        for time in self.tabela.times.values():
            self.assertIsInstance(time, Time)
 
    def test_pontos_correspondentes(self):
        # Testa se os pontos são atribuídos corretamente após um jogo
        jogo = Jogo(1, self.time1, self.time2, (3, 1))
        self.tabela.adicionar_jogo(jogo)
        self.assertEqual(self.time1.pontos, 3)
        self.assertEqual(self.time2.pontos, 0)
 
    def test_saldo_gols_correto(self):
        # Testa se o saldo de gols é calculado corretamente após um jogo
        jogo = Jogo(1, self.time1, self.time2, (3, 0))
        self.tabela.adicionar_jogo(jogo)
        self.assertEqual(self.time1.saldo_gols, 3)
        self.assertEqual(self.time2.saldo_gols, -3)
 
    def test_numero_vitorias_correto(self):
        # Testa se o número de vitórias é atualizado corretamente após um jogo
        jogo = Jogo(1, self.time1, self.time2, (3, 0))
        self.tabela.adicionar_jogo(jogo)
        self.assertEqual(self.time1.vitorias, 1)
        self.assertEqual(self.time2.vitorias, 0)
 
if __name__ == '__main__':
    unittest.main()