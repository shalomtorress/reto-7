def es_primo(numero):
  """Devuelve True si el número es primo, False en caso contrario."""

  for i in range(2, numero):
    if numero % i == 0:
      return False
  return True


def main():
  """Programa principal."""

  for numero in range(1, 101):
    if es_primo(numero):
      print(numero)


if __name__ == "__main__":
  main()
