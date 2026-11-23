# Fase Maldita

Jogo de plataforma 2D feito com PyGame. O jogador controla um quadrado e tem de chegar na porta verde de cada uma das 4 fases. As fases têm armadilhas: chão falso, blocos invisíveis, bloco que cai, espinho escondido, porta falsa, teleporte, inversor dos controles e uma porta que foge. O jogo conta as mortes e o tempo e guarda um ranking das melhores partidas.

## Integrantes do grupo

- Samuel Arruda de Vasconcelos
- Joaquim Blanco
- Guilherme Gasparini

## Como rodar o jogo

1. Instale o Python 3.
2. Instale o pygame: `pip install pygame`
3. Baixe este repositório: botão **Code** e depois **Download ZIP**, ou `git clone https://github.com/joaquimblanco/py.game.git`.
4. Abra um terminal dentro da pasta do repositório e rode `python base_do_jogo.py` (no Mac ou no Linux, `python3 base_do_jogo.py`).

A pasta `sons` tem de ficar junto do arquivo `base_do_jogo.py`.

## Como jogar

- No menu, digite 3 letras do seu nome e aperte ENTER para começar.
- Setas ou A e D andam para os lados.
- Espaço, W ou seta para cima pulam.
- ESC fecha o jogo.

## Vídeo do jogo funcionando

COLE AQUI O LINK DO VÍDEO

## Uso de IA generativa

Usamos IA generativa (Claude, da Anthropic) no desenvolvimento do jogo. A maior parte do código do arquivo `base_do_jogo.py` foi gerada pela IA a partir dos nossos pedidos: os mapas e a montagem das fases, o movimento e as colisões, os sons, as armadilhas, o placar e o ranking. A classe `quadrado` veio do nosso código inicial e foi adaptada. Nós juntamos as partes, testamos o jogo, corrigimos erros e ajustamos os valores da gravidade e da velocidade.

O histórico da conversa com a IA está em: COLE AQUI O LINK DO HISTÓRICO
