import sys
# Irei pedir um número ao usuário
numUsuario = int(input('Digite um número: '))

# adiciono ao número do usuário + 10 para ter certeza que a sequência irá passar dele
limitador = numUsuario + 10
# variáveis de apoio
f1 = 0
f2 = 1
f3 = 0

#gerar a sequência e verificar se o numUsuario faz parte 
while (f3 < limitador):
     f3 = f1 + f2
     f1 = f2
     f2 = f3
     print(f3,end=', ')
     if f3 == numUsuario:
           print('Seu número faz parte da sequência!')
           sys.exit()
     elif f3 > limitador:
         print("Seu número não faz parte da sequência")
        

