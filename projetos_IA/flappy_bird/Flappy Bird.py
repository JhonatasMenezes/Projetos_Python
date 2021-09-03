# Jogo Flappy Bird com Inteligencia Artificial.
# Jogo criado seguindo o tutorial do canal do Youtube Hashtag Programação.

# Bibliotecas usadas
import pygame as pg
import os
import random
import neat

# Definindo constantes da IA
ia_jogando = True
geracao = 0

# Definindo constantes do game
TELA_LARGURA = 550
TELA_ALTURA = 670

# imagem do cano
IMAGEM_CANO = pg.transform.scale2x(pg.image.load(os.path.join('images', 'pipe.png')))
# imagem do chão
IMAGEM_CHAO = pg.transform.scale2x(pg.image.load(os.path.join('images', 'base.png')))
# imagem do fundo
IMAGEM_BACKGROUND = pg.transform.scale2x(pg.image.load(os.path.join('images', 'bg.png'))) 
# imagem do pássaro
IMAGENS_PASSARO = [ 
    pg.transform.scale2x(pg.image.load(os.path.join('images', 'bird1.png'))),
    pg.transform.scale2x(pg.image.load(os.path.join('images', 'bird2.png'))),
    pg.transform.scale2x(pg.image.load(os.path.join('images', 'bird3.png')))
]

# inicializar as fontes e definir a fonte do jogo
pg.font.init()
FONTE_PONTOS = pg.font.SysFont('arial', 50)


class Passaro:
    # definir constantes
    IMGS = IMAGENS_PASSARO
    # animaçõesde rotação
    ROTACAO_MAXIMA = 22
    VELOCIDADE_ROTACAO = 18
    TEMPO_ANIMACAO = 5
    
    # valores iniciais do passaro
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
    
    # animação de pular    
    def pular(self):
        self.velocidade = -8
        self.tempo = 0
        self.altura = self.y
        
    # calcular deslocamento
    def mover(self):
        self.tempo += 1
        deslocamento = 0.5 * (self.tempo**2 + self.velocidade * self.tempo)
        
        # restringir deslocamento
        if deslocamento > 15:
            deslocamento = 15
        elif deslocamento < 0:
            deslocamento -= 2
        
        self.y += deslocamento
        
        # angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO
                
    # definir imagem do passaro ao voar
    def desenhar(self, tela):
        self.contagem_imagem += 1
        
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0
        
        # se estiver caindo não bater asas
        if self.angulo <= -90:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2
            
        # desenhar a imagem
        imagem_rotacionada = pg.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)
    
    # definir uma máscara de pixels para colisões    
    def get_mask(self):
        return pg.mask.from_surface(self.imagem)
                
                

class Cano:
    # distancia entre os canos para o passaro poder passar e vel do cano
    DISTANCIA = 140
    VELOCIDADE = 5
    
    # valores iniciais dos canos
    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pg.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()
        
    # definir qual altura o proximo cano aparecerá    
    def definir_altura(self):
        self.altura = random.randrange(50, 390)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA
        
    # movimento do cano    
    def mover(self):
        self.x -= self.VELOCIDADE
      
    # definir imagem do pássaro    
    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))
        
    # método de colisão  
    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pg.mask.from_surface(self.CANO_TOPO)
        base_mask = pg.mask.from_surface(self.CANO_BASE)
        
        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))
        
        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)
        
        if base_ponto or topo_ponto:
            return True
        else:
            return False
        

class Chao:
    # constantes da base do game
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO
    
    # valores iniciais do chao
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA
        
    # movimento do chao colocando o primeiro após o segundo apos sair da tela
    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE
        
        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA
            
    # exibir o chao na tela        
    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))        
    
# exibir toda a tela do game
def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND,(0,0))
    # função que permite vários pássaros no mesmo jogo (possibilita a IA desenvolver mais rápido)
    for passaro in passaros:
        passaro.desenhar(tela)
    # gerar vários canos ao longo do game
    for cano in canos:
        cano.desenhar(tela)
    
    # gerar os texto de pontos e de geração da IA
    texto = FONTE_PONTOS.render(f'Pontuação:{pontos}', 1, (255, 255, 255))
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    if ia_jogando:
        texto = FONTE_PONTOS.render(f'Geração:{geracao}', 1, (255, 255, 255))
        tela.blit(texto, (10, 10))
    
    
    # gerar base do game
    chao.desenhar(tela)
    pg.display.update()   
    
# função principal para chamar todas
def main(genomas, config):
    # definir valores da IA
    global geracao 
    geracao += 1
    
    # definir funções da IA com os pássaros
    if ia_jogando:
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
            if not ia_jogando:
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        for passaro in passaros:
                            passaro.pular()
        
        # 
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
            lista_genomas[i].fitness += 0.1
            output = redes[i].activate((passaro.y, 
                            abs(passaro.y - canos[indice_cano].altura),
                            abs(passaro.y - canos[indice_cano].pos_base)))
            if output[0] > 0.5:
                passaro.pular()
        
        chao.mover()
        
        # variáveis que ajudam a implementar a exclusão de canos de pássaros 
        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            # eliminar passaro caso colidir e retirar pontos fitness
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                    if ia_jogando:
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
            for genoma in lista_genomas:
                genoma.fitness += 5
        for cano in remover_canos:
            canos.remove(cano)
        
        # caso o pássaro morra, retirar ele da rede
        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                passaros.pop(i)
                if ia_jogando:
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
    if ia_jogando:
        populacao.run(main, 50)
    else:
        main(None, None)

# inicializar o programa
if __name__ == '__main__':
    caminho = os.path.dirname(__file__)
    caminho_config = os.path.join(caminho, 'config.txt')
    rodar(caminho_config)
