# Refatoramento do código original na tentativa de melhorar a experiência do leitor

# Jogo Flappy Bird com Inteligencia Artificial.
# Jogo criado seguindo o tutorial do canal do Youtube Hashtag Programação.

# Bibliotecas usadas
import pygame as pg
import os
import random
import neat

# Módulos separados para melhor entendimento do código 
from Passaro import Passaro
from Cano import Cano
from Chao import Chao

# Definindo constantes
IA_PLAY = False
GERACAO = 0
# tamanho da tela
TELA_LARGURA = 550
TELA_ALTURA = 670
# imagem do fundo
IMAGEM_BACKGROUND = pg.transform.scale2x(pg.image.load(os.path.join('images', 'bg.png'))) 
# inicializar as fontes e definir a fonte do jogo
pg.font.init()
FONTE_PONTOS = pg.font.SysFont('arial', 35)


# exibir toda a tela do game
def desenhar_tela(tela, passaros, canos, chao, pontos):
    # gerar background
    tela.blit(IMAGEM_BACKGROUND,(0,0))
    # gerar base do game
    chao.desenhar(tela)
    # função que permite vários pássaros no mesmo jogo (possibilita a IA desenvolver mais rápido)
    for passaro in passaros:
        passaro.desenhar(tela)
    # gerar vários canos ao longo do game
    for cano in canos:
        cano.desenhar(tela)
    
    # gerar os texto de pontos e de geração da IA
    texto = FONTE_PONTOS.render(f'Pontuação:{pontos}', 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    if IA_PLAY:
        texto = FONTE_PONTOS.render(f'Geração:{GERACAO}', 1, (255, 255, 255))
        tela.blit(texto, (10, 10))
    
    pg.display.update()   
    
    
    
    
# função principal para chamar todas
def main(genomas, config):
    # definir valores da IA
    global GERACAO 
    GERACAO += 1
    
    # definir funções da IA com os pássaros
    if IA_PLAY:
        redes = []
        lista_genomas = []
        passaros = []
        for _, genoma in genomas:
            rede = neat.nn.FeedForwardNetwork.create(genoma, config)
            redes.append(rede)
            genoma.fitness = 0
            lista_genomas.append(genoma)
            passaros.append(Passaro(230, 250))
    else:
        passaros = [Passaro(230, 250)]
    
    # valores iniciais do cenário e da execução
    chao = Chao(600)
    canos = [Cano(650)]
    tela = pg.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pg.time.Clock()
    
    
    # executar o game
    rodando = True
    while rodando:
        relogio.tick(30)
        
        # interação com usuário
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                rodando = False
                pg.quit()
            # possibilitar jogo sem a IA    
            if not IA_PLAY:
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        for passaro in passaros:
                            passaro.pular()
        
        # parar o game se não existir mais pássaros
        indice_cano = 0
        if len(passaros) > 0:
            if len(canos) > 1 and passaros[0].x > (canos[0].x + canos[0].CANO_TOPO.get_width()):
                indice_cano = 1
        else:
            rodando = False
            break
        
        # mover o pássaro e aicionar pontos ao chegar mais longe
        for i, passaro in enumerate(passaros):
            passaro.mover()
            if IA_PLAY:
                lista_genomas[i].fitness += 0.1
                output = redes[i].activate((passaro.y, 
                                    abs(passaro.y - canos[indice_cano].altura),
                                    abs(passaro.y - canos[indice_cano].pos_base)))
                if output[0] > 0.5:
                    passaro.pular()
        
        chao.mover()
        
        # variáveis que ajudam a implementar a exclusão de canos e pássaros 
        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            # eliminar passaro caso colidir e retirar pontos fitness
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                    if IA_PLAY:
                        lista_genomas[i].fitness -= 1
                        lista_genomas.pop(i)
                        redes.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
            cano.mover()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)
        
        # função para gerar novos canos e adicionar pontos fitness aos pássaros que passarem adiante
        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
            if IA_PLAY:
                for genoma in lista_genomas:
                     genoma.fitness += 5
            else:
                pass
        for cano in remover_canos:
            canos.remove(cano)
        
        # caso o pássaro morra, retirar ele da rede
        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                passaros.pop(i)
                if IA_PLAY:
                    lista_genomas.pop(i)
                    redes.pop(i)
        
        # gerar parte visual do game
        desenhar_tela(tela, passaros, canos, chao, pontos)

# habilitar IA
def rodar(caminho_config):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                caminho_config)
                                
    populacao = neat.Population(config)
    populacao.add_reporter(neat.StdOutReporter(True))
    populacao.add_reporter(neat.StatisticsReporter())
    
    # chamar função principal sem parâmetros em caso de jogo manual
    if IA_PLAY:
        populacao.run(main, 50)
    else:
        main(None, None)

# inicializar o programa
if __name__ == '__main__':
    caminho = os.path.dirname(__file__)
    caminho_config = os.path.join(caminho, 'config.txt')
    rodar(caminho_config)
