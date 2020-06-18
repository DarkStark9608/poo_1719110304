#Creacion de la clase
class CCifrado:
  cadena=""#atributos

  def __init__(self,cadena):#ctr
    self.cadena=cadena #igualo variables
  
  #metodo para cifrar
  def cifrarCadena(self):
    cifrarCadena=""#creo una variable string para utilizar mas adelante
    for caracter in self.cadena: #Con un for recorrere la cadena que el usuario ingrese
      numAlfabeto= ord(caracter) #Con el funcion ord() obtengo el valor del caracter dentro del codigo ascii
      cifrarCadena += chr(numAlfabeto +3) #Aqui ciframos con la funcion chr() donde al numero obtenido anteriormente le sumaremos 3 que es el codigo cesar y lo concatenamos en la variable para imprimirlo
    print("La cadena cifrada es: "+cifrarCadena)
  
  #metodo para descifrar
  def descifrarCadena(self):
    descifrarCadena=""#creo una variable string para utilizar mas adelante
    for caracter in self.cadena: #Con un for recorrere la cadena que el usuario ingrese
      numAlfabeto= ord(caracter)#Con el funcion ord() obtengo el valor del caracter dentro del codigo ascii
      descifrarCadena += chr(numAlfabeto -3) #Aqui desciframos con la funcion chr() donde al numero obtenido anteriormente le restaremos 3 ya que para cifrar utilizamos 3 posiciones en la rotacion 
    print("La cadena descifrada es: "+descifrarCadena) #imprimimos la variable
    
#Menu
repetir="s"
while repetir=="s" or repetir=="S":#Se realizara mientras el usuario diga que si
  cadena=input("Ingresa tu cadena: \n")#Ingresa su texto a cifrar
  opcion=input("Ingresa 1) Para encriptar: \nIngresa 2) Para descifrar\n")#el uuario selecciona que desea realizar  
  objCesar=CCifrado(cadena)# Apartir de la opcion que desea realizar evaluara y realizara ya sea:
  if opcion=="1":#Cifrar
    objCesar.cifrarCadena()
  elif opcion=="2":#Descifrar
    objCesar.descifrarCadena()
  else:#Un pequeño flitro
    print("Valor incorrecto")
    break
  repetir=input("Desea repetir s/S:")#Opcion para evaluar si se realizara otra operacion
