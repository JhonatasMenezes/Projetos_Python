import pygame as pg
import random
import os

# imagem do cano
IMAGEM_CANO = pg.transform.scale2x(pg.image.load(os.path.join('images', 'pipe.png')))


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
