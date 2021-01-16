def triangulo(num):
    if num == 0:
        return ''
    else:
        return ("*" * num + '\n') + triangulo(num - 1)


numero = int(input("Ingresa el tamaño:\n "))
piramide = triangulo(numero)
print(piramide)
