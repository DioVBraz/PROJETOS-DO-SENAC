import tkinter
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askinteger
 
#Classes
class Time:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.saldo_gols = 0
        self.vitorias = 0
 
class Jogo:
    def __init__(self, rodada, mandante, visitante, resultado):
        self.rodada = rodada
        self.mandante = mandante.nome
        self.visitante = visitante.nome
        self.resultado = resultado
 
    def atualizar_tabela(self, tabela):
        mandante = tabela[self.mandante]
        visitante = tabela[self.visitante]
 
        mandante.saldo_gols += self.resultado[0] - self.resultado[1]
        visitante.saldo_gols += self.resultado[1] - self.resultado[0]
 
        if self.resultado[0] > self.resultado[1]:
            mandante.pontos += 3
            mandante.vitorias += 1
 
        elif self.resultado[1] > self.resultado[0]:
            visitante.pontos += 3
            visitante.vitorias += 1
 
        else:
            mandante.pontos += 1
            visitante.pontos += 1
 
class Tabela:
    def __init__(self):
        self.times = {}
    def adicionar_time(self, time):
        self.times[time.nome] = time
    def adicionar_jogo(self, jogo):
        jogo.atualizar_tabela(self.times)
    def exibir_tabela(self):
        sorted_times = sorted(self.times.values(), key=lambda x: (x.pontos, x.vitorias, x.saldo_gols), reverse=True)
        exibir_tabela_grafica.grafica(sorted_times)
 
# Função para selecionar rodada
def selecionar_rodada():
    rodada = tkinter.simpledialog.askinteger("Selecionar Rodada", "Digite o número da rodada:")
    return rodada
 
# Exibir tabela na interface gráfica
class exibir_tabela_grafica:
    @staticmethod
    def grafica(tabela):
        interface = tk.Tk()
        interface.title("Tabela do Campeonato")
        cabeçalho = ["Posição", "   Time", "   Pontos", "   Vitórias", "   Saldo de Gols"]
        for i, col_name in enumerate(cabeçalho):
            label = tk.Label(interface, text=col_name, font=("Arial", 12, "bold"), width=15)
            label.grid(row=0, column=i)
        for i, time in enumerate(tabela, 1):
            posicao_interface = tk.Label(interface, text=str(i), width=15)
            posicao_interface.grid(row=i, column=0)
            nome_interface = tk.Label(interface, text=time.nome, width=15)
            nome_interface.grid(row=i, column=1)
            pontos_interface = tk.Label(interface, text=str(time.pontos), width=15)
            pontos_interface.grid(row=i, column=2)
            vitorias_interface = tk.Label(interface, text=str(time.vitorias), width=15)
            vitorias_interface.grid(row=i, column=3)
            saldo_gols_interface = tk.Label(interface, text=str(time.saldo_gols), width=15)
            saldo_gols_interface.grid(row=i, column=4)
        for i in range(len(cabeçalho)):
            interface.grid_columnconfigure(i, weight=1)
        lider = tabela[0].nome
        lanterna = tabela[-1].nome
        rebaixados = [time.nome for time in tabela[-4:]]
        lider_label = tk.Label(interface, text="Líder da tabela: " + lider, height=2)
        lider_label.grid(row=len(tabela) + 1, columnspan=len(cabeçalho), sticky="ew")
        lanterna_label = tk.Label(interface, text="Lanterna da tabela: " + lanterna, height=2)
        lanterna_label.grid(row=len(tabela) + 2, columnspan=len(cabeçalho), sticky="ew")
        rebaixados_label = tk.Label(interface, text="Times na zona de rebaixamento: " + ", ".join(rebaixados), height=2)
        rebaixados_label.grid(row=len(tabela) + 3, columnspan=len(cabeçalho), sticky="ew")
        interface.mainloop()
 
# Campeonato
flamengo = Time("Flamengo")
vasco = Time("Vasco")
corinthians = Time("Corinthians")
palmeiras = Time("Palmeiras")
realmadrid = Time("Real Madrid")
uberlandia = Time("Uberlândia")
cruzeiro = Time("Cruzeiro")
atleticomg = Time("Atlético-MG")
gremio = Time("Grêmio")
paysandu = Time("Paysandu")
 
