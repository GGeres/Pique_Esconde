from Entity.jogador import Jogador


class Buscador(Jogador):
    def __init__(self, nome:str):
        super().__init__(nome)
        self.olhosFechados: bool = False

    def mover(self, destino: str):
        self.posicaoAtual = destino
        print(f"[Buscador] {self.nome} moveu para '{destino}'")

    def contar(self):
        self.olhosFechados = True
        print(f"[Buscador] {self.nome} está contando com os olhos fechados...")
        self.olhosFechados = False
        print(f"[Buscador] {self.nome} terminou a contagem!")

    def baterNaBase(self, Jogador : Jogador):
        self.mover("base")
        print(f"[Buscador] {self.nome} bateu na base tentando capturar {Jogador.nome}!")    