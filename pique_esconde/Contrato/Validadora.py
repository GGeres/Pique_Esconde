from abc import ABC, abstractmethod

class Validadora(ABC):
    @abstractmethod
    def validarContagem(self) -> bool:
        pass

    @abstractmethod
    def validarCaptura(self) -> bool:
        pass

    @abstractmethod
    def validarSalvamento(self) -> bool:
        pass


class RegrasPadrao(Validadora):
    def validarContagem(self) -> bool:
        print("[RegrasPadrao] Contagem válida.")
        return True
    
    def validarCaptura(self) -> bool:
        print("[RegrasPadrao] Captura confirmada.")
        return True
    
    def validarSalvamento(self) -> bool:
        print("[RegrasPadrao] Salvamento confirmado!")
        return True
    

class RegrasPersonalizadas(Validadora):
    def __init__(self, tempoExtra: int = 5):
        self.tempoExtra: int = tempoExtra

    def validarContagem(self) -> bool:
        print(f"[RegrasPersonalizadas] Contagem com {self.tempoExtra}s extra - válida.")
        return True
    
    def validarCaptura(self) -> bool:
        print("[RegrasPersonalizadas] Captura verificada com regras personalizadas - confirmada!")
        return True
    
    def validarSalvamento(self) -> bool:
        print("[RegrasPersonalizadas] Salvamento verificado com regras personalizadas - confirmado!")
        return True