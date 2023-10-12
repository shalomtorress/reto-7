numero = int(input("Introduce un número de 2 a 50: "))

divisores = []
i = 2

while i <= numero:
  if numero % i == 0:
    divisores.append(i)
  i += 1

print("Los divisores de", numero, "son:", divisores)

