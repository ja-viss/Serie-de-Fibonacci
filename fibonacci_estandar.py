def fibonacci_estandar(n):
  """
  Genera los primeros n números de la secuencia de Fibonacci estándar.

  Args:
    n: El número de términos a generar.

  Returns:
    Una lista con los primeros n números de Fibonacci.
  """
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  else:
    list_fib = [0, 1]
    while len(list_fib) < n:
      next_fib = list_fib[-1] + list_fib[-2]
      list_fib.append(next_fib)
    return list_fib

# Ejemplo de uso:
n_terms = 10
fib_sequence = fibonacci_estandar(n_terms)
print(f"Los primeros {n_terms} números de Fibonacci son: {fib_sequence}")
