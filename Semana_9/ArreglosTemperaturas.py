#Creamos la clase
class ArreglosTemperatura:
  #creamos su variables 
  centigrados=0
  fahrenheit=0
  promedioCenti=0
  promedioFare=0
  arreglo=[]
  fecha=""
  #Creamos un constructor
  def __init__(self):
    pass
#Creamos el metodo para leer la temperatura y convertirala a fahrenheit
  def leerTemperatura(self,centigrados,fecha):
    #Recibimos la temperatura como parametro y la igualamos como propiedad en nuestra clase
    self.centigrados=centigrados
    #Convertimos la temperatura a fahenheit
    self.fahrenheit=(self.centigrados*1.8)+32
    self.fecha=fecha
   
#Metodo para guardar la temperatura
  def guardarTemperatura(self,archivo):
    #recibimos como parametro el archivo txt y lo creamos en modo de escritura 
    file=open(archivo, 'a')
    #Convertimos nuestras variables en cadenas para poder darles formato
    self.fecha=self.fecha+"\n"
    variable=str(self.centigrados)+", "+str(self.fahrenheit)+", "+str(self.fecha)
    #Guardamos nuestras variables en el archivo
    file.write(variable)
    #Se cierra el archivo
    file.close()
    
    #metodo leer archivo
  def leerArchivo(self,archivo):
    #Creo un contador
   #Creamos y abrimos el archivo en modo de lectura
    file=open(archivo, 'r')
    #leemos el archivo con un for 
    for line in file:
      #Damos formato para agregar los datos a nuestro arreglo
      formato=line.replace("\n","")
    #Lo agregamos al arreglo
      self.arreglo.append(formato.split(","))
    #Al terminar de leer el archivo lo cerramos
    file.close()
    
    
    #definimos un metodo  para obtener los valores maximos en nuestra lista 
  def valorMaximo(self) :
      maximo_lista=0
      #leamos nuestro arreglo en una columna especifica
      for i in range(len(self.arreglo)):
        #asignamos el valor de la dicha pocision
        prueba=self.arreglo[i][0]
        #le damos formato
        prueba=int(prueba)
        #y evaluamos si es mayor que el anterior ingresado
        if prueba>maximo_lista:
            maximo_lista=prueba
            #aca obtenemos el valor de la fila con la temperatura mas alta
            ind=self.arreglo[i]
      print("La temperatura mas alta registrada es: ")

      print(ind)
      #Creamos un metodo para obtener el promedio de las temperaturas
  def calcularPromedios(self):
      #leemos el arreglo 
      cont=0
      for i in range(len(self.arreglo)):
          #Obtenemos el valor de la pocicion y lo vamos sumando 
          prueba=self.arreglo[i][0]
          prueba=int(prueba)
          self.promedioCenti+=prueba
          cont=cont+1
          #obtnemos el promedio
      self.promedioCenti=self.promedioCenti/cont
      print("El promedio en grados centigrados es: "+str(self.promedioCenti))
      cont2=0
      for i in range(len(self.arreglo)):
          prueba=self.arreglo[i][1]
          prueba=float(prueba)
          self.promedioFare+=prueba
          cont2=cont2+1
      self.promedioFare=self.promedioFare/cont2
      print("El promedio en grados fahrenheit es: "+str(self.promedioFare))
    
#Menu
repetir="s"
while repetir=="s" or repetir=="S":#Se realizara mientras el usuario diga que si
  
    #Pedimos la temperatura
  temperatura=int(input("Ingresa la temperatura que deseas convertir\n"))  
  fecha=input("Ingresa la fecha\n")
  #creamos el objeto
  objtemperatura=ArreglosTemperatura()
  #llamamos nuestros metods
  objtemperatura.leerTemperatura(temperatura,fecha)
  objtemperatura.guardarTemperatura("temperatura.txt")

  repetir=input("Desea repetir s/S:")
  if repetir != "s" and repetir!="S":#Opcion para evaluar si se realizara otra operacion o imprimir las temperaturas
    #llamamos nuestros metodos
    objtemperatura.leerArchivo("temperatura.txt")
    objtemperatura.valorMaximo()
    objtemperatura.calcularPromedios()

