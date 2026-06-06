from Entity.jogador import Jogador

class InterfaceVoz:
    def captarGrito(self, mensagem: str):
        print(f"[InterfaceVoz] Grito captado: '{mensagem}'")

    def identificarJogador(self, jogador: Jogador):
        print(f"[InterfaceVoz] Jogador identificado por voz: {jogador.nome}")

    def transmitirDeclaracoes(self, mensagem: str):
        print(f"[InterfaceVoz] Declaração transmitida: '{mensagem}'")

class InterfaceToque:
    def detectarToque(self):
        print("[InterfaceToque] Toque detectado na base!")
    
    def identificarJogador(self, jogador: Jogador):
        print(f"[InterfaceToque] Jogador identificado por toque: {jogador.nome}")

    def registrarMomento(self):
        print("[InterfaceToque] Momento do toque registrado")