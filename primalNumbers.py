print("¿Hasta que número desea detectar números primos?")

while True:
    try:
        x = int(input())
        if x < 2:                                  # Verificamos que el numero sea mayor que 2
          print("El numero debe ser mayor que 2")
          continue
        break
    except ValueError:
        print("Por favor, ingresa un número entero y positivo")
    
total_primal = 0                                   # Contador de numeros primos totales

# Bucle de numeros a analizar
# Usamos el algoritmo de division hasta la raiz
# cuadrada, el cual optimiza el proceso.
for num in range(2, x+1):                          # En el for me cuenta hasta el penúltimo numero, no hasta el último, por tanto x+1  
  is_primal = True                                 # Se define una variable booleana True, indicando que el numero es primo hasta que se demuestre lo contrario :)                        
  if num > 2 and num % 2 == 0: continue            # Para reducir las iteraciones, todo numero par y mayor que 2 no es primo, se salta.

  # Bucle de divisores hasta la raiz caudrada
  for y in range(2, max(2, int(num ** 0.5) + 1)):  # Hallar la raiz cuadrada del numero para optimizar division y convertir a entero para eliminar el float
                                                   # Recorre los divisores hasta la raiz cuadrada incluida
    if num % y == 0:                                
      is_primal = False                            # Si el numero obtiene resto 0 con algun divisor, entonces no es primo, y la variable booleana cambia su valor a false y
      break                                        # se cierra el bucle

  # Verificacion de la variable booleana 
  # para determinar si el numero es primo o no.
  if is_primal:                                    # Si ningun divisor obtuvo resto 0, la variable primal deberia seguir siendo True, por tanto, el numero es primo
    print(f"{num} es un primo")
    total_primal = total_primal + 1                            # Aumenta el contador de numeros primos

print(f"En total hay {total_primal} números primos desde 2 hasta {x}")