from Entity.partida import Partida, AreaJogo
from Entity.jogador import Jogador
from Contrato.Validadora import Validadora


class ValidacaoEsconderijoUC:
        def __init__(self, areaJogo: AreaJogo):
            self.areaJogo: AreaJogo = areaJogo

        def confirmarLocal(self, posicao: str) -> bool:
              print(f"[ValidacaoEsconderijoUC] Confirmando local '{posicao}'...")
              return self.verificarLimite(posicao)
        
        def verificarLimite(self, posicao: str) -> bool:
              return self.areaJogo.verificarLimite(posicao)
        
class PartidaUC:
        def __init__(self, partida: Partida, validadora: Validadora):
            self.partida: Partida = partida
            self.validadora: Validadora = validadora


        def rodarRodada(self):
              print("\n[PartidaUC] Iniciando nova rodada...")
              self.partida.iniciarRodada()

        def encerrarRodada(self, motivo: str = ""):
              print(f"[PartidaUC] Encerrando rodada. Motivo: {motivo}")

        def validarCaptura(self) -> bool:
            resultado = self.validadora.validarCaptura()
            if resultado:
                self.partida.qtdCaptura += 1
            return resultado
        
        def validarSalvamento(self) -> bool:
              return self.validadora.validarSalvamento()
        
        def notificarCaptura(self, jogador:Jogador):
              print(f"[PartidaUC] Notificando captura para {jogador.nome}!")