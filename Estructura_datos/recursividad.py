def factorial(num):
   if num < 0:
     return "Error debe de ser un numero mayor a cero"
   if num == 0:
     return 1
   if num == 1:
       return num
   else:
       return num*factorial(num-1)

numero = int(input("Ingresa el numero que deseas calcular \n"))

print("El factorial es: " + str(factorial(numero)))