#utilizando for para loops

qtAndares = 20;

#Realizando de forma decrescente"

controle = qtAndares

for i in range(qtAndares,0, -1):

    controle -= 1

    if(controle + 1 == 13):
       continue;

    print(f"Andar Decrescente: {controle + 1}")

#Realizando de forma crescente
print("======================================== Executando de forma Crescente")

for i in range(qtAndares):

  if(i + 1 == 13):
    continue

  print(f"Andar Crescente: {i + 1}")


# loops com While
print("======================================== Executando loop com while")
#Realizando de forma crescrente loop com while

contador = 0;
while(contador != qtAndares):

  contador += 1;

  if(contador == 13):

    continue;

  print(f"Andar Crescente: {contador}")

print("======================================== Executando de forma Decrescente")

contador = qtAndares;
while(contador != 0):

  if(contador == 13):
    contador -= 1
    continue;

  print(f"Andar Crescente: {contador}")
  contador -= 1
