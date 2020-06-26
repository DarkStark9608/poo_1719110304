#Creacion de la clase
class CCifradoArchivo:
  
  def __init__(self):#ctr
    pass
    #metodo para leer el archivo
  def LeerArchivo(self,archivo):
    #Creo mis variables
    cadena=""
    cifrarArchivo=""
    cifrarCadena=""
    file= open (archivo, 'r')#Creo mis archivo 
        for caracter in file: #Utilizo un  for para recorrer mi archivo
      cadena+=caracter#Concateno mi archivo en una sola linea
    print("El archivo original es: "+cadena)#Lo imprimo
    for caracter in cadena:#Leemos la cadena
      numAlfabeto= ord(caracter) #Obtenemos el caracter del codigo acsii
      cifrarCadena += chr(numAlfabeto +3)#Ciframos la cadena
    print(cifrarCadena) #Imprimimos la cadena cifrada
  
  #metodo para descifrar
  def descifrarArchivo(self,archivo):
    #Creamos variables
    descifrarCadena=""
    cadena=""
    file= open (archivo, 'r')#Creo mis archivo 
        for caracter in file: #Utilizo un  for para recorrer mi archivo
      cadena+=caracter#Concateno mi archivo en una sola linea
    print("El archivo original es: "+cadena)#Lo imprimo
    for caracter in cadena:#Leemos la cadena
      numAlfabeto= ord(caracter) #Obtenemos el caracter del codigo acsii
      cifrarCadena += chr(numAlfabeto -3)#desciframos la cadena
    print(cifrarCadena) #Imprimimos la cadena cifrada
    
#Menu
repetir="s"
while repetir=="s" or repetir=="S":#Se realizara mientras el usuario diga que si
  
  opcion=input("Ingresa 1) Para encriptar: \nIngresa 2) Para descifrar\n")#el uuario selecciona que desea realizar  
  objCesar=CCifradoArchivo()# Apartir de la opcion que desea realizar evaluara y realizara ya sea:
  if opcion=="1":#Cifrar
  
    objCesar.LeerArchivo("archivo.txt")#El archivo sera este donde viene la cadena normal
  elif opcion=="2":#Descifrar
    objCesar.descifrarArchivo("archivoCifrado.txt")#Viene una cadena cifrada y buscamos volverla a la normalidad
  else:#Un pequeño flitro
    print("Valor incorrecto")#un pequeño filtro
    break
  repetir=input("Desea repetir s/S:")#Opcion para evaluar si se realizara otra operacion
