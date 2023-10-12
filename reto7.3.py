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
