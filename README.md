# reto-7
note book con resultados: https://colab.research.google.com/drive/1O32WwYl6dzEPNG3Lm27NQfff06-oTq5Q?hl=es#scrollTo=QbissQThK82O
## Punto 1 
 Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```python
def listanumeros():
  i = 1

  while i <= 100:
    print(i,i**2, sep=":")
    i += 1


if __name__ == "__main__":
  listanumeros()
```
[![image.png](https://github.com/shalomtorress/reto-7/blob/main/punto1.png)
+ Se inicializa la variable i en 1.
+ Se inicia un bucle while que se repite mientras i sea menor o igual a 100.
+ Dentro del bucle while, se imprime el valor de i y su cuadrado
+ Se suma de uno en uno ```  i += 1```
El bucle while se repite hasta que i sea mayor que 100.
## Punto 2 
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```python
i=0
while i < 999:
  i+=1
  if i%2==0:
    continue
  print(i)

i=1
while i < 1000:
  i+=1
  if i%2!=0:
    continue
  print(i)
```
[![image.png](https://github.com/shalomtorress/reto-7/blob/main/punto2.png)
+ se inicializa la variable i en 1
+  se inicia un ciclo while que se repite mientras i sea menor a 999
+  se comprueba que el numero es par con el condicional if ```i%2==0``` Si si es par, se utiliza continue para ignorar el resto y que siga con el sguiente numero
+ se inicia otro ciclo while. El ciclo se repetirá mientras la variable i sea menor a 1000. Se comprueba si el valor de i es impar. Si es así, se utiliza continue
## Punto 3 
+ Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```python
  def imprimir_numeros_pares(n): 

  if n < 2:
    return

  i = n

  while i >= 2:
    print(i)
    i -= 2
if __name__ == "__main__":
  n = int(input("Introduce un número natural n: "))
  imprimir_numeros_pares(n)
````
[![image.png](https://github.com/shalomtorress/reto-7/blob/main/punto3.png)
+ Si n es menor que 2, la función no imprime nada y se sale.
+ De lo contrario, la función inicializa la variable i en n.
+ La función utiliza un bucle while para iterar sobre todos los números pares desde 2 hasta n.
+ Para cada número par, la función imprime el número.
 ## Punto 4
+ En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.
```python
 poblacion_a = 25000000
poblacion_b = 18900000
crecimiento_a = 0.02
crecimiento_b = 0.03

año = 2022

while poblacion_a >= poblacion_b:
  poblacion_a *= (1 + crecimiento_a)
  poblacion_b *= (1 + crecimiento_b)
  año += 1

print("La población del país B superará a la de A en el año:", año)
```
+ Se declaran las variables ```poblacion_a```, ```poblacion_b```, ```crecimiento_a``` y ```crecimiento_b``` con sus valores iniciales.
+ Se inicializa la variable año en 2022.
+ Se inicia un bucle while. El bucle se repite mientras la población del país A sea mayor o igual a la población del país B.
+ el año se va incrementando de a uno ``` año += 1```
+ se obtiene el resultado
## Punto 5 
+ Imprimir el factorial de un número natural n dado.
```python
n = int(input("Introduce un número natural n: "))
factorial = 1
i = 1
while i <= n:
  factorial *= i
  i += 1

print("El factorial de n es:", factorial)
````
+ Se solicita al usuario que introduzca un número natural n.
+ Se inicializa la variable factorial en 1.
+ Se inicializa la variable i en 1.
+ Se inicia un bucle while. El bucle se repite mientras i sea menor o igual a n.
+ El bucle hace que se multiplique la variable factorial por i.


## Punto 6
+ Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.
```python
  import random 
n = int(input("Ingresar numero:"))
min = 1
max = 100
bandera : bool = True
while bandera == True:
  n_random=random.randint(min, max)
  pregunta = input("El número es mayor, menor, o igual que: " + str(n_random) + " ")
  if pregunta == "mayor":
    min = n_random + 1
  elif pregunta =="menor":
    max = n_random - 1
  else:
    break
print("El número es: " + str(n_random))  
````
+ La función import random importa el módulo random, que se utiliza para generar números aleatorios.
+ se solicita al usuario que introduzca un número.
+ min = 1 y max = 100 inicializan las variables min y max en 1 y 100, respectivamente.
+ la bandera se utiliza para controlar el bucle while.
+ El  while se ejecuta mientras bandera sea True.
En cada iteración del bucle, se genera un número aleatorio entre min y max
## Punto 7
+ Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.
```python
divisores = []
i = 2

while i <= numero:
  if numero % i == 0:
    divisores.append(i)
  i += 1

print("Los divisores de", numero, "son:", divisores)
````
+ La variable divisores se utiliza para almacenar la lista de divisores.
+ La variable i se utiliza para recorrer los números desde 2 hasta el número dado.
+ El bucle while se ejecuta mientras i sea menor o igual que el número dado.
+ se comprueba si el número dado es divisible por i.
+ Si es divisible el programa pone i a la lista delos divisores.
+ se aumenta el valor de i en 1.
## Punto 8
+ Implementar el algoritmo que muestre los números primos del 1 al 100.
```python
def es_primo(numero):
  
  for i in range(2, numero):
    if numero % i == 0:
      return False
  return True


def main():
  for numero in range(1, 101):
    if es_primo(numero):
      print(numero)


if __name__ == "__main__":
  main()
````
+ La variable numero se utiliza para almacenar el número actual que se está comprobando.
+ La variable primo se utiliza para indicar si el número actual es primo.
+ El bucle while se utiliza para iterar sobre todos los números del 1 al 100.
+ Para cada número, el bucle comprueba si es divisible por algún número entre 2 y el número actual. Si lo es, la variable primo da en False.
+ Si la variable primo sigue siendo True, el número actual se imprime.
