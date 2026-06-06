# Pique_Esconde
Sistema que simula o jogo Pique-Esconde, desenvolvido para a disciplina Engenharia de Software III da Fatec Zona Leste. Implementado em Python com padrão arquitetural BCE (Boundary, Control, Entity), contemplando fluxo principal, alternativo e de exceção.


Este projeto foi desenvolvido como parte do Trabalho 2 da disciplina Engenharia de Software III do curso de Análise e Desenvolvimento de Sistemas da Fatec Zona Leste, sob orientação do professor Wilson Vendramel.
📌 Sobre o projeto
O sistema simula a dinâmica do jogo Pique-Esconde, modelado e implementado seguindo o padrão arquitetural BCE (Boundary, Control, Entity). O projeto contempla três fluxos de jogo: principal, alternativo e de exceção.
🗂️ Estrutura do projeto
pique_esconde/
├── main.py                  # Executa os três fluxos do jogo
├── entidade/
│   ├── jogador.py           # Classe abstrata Jogador
│   ├── buscador.py          # Herda de Jogador
│   ├── fugitivo.py          # Herda de Jogador
│   └── partida.py           # Classes Partida, Base e AreaJogo
├── controle/
│   └── controladores.py     # PartidaUC e ValidacaoEsconderijoUC
├── fronteira/
│   └── interfaces.py        # InterfaceVoz e InterfaceToque
└── contrato/
    └── validadora.py        # Interface Validadora, RegrasPadrao e RegrasPersonalizadas
▶️ Como executar
bashpython main.py
🛠️ Tecnologia

Python 3.x
Módulo abc para classes abstratas e interfaces

📐 Artefatos UML
O projeto acompanha os seguintes diagramas modelados no Draw.io:

Diagrama de Classes (padrão BCE)
Diagrama de Sequência (com fragmentos opt e alt)
Diagrama de Transição de Estados

👤 Autor
Gustavo Jorge Geres