tabela = Tabela()
tabela.adicionar_time(flamengo)
tabela.adicionar_time(vasco)
tabela.adicionar_time(corinthians)
tabela.adicionar_time(palmeiras)
tabela.adicionar_time(realmadrid)
tabela.adicionar_time(uberlandia)
tabela.adicionar_time(cruzeiro)
tabela.adicionar_time(atleticomg)
tabela.adicionar_time(gremio)
tabela.adicionar_time(paysandu)
 
#rodada 1
jogo1 = Jogo(1, flamengo, vasco, (3, 0))
jogo2 = Jogo(1, palmeiras, corinthians, (1, 5))
jogo3 = Jogo(1, cruzeiro, atleticomg, (6, 1))
jogo4 = Jogo(1, uberlandia, realmadrid, (2, 0))
jogo5 = Jogo(1, paysandu, gremio, (0, 1))
 
tabela.adicionar_jogo(jogo1)
tabela.adicionar_jogo(jogo2)
tabela.adicionar_jogo(jogo3)
tabela.adicionar_jogo(jogo4)
tabela.adicionar_jogo(jogo5)
 
#rodada 2
jogo6 = Jogo(2, uberlandia, cruzeiro, (0, 3))
jogo7 = Jogo(2, atleticomg, gremio, (2, 3))
jogo8 = Jogo(2, realmadrid, palmeiras, (2, 0))
jogo9 = Jogo(2, paysandu, flamengo, (3, 5))
jogo10 = Jogo(2, vasco, corinthians, (3, 4))
 
tabela.adicionar_jogo(jogo6)
tabela.adicionar_jogo(jogo7)
tabela.adicionar_jogo(jogo8)
tabela.adicionar_jogo(jogo9)
tabela.adicionar_jogo(jogo10)
 
#rodada 3
jogo11 = Jogo(3, flamengo, atleticomg, (2, 0))
jogo12 = Jogo(3, cruzeiro, palmeiras, (1, 0))
jogo13 = Jogo(3, realmadrid, paysandu, (2, 3))
jogo14 = Jogo(3, gremio, vasco, (2, 1))
jogo15 = Jogo(3, corinthians, uberlandia, (2, 1))
 
tabela.adicionar_jogo(jogo11)
tabela.adicionar_jogo(jogo12)
tabela.adicionar_jogo(jogo13)
tabela.adicionar_jogo(jogo14)
tabela.adicionar_jogo(jogo15)
 
#rodada 4
jogo16 = Jogo(4, palmeiras, flamengo, (2, 4))
jogo17 = Jogo(4, uberlandia, gremio, (0, 0))
jogo18 = Jogo(4, atleticomg, paysandu, (1, 2))
jogo19 = Jogo(4, realmadrid, corinthians, (1, 2))
jogo20 = Jogo(4, cruzeiro, vasco, (2, 1))
 
tabela.adicionar_jogo(jogo16)
tabela.adicionar_jogo(jogo17)
tabela.adicionar_jogo(jogo18)
tabela.adicionar_jogo(jogo19)
tabela.adicionar_jogo(jogo20)
 
#rodada 5
jogo21 = Jogo(5, flamengo, realmadrid, (2, 1))
jogo22 = Jogo(5, vasco, uberlandia, (0, 2))
jogo23 = Jogo(5, paysandu, corinthians, (0, 3))
jogo24 = Jogo(5, cruzeiro, gremio, (0, 3))
jogo25 = Jogo(5, atleticomg, palmeiras, (0, 1))
 
tabela.adicionar_jogo(jogo21)
tabela.adicionar_jogo(jogo22)
tabela.adicionar_jogo(jogo23)
tabela.adicionar_jogo(jogo24)
tabela.adicionar_jogo(jogo25)
 
