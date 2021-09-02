# Jogo Flappy Bird com Inteligencia Artificial.
# Jogo criado seguindo o tutorial do canal do Youtube Hashtag Programação.

# Bibliotecas usadas
import pygame as pg
import os
import random

# Definindo constantes do game
TELA_LARGURA = 500
TELA_ALTURA = 800
# imagem do cano
IMAGEM_CANO = pg.tranform.scale2x(pg.image.load(os.path.join('images', 'pipe.png')))
# imagem do chão
IMAGEM_CHAO = pg.tranform.scale2x(pg.image.load(os.path.join('images', 'base.png')))
# imagem do fundo
IMAGEM_BACKGROUND = pg.tranform.scale2x(pg.image.load(os.path.join('images', 'bg.png'))) 
# imagem do pássaro
IMAGENS_PASSARO = [ 
    pg.tranform.scale2x(pg.image.load(os.path.join('images', 'bird1.png'))),
    pg.tranform.scale2x(pg.image.load(os.path.join('images', 'bird2.png'))),
    pg.tranform.scale2x(pg.image.load(os.path.join('images', 'bird3.png')))
]

# inicializar as fontes e definir a fonte do jogo
pg.font.init()
FONTE_PONTOS = pg.font.SysFont('arial', 50)


class Passaro:
    # definir constantes
    IMGS = IMAGENS_PASSARO
    # animaçõesde rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5
    
    def __init__(self, x, y):
        # valores iniciais do passaro
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
        
    def pular(self,):
        self.velocidade = -10,5
        self.tempo = 0
        self.altura = self.y
        
    def mover(self):
        # calcular deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo
        
        # restringir deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        
        self.y += deslocamento
        
        # angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo =self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO
                
    def desenhar(self, tela):
        # definir imagem do passaro ao voar
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
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2
            
        # desenhar a imagem
        imagem_rotacionada = pg.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)
        
        

class Cano:
    def __init__(self):
        pass


class Chao:
    def __init__(self):
        pass


