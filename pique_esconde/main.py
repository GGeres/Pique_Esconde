from Entity.buscador import Buscador
from Entity.fugitivo import Fugitivo
from Entity.partida import Partida, Base, AreaJogo
from Control.controladores import PartidaUC, ValidacaoEsconderijoUC
from Boundary.interfaces import InterfaceVoz, InterfaceToque
from Contrato.Validadora import RegrasPadrao


def simularFluxoPrincipal():
    print("=" * 60)
    print("=== PIQUE-ESCONDE - FLUXO PRINCIPAL ===")
    print("=" * 60)

    #Instancias
    fugitivo = Fugitivo("João")
    buscador = Buscador("Amanda")
    partida = Partida(tempoLimite=60)
    base = Base(localizacao="Árvore Central")
    areaJogo = AreaJogo(raio=50.0)
    validadora = RegrasPadrao()
    interfaceVoz = InterfaceVoz()
    interfaceToque = InterfaceToque()
    validacaoUC = ValidacaoEsconderijoUC(areaJogo)
    partidaUC = PartidaUC(partida, validadora)

    # Passo 1 - Fugitivo declara prontidão
    interfaceVoz.transmitirDeclaracoes("Estou Pronto")

    # Passo 2 - PartidaUc inicia a rodada
    partidaUC.rodarRodada()
    partida.iniciarRodada()

    # Passo 3 - Buscador conta com os olhos fechados
    buscador.contar()
    base.registrarToque(buscador)

    # Passo 4 - Fugitivo se esconde
    fugitivo.esconder("arbusto norte")
    fugitivo.estaOculto = True

    # Passo 5 - Buscador busca, Fugitivo se mantém oculto
    print(f"[Buscador] {buscador.nome} está buscando...")
    fugitivo.manterOculto()

    # Passo 6 - Corrida para a base
    buscador.baterNaBase(fugitivo)
    fugitivo.correrParaBase()

    # Passo 7 - Toque detectado
    interfaceToque.detectarToque()
    interfaceToque.identificarJogador(fugitivo)

    # Passo 8 - Validação e encerramento
    captura = partidaUC.validarCaptura()
    if captura:
        interfaceVoz.captarGrito("1, 2, 3 pego!")
        partidaUC.encerrarRodada("Captura confirmada")
        partidaUC.notificarCaptura(fugitivo)


def simularFluxoAlternativo():
    print("\n" + "=" * 60)
    print("=== PIQUE-ESCONDE - FLUXO ALTERNATIVO (Fugitivo Salvo)")
    print("=" * 60)

    fugitivo = Fugitivo("Maria")
    buscador = Buscador("Amanda")
    partida = Partida(tempoLimite=60)
    validadora = RegrasPadrao()
    partidaUC = PartidaUC(partida, validadora)
    interfaceVoz = InterfaceVoz()

    partidaUC.rodarRodada()
    buscador.contar()
    fugitivo.esconder("arbusto sul")
    fugitivo.manterOculto()

    #Fugitivo percebe a distração e corre primeiro
    print(f"[Fugitivo] {fugitivo.nome} percebeu a distração do buscador!")
    fugitivo.correrParaBase()

    salvamento = partidaUC.validarSalvamento()
    if salvamento:
        interfaceVoz.captarGrito("1, 2, 3 salvo!")
        partidaUC.encerrarRodada("Salvamento confirmado")

def simularFluxoExcecao():
    print("\n" + "=" * 60)
    print("=== PIQUE-ESCONDE - FLUXO EXCEÇÃO (Fora da Área)")
    print("=" * 60)

    fugitivo = Fugitivo("Julio")
    partida = Partida(tempoLimite=60)
    areaJogo = AreaJogo(raio=50.0)
    validadora = RegrasPadrao()
    partidaUC = PartidaUC(partida, validadora)
    validacaoUC = ValidacaoEsconderijoUC(areaJogo)

    partidaUC.rodarRodada()
    fugitivo.esconder("fora") #posição inválida

    # Validação detecta violação
    dentro = validacaoUC.confirmarLocal(fugitivo.posicaoAtual)
    if not dentro:
        partidaUC.encerrarRodada("Violação de limite - rodada anulada")

if __name__ == "__main__":
    simularFluxoPrincipal()
    simularFluxoAlternativo()
    simularFluxoExcecao()