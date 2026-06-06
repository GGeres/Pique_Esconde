from Entity.jogador import Jogador


class Base:
    def __init__(self, localizacao: str):
        self.localizacao: str = localizacao
        self.ocupada: bool = False

    def registrarToque(self, jogador: Jogador):
        self.ocupada = True
        print(f"[Base] Toque registado de {jogador.nome} em '{self.localizacao}'")


class AreaJogo:
    def __init__(self, raio: float):
        self.raio: float = raio

    def verificarLimite(self, posicao: str) -> bool:
        #Simulação: posições válidas são diferentes de "fora"
        dentro = posicao != "fora"
        if not dentro:
            print(f"[AreaJogo] Posição '{posicao}' está fora do limite!")
        else:
            print(f"[AreaJogo] Posição '{posicao}' está dentro do limite!")
        return dentro
    
class Partida:
    def __init__(self, tempoLimite: int):
        self.tempoLimite: int = tempoLimite
        self.rodadaAtual: int = 0
        self.qtdFugitivos: int = 0
        self.qtdCaptura: int = 0
        self.qtdDeclaracoes: int = 0

    def iniciarRodada(self):
        self.rodadaAtual += 1
        print(f"[Partida] Rodada {self.rodadaAtual} iniciada!")