#rodada 6
jogo26 = Jogo(6, gremio, flamengo, (0, 3))
jogo27 = Jogo(6, atleticomg, corinthians, (0, 1))
jogo28 = Jogo(6, paysandu, uberlandia, (1, 0))
jogo29 = Jogo(6, palmeiras, vasco, (1, 3))
jogo30 = Jogo(6, realmadrid, cruzeiro, (0, 1))
 
tabela.adicionar_jogo(jogo26)
tabela.adicionar_jogo(jogo27)
tabela.adicionar_jogo(jogo28)
tabela.adicionar_jogo(jogo29)
tabela.adicionar_jogo(jogo30)
 
#rodada 7
jogo31 = Jogo(7, flamengo, uberlandia, (2, 1))
jogo32 = Jogo(7, gremio, palmeiras, (0, 0))
jogo33 = Jogo(7, vasco, paysandu, (1, 3))
jogo34 = Jogo(7, atleticomg, realmadrid, (1, 1))
jogo35 = Jogo(7, corinthians, cruzeiro, (6, 1))
 
tabela.adicionar_jogo(jogo31)
tabela.adicionar_jogo(jogo32)
tabela.adicionar_jogo(jogo33)
tabela.adicionar_jogo(jogo34)
tabela.adicionar_jogo(jogo35)
 
#rodada 8
jogo36 = Jogo(8, cruzeiro, flamengo, (2, 2))
jogo37 = Jogo(8, gremio, corinthians, (0, 5))
jogo38 = Jogo(8, paysandu, palmeiras, (5, 1))
jogo39 = Jogo(8, atleticomg, uberlandia, (4, 3))
jogo40 = Jogo(8, vasco, realmadrid, (2, 0))
 
tabela.adicionar_jogo(jogo36)
tabela.adicionar_jogo(jogo37)
tabela.adicionar_jogo(jogo38)
tabela.adicionar_jogo(jogo39)
tabela.adicionar_jogo(jogo40)
 
#rodada 9
jogo41 = Jogo(9, flamengo, corinthians, (0, 6))
jogo42 = Jogo(9, realmadrid, gremio, (0, 1))
jogo43 = Jogo(9, uberlandia, palmeiras, (4, 1))
jogo44 = Jogo(9, vasco, atleticomg, (0, 0))
jogo45 = Jogo(9, paysandu, cruzeiro, (0, 4))
 
tabela.adicionar_jogo(jogo41)
tabela.adicionar_jogo(jogo42)
tabela.adicionar_jogo(jogo43)
tabela.adicionar_jogo(jogo44)
tabela.adicionar_jogo(jogo45)
 
#rodada 10
jogo46 = Jogo(10, vasco, flamengo, (1, 10))
jogo47 = Jogo(10, corinthians, palmeiras, (5, 0))
jogo48 = Jogo(10, atleticomg, cruzeiro, (1, 6))
jogo49 = Jogo(10, realmadrid, uberlandia, (0, 2))
jogo50 = Jogo(10, gremio, paysandu, (2, 3))
 
tabela.adicionar_jogo(jogo46)
tabela.adicionar_jogo(jogo47)
tabela.adicionar_jogo(jogo48)
tabela.adicionar_jogo(jogo49)
tabela.adicionar_jogo(jogo50)
 
#rodada 11
jogo51 = Jogo(11, cruzeiro, uberlandia, (2, 0))
jogo52 = Jogo(11, gremio, atleticomg, (0, 0))
jogo53 = Jogo(11, palmeiras, realmadrid, (1, 4))
jogo54 = Jogo(11, flamengo, paysandu, (3, 3))
jogo55 = Jogo(11, corinthians, vasco, (3, 1))
 
tabela.adicionar_jogo(jogo51)
tabela.adicionar_jogo(jogo52)
tabela.adicionar_jogo(jogo53)
tabela.adicionar_jogo(jogo54)
tabela.adicionar_jogo(jogo55)
 
#rodada 12
jogo56 = Jogo(12, atleticomg, flamengo, (2, 4))
jogo57 = Jogo(12, palmeiras, cruzeiro, (0, 1))
jogo58 = Jogo(12, paysandu, realmadrid, (1, 0))
jogo59 = Jogo(12, vasco, gremio, (1, 3))
jogo60 = Jogo(12, uberlandia, corinthians, (2, 3))
 
