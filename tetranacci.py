def tetranacci(n):
  """
  Genera los primeros n números de la secuencia de Tetranacci (comenzando con 0, 0, 0, 1).

  Args:
    n: El número de términos a generar.

  Returns:
    Una lista con los primeros n números de Tetranacci.
  """
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 0]
  elif n == 3:
    return [0, 0, 0]
  elif n == 4:
    return [0, 0, 0, 1]
  else:
    list_tetra = [0, 0, 0, 1]
    while len(list_tetra) < n:
      next_tetra = sum(list_tetra[-4:])
      list_tetra.append(next_tetra)
    return list_tetra

# Ejemplo de uso:
n_terms = 10
tetra_sequence = tetranacci(n_terms)
print(f"Los primeros {n_terms} números de Tetranacci son: {tetra_sequence}")
