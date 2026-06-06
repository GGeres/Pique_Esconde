from Entity.jogador import Jogador


class Fugitivo(Jogador):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.estaOculto: bool = False

    def mover(self, destino: str):
        self.posicaoAtual = destino
        print(f"[Fugitivo] {self.nome} moveu para '{destino}'")

    def esconder(self, local: str):
        self.posicaoAtual = local
        self.estaOculto = True
        print(f"[Fugitivo] {self.nome} se escondeu em '{local}'")

    def manterOculto(self):
        print(f"[Fugitivo] {self.nome} está se mantendo oculto...")

    def correrParaBase(self):
        self.estaOculto = False
        self.mover("base")
        print(f"[Fugitivo] {self.nome} correu para a base!")