tabela.adicionar_jogo(jogo56)
tabela.adicionar_jogo(jogo57)
tabela.adicionar_jogo(jogo58)
tabela.adicionar_jogo(jogo59)
tabela.adicionar_jogo(jogo60)
 
#rodada 13
jogo61 = Jogo(13, flamengo, palmeiras, (5, 0))
jogo62 = Jogo(13, gremio, uberlandia, (0, 3))
jogo63 = Jogo(13, paysandu, atleticomg, (1, 2))
jogo64 = Jogo(13, corinthians, realmadrid, (2, 2))
jogo65 = Jogo(13, vasco, cruzeiro, (0, 1))
 
tabela.adicionar_jogo(jogo61)
tabela.adicionar_jogo(jogo62)
tabela.adicionar_jogo(jogo63)
tabela.adicionar_jogo(jogo64)
tabela.adicionar_jogo(jogo65)
 
#rodada 14
jogo66 = Jogo(14, realmadrid, flamengo, (2, 6))
jogo67 = Jogo(14, uberlandia, vasco, (2, 0))
jogo68 = Jogo(14, corinthians, paysandu, (3, 1))
jogo69 = Jogo(14, gremio, cruzeiro, (5, 3))
jogo70 = Jogo(14, palmeiras, atleticomg, (2, 2))
 
tabela.adicionar_jogo(jogo66)
tabela.adicionar_jogo(jogo67)
tabela.adicionar_jogo(jogo68)
tabela.adicionar_jogo(jogo69)
tabela.adicionar_jogo(jogo70)
 
#rodada 15
jogo71 = Jogo(15, flamengo, gremio, (2, 1))
jogo72 = Jogo(15, corinthians, atleticomg, (1, 0))
jogo73 = Jogo(15, uberlandia, paysandu, (1, 2))
jogo74 = Jogo(15, vasco, palmeiras, (2, 3))
jogo75 = Jogo(15, cruzeiro, realmadrid, (4, 1))
 
tabela.adicionar_jogo(jogo71)
tabela.adicionar_jogo(jogo72)
tabela.adicionar_jogo(jogo73)
tabela.adicionar_jogo(jogo74)
tabela.adicionar_jogo(jogo75)
 
#rodada 16
jogo76 = Jogo(16, uberlandia, flamengo, (2, 4))
jogo77 = Jogo(16, palmeiras, gremio, (1, 0))
jogo78 = Jogo(16, paysandu, vasco, (2, 1))
jogo79 = Jogo(16, realmadrid, atleticomg, (0, 3))
jogo80 = Jogo(16, cruzeiro, corinthians, (2, 5))
 
tabela.adicionar_jogo(jogo76)
tabela.adicionar_jogo(jogo77)
tabela.adicionar_jogo(jogo78)
tabela.adicionar_jogo(jogo79)
tabela.adicionar_jogo(jogo80)
 
#rodada 17
jogo81 = Jogo(17, flamengo, cruzeiro, (5, 1))
jogo82 = Jogo(17, corinthians, gremio, (2, 0))
jogo83 = Jogo(17, palmeiras, paysandu, (1, 4))
jogo84 = Jogo(17, uberlandia, atleticomg, (3, 2))
jogo85 = Jogo(17, realmadrid, vasco, (2, 0))
 
tabela.adicionar_jogo(jogo81)
tabela.adicionar_jogo(jogo82)
tabela.adicionar_jogo(jogo83)
tabela.adicionar_jogo(jogo84)
tabela.adicionar_jogo(jogo85)
 
#rodada 18
jogo86 = Jogo(18, corinthians, flamengo, (7, 1))
jogo87 = Jogo(18, gremio, realmadrid, (1, 0))
jogo88 = Jogo(18, palmeiras, uberlandia, (0, 1))
jogo89 = Jogo(18, atleticomg, vasco, (1, 0))
jogo90 = Jogo(18, cruzeiro, paysandu, (4, 1))
 
