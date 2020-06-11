import unidecode  #importo la libreria
class Palindromo: #Creacion de la clase
  palabra ="" #Atributos

  def __init__(self,palabra):  #ctr 
    self.palabra=palabra    #igualo variables
    print("La palabra: "+self.palabra)
    #Aqui le doy formato quitando espacios y haciendo todas minusculas y quitando puntos
    self.palabra=palabra.replace(" ", "").lower().replace(".","")#.replace("á","a")
    #metodo palindromo
  def Palindromo(self):
    #Creo dos listas
    lista=[]
    listaaux=[]
    #dos contadores
    cont=0
    aux=0
    resultado=""
    #Recorro mi palabra hasta la longitud de dicha
    for indice in range(len(self.palabra)):
      #obtengo un caracter con el indice del bucle
      caracter = self.palabra[indice]
      #agrego el caracter a las dos listas
      lista.append(caracter)
      listaaux.append(caracter)
      cont=cont+1 #incremento mi contador
    
#Creo otro bucle tengo dos listas mi idea es recorrer una normal y la otra a la inversa
    for i in range(cont-1,-1,-1): 
      #evaluo ambas listas
      if lista[aux]==listaaux[i]:
        resultado="Es palindromo"
      else:
        resultado="No palindromo"
      #Un contador para mis indices al recorrer mi listas ya que el for va en decremento 
      # y el aux en aumento para asi recorrer ambas listas
      aux=aux+1
    #imprimo el resultado si es o no palindromo
    print(resultado)
# Mi variable para mi menu que hare con un while
eleccion="S"
while  eleccion=="S" or eleccion=="s":
#Pido la palabra al usuario
  palabra =input("Ingresa la palabra:\n")
    #Si la palabra contine puras letras entrara al if con eso aplicare unidecode que me sirve para quitar los acentos si lo hacia en la clase me tronaba :() esto para que admita numeros y cadenas 
  if palabra.isalpha() == True:
    palabra=unidecode.unidecode(palabra)
  print(palabra)
    #Creo mi objeto
  objPalindromo= Palindromo(palabra)
  #LLamo el metodo Palindromo
  objPalindromo.Palindromo()
  #para evaluar si se repite o no
  eleccion=input("¿Desea analizar otra cadena s/n\n")
