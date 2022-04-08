Ncantidad = int(input("cuantos numero ingresaras: "))
contador = 0
contadoPar= 0
contadorImpar = 0
while(contador < Ncantidad):
        numero = int(input("ingrese numero "))
        if(numero %2 == 0):
              contadoPar = contadoPar + 1
              
        if(numero %3 == 0):
                contadorImpar = contadorImpar + 1
               
        contador = contador + 1                   

print(contadoPar)
print(contadorImpar)