from abc import ABC, abstractmethod

class Jogador (ABC):
    def __init__(self, nome: str):
        self.nome: str = nome
        self.posicaoAtual: str = "base"


        @abstractmethod
        def mover(self, destino: str):
            pass

        def __str__(self):
            return f"{self.__class__.__name__}({self.nome})"