tabela.adicionar_jogo(jogo86)
tabela.adicionar_jogo(jogo87)
tabela.adicionar_jogo(jogo88)
tabela.adicionar_jogo(jogo89)
tabela.adicionar_jogo(jogo90)
 
tabela.exibir_tabela()
 
# Selecionar rodada
class InterfaceJogosRodada:
    def __init__(self, jogos):
        self.jogos = jogos
        self.rodada = tk.Tk()
        self.rodada.title("Jogos da Rodada")
        self.label_rodada = tk.Label(self.rodada, text="Número da Rodada:")
        self.label_rodada.pack()
        self.entry_rodada = tk.Entry(self.rodada)
        self.entry_rodada.pack()
        self.button_selecionar = tk.Button(self.rodada, text="Selecionar Rodada", command=self.mostrar_jogos)
        self.button_selecionar.pack()
        self.rodada.mainloop()
    def mostrar_jogos(self):
        rodada_selecionada = self.entry_rodada.get()
        try:
            rodada_selecionada = int(rodada_selecionada)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido para a rodada.")
            return
        jogos_rodada = []
        for jogo in self.jogos:
            if jogo.rodada == rodada_selecionada:
                resultado = jogo.resultado
                jogos_rodada.append(f"{jogo.mandante} {resultado[0]} x {resultado[1]} {jogo.visitante}")
        if jogos_rodada:
            messagebox.showinfo(f"Jogos da Rodada {rodada_selecionada}", "\n".join(jogos_rodada))
        else:
            messagebox.showinfo("Informação", f"Não há jogos registrados para a rodada {rodada_selecionada}.")
jogos = [jogo1, jogo2, jogo3, jogo4, jogo5, jogo6, jogo7, jogo8, jogo9, jogo10,
         jogo11, jogo12, jogo13, jogo14, jogo15, jogo16, jogo17, jogo18, jogo19, jogo20,
         jogo21, jogo22, jogo23, jogo24, jogo25, jogo26, jogo27, jogo28, jogo29, jogo30,
         jogo31, jogo32, jogo33, jogo34, jogo35, jogo36, jogo37, jogo38, jogo39, jogo40,
         jogo41, jogo42, jogo43, jogo44, jogo45, jogo46, jogo47, jogo48, jogo49, jogo50,
         jogo51, jogo52, jogo53, jogo54, jogo55, jogo56, jogo57, jogo58, jogo59, jogo60,
         jogo61, jogo62, jogo63, jogo64, jogo65, jogo66, jogo67, jogo68, jogo69, jogo70,
         jogo71, jogo72, jogo73, jogo74, jogo75, jogo76, jogo77, jogo78, jogo79, jogo80,
         jogo81, jogo82, jogo83, jogo84, jogo85, jogo86, jogo87, jogo88, jogo89, jogo90]
InterfaceJogosRodada(jogos)
 
# Banco de dados
bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
 
cursor = bd.cursor()
 
nome_bd = "campeonato"
 
cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(nome_bd))
cursor.execute("USE {}".format(nome_bd))
bd.commit()
 
nome_tabela = "tabela_brasileirao"
 
tabela_bd = '''CREATE TABLE IF NOT EXISTS {} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(20),
                pontos INT,
                numero_vitorias INT,
                saldo_gols INT)'''.format(nome_tabela)
cursor.execute(tabela_bd)
bd.commit()
 
sorted_times = sorted(tabela.times.values(), key=lambda x: (x.pontos, x.vitorias, x.saldo_gols), reverse=True)
for i, time in enumerate(sorted_times, 1):
    dados_time = (i, time.nome, time.pontos, time.vitorias, time.saldo_gols)
    inserir_dados = "INSERT IGNORE INTO {} (id, nome, pontos, numero_vitorias, saldo_gols) VALUES (%s, %s, %s, %s, %s)".format(nome_tabela)
    cursor.execute(inserir_dados, dados_time)
bd.commit()
cursor.close()
bd.close()