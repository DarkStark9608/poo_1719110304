#creacion de clase
class CCadenas_String:
  #atributos
  cadena=""
  #ctr  
  def __init__(self,cadena):
    self.cadena=cadena
    #metodo para imprimir separado
  def imprimirPorSeparado(self):
    #for para leer la palabra
    for caracter in self.cadena:
      #se imprime caracter por caracter
      print(caracter)  
  #metodo para decir que es
  def imprimirTipoDato(self):
    #variable aux 
    dato=""
    print("La cadena por separado")
    #for para leer y los if para evaluar que es
    for caracter in self.cadena:
      if caracter.isdecimal() == True:
        dato="Numero"
      elif caracter.isalpha() ==True:
        dato="Letra"
      elif caracter.isdecimal() == False and caracter.isdigit()==False:
        dato="Simbolo"
      #se imprime 
      print("El siguiente : "+caracter+" es un: "+dato)    
  #metodo oara imprimir la longitud con .len
  def imprimirLongiud(self):
    print("La longitud de la cadena es de :"+str(len(self.cadena))+" caracteres")
    #metodo para imprimir sin espacios
  def imprimirLonsinSpacio(self):
    #quita espacios remplaznado el espacio por nada
    quitarEspacio=self.cadena.replace(" ", "") 
    print("La longitud de la cadena sin espacios es de :"+str(len(quitarEspacio))+" caracteres")
    print("La cadena sin espacios: "+quitarEspacio)
#menu
eleccion="S"
while  eleccion=="S" or eleccion=="s":
  cadena=input("Ingresa el texto:\n")
  objCCadena=CCadenas_String(cadena)
  print("El texto ingresado es: "+objCCadena.cadena)
  objCCadena.imprimirLongiud()
  objCCadena.imprimirPorSeparado()
  objCCadena.imprimirTipoDato()
  objCCadena.imprimirLonsinSpacio()
  eleccion=input("¿Desea analizar otra cadena s/n\n")
