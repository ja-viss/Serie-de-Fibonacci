def tribonacci(n):
  """
  Genera los primeros n números de la secuencia de Tribonacci (comenzando con 0, 0, 1).

  Args:
    n: El número de términos a generar.

  Returns:
    Una lista con los primeros n números de Tribonacci.
  """
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 0]
  elif n == 3:
    return [0, 0, 1]
  else:
    list_trib = [0, 0, 1]
    while len(list_trib) < n:
      next_trib = list_trib[-1] + list_trib[-2] + list_trib[-3]
      list_trib.append(next_trib)
    return list_trib

# Ejemplo de uso:
n_terms = 10
trib_sequence = tribonacci(n_terms)
print(f"Los primeros {n_terms} números de Tribonacci son: {trib_sequence}")
