import string
from random import randint

def geradorDeCpf():

   # 9 números aleatórios
   arNumeros = []
   for i in range(9):
      arNumeros.append( randint(0,9) )      

   
   # Calculado o primeiro DV
   somaJ = ( arNumeros[0] * 10 ) + ( arNumeros[1] * 9 ) + ( arNumeros[2] * 8 ) + ( arNumeros[3] * 7 )  + ( arNumeros[4] * 6 ) + ( arNumeros[5] * 5 ) + ( arNumeros[6] * 4 )  + ( arNumeros[7] * 3 ) + ( arNumeros[8] * 2 )

   restoJ = somaJ % 11

   if ( restoJ == 0 or restoJ == 1 ):
      j = 0
   else:
      j = 11 - restoJ   

   arNumeros.append( j )

   # Calculado o segundo DV
   somaK = ( arNumeros[0] * 11 ) + ( arNumeros[1] * 10 ) + ( arNumeros[2] * 9 ) + ( arNumeros[3] * 8 )  + ( arNumeros[4] * 7 )  + ( arNumeros[5] * 6 ) + ( arNumeros[6] * 5 )  + ( arNumeros[7] * 4 )  + ( arNumeros[8] * 3 ) + ( j * 2 )

   restoK = somaK % 11
   
   if ( restoK == 0 or restoK == 1 ):
      k = 0
   else:
      k = 11 - restoK      

   arNumeros.append( k )
   
   cpf = ''.join(str(x) for x in arNumeros)

   return cpf

# def geradorDeNome():
