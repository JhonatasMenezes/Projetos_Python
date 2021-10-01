import pygame as pg
import os

IMAGENS_PASSARO = [ 
    pg.transform.scale2x(pg.image.load(os.path.join('images', 'bird1.png'))),
    pg.transform.scale2x(pg.image.load(os.path.join('images', 'bird2.png'))),
    pg.transform.scale2x(pg.image.load(os.path.join('images', 'bird3.png')))
]

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
