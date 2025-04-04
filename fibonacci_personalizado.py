def fibonacci_personalizado(n, a, b):
  """
  Genera los primeros n números de una secuencia tipo Fibonacci con valores iniciales a y b.

  Args:
    n: El número de términos a generar.
    a: El primer valor de la secuencia.
    b: El segundo valor de la secuencia.

  Returns:
    Una lista con los primeros n números de la secuencia.
  """
  if n <= 0:
    return []
  elif n == 1:
    return [a]
  elif n == 2:
    return [a, b]
  else:
    list_fib = [a, b]
    while len(list_fib) < n:
      next_fib = list_fib[-1] + list_fib[-2]
      list_fib.append(next_fib)
    return list_fib

# Ejemplo de uso:
n_terms = 10
primer_valor = 2
segundo_valor = 3
fib_sequence_personalizada = fibonacci_personalizado(n_terms, primer_valor, segundo_valor)
print(f"Los primeros {n_terms} números de la secuencia tipo Fibonacci ({primer_valor}, {segundo_valor}) son: {fib_sequence_personalizada}")
