class Palindromo:
  palabra =""

  def __init__(self,palabra):
    self.palabra=palabra
    print("La palabra: "+self.palabra)
    self.palabra=palabra.replace(" ", "")   

  def Palindromo(self):
    lista=[]
    listaaux=[]
    cont=0
    aux=0
    resultado=""
    for indice in range(len(self.palabra)):
      caracter = self.palabra[indice]
      lista.append(caracter)
      listaaux.append(caracter)
      cont=cont+1

    for i in range(cont-1,-1,-1): 
      if lista[aux]==listaaux[i]:
        resultado="Es palindromo"
      else:
        resultado="No palindromo"
      aux=aux+1
      cont=cont-1    
    
    print(resultado)

eleccion="S"
while  eleccion=="S" or eleccion=="s":

  palabra =input("Ingresa la palabra:\n")
  objPalindromo= Palindromo(palabra)
  objPalindromo.Palindromo()
  eleccion=input("¿Desea analizar otra cadena s/n\n")
