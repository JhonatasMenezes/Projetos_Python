# Algoritmo que mostraas jogadas certas para resolver a Torre de Hanoi
# levando em conta o número de dicscos

# Função recursiva
def _torre_De_hanoi_recursivo(numero_de_discos, origem, destino, auxiliar):
    # resolução com 1 disco
    if numero_de_discos == 1:
        print(f'{numero_de_discos} : {origem} -> {destino}')
        return
    # resoluçao para os demais números de discos, que irá chamar a 
    # resolução de 1 caso for com 1 discos, e assim por diante sempre
    # resolvendo -1 disco
    _torre_De_hanoi_recursivo(numero_de_discos - 1, origem, auxiliar, destino)
    print(f'{numero_de_discos} : {origem} -> {destino}')
    _torre_De_hanoi_recursivo(numero_de_discos - 1, auxiliar, destino, origem)
    
# Função que define o númerode discos    
def torre_de_hanoi_discos(numero_de_discos: int):
    _torre_De_hanoi_recursivo(numero_de_discos, origem='A', destino='B', auxiliar='C')
    pass

# Função final que mostrará na telaas jogadas certas
def torre_de_hanoi(discos: int):
    for i in range(1, discos + 1):
        print(f'### Hanoi para {i} discos ###')    
        torre_de_hanoi_discos(i)
        
# Chamando pra conferir        
if __name__ == '__main__':
    torre_de_hanoi(1)
    
        