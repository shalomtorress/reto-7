n = int(input("Introduce un número natural n: "))

factorial = 1

i = 1

while i <= n:
  factorial *= i
  i += 1

print("El factorial de n es:", factorial)
