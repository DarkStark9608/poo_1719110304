class CCadenas_String:
  cadena=""
    
  def __init__(self,cadena):
    self.cadena=cadena
    
  def imprimirPorSeparado(self):
    
    for caracter in self.cadena:
      print(caracter)  
  def imprimirTipoDato(self):
    dato=""
    print("La cadena por separado")
    for caracter in self.cadena:
      if caracter.isdecimal() == True:
        dato="Numero"
      elif caracter.isalpha() ==True:
        dato="Letra"
      elif caracter.isdecimal() == False and caracter.isdigit()==False:
        dato="Simbolo"
      
      print("El siguiente : "+caracter+" es un: "+dato)    
  def imprimirLongiud(self):
    print("La longitud de la cadena es de :"+str(len(self.cadena))+" caracteres")
  def imprimirLonsinSpacio(self):
    quitarEspacio=self.cadena.replace(" ", "") 
    print("La longitud de la cadena sin espacios es de :"+str(len(quitarEspacio))+" caracteres")
    print("La cadena sin espacios: "+quitarEspacio)

eleccion="S"
while  eleccion=="S" or eleccion=="s":
  cadena=input("Ingresa el texto:\n")
  objCCadena=CCadenas_String(cadena)
  print(objCCadena.cadena)
  objCCadena.imprimirLongiud()
  objCCadena.imprimirPorSeparado()
  objCCadena.imprimirTipoDato()
  objCCadena.imprimirLonsinSpacio()
  eleccion=input("¿Desea analizar otra cadena s/n\n")
