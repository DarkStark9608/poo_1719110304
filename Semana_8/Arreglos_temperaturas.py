#Creamos la clase
class ConversionTemperatura:
  #creamos su variables 
  centigrados=0
  fahrenheit=0
  promedioCenti=0
  promedioFare=0
  #Creamos un constructor
  def __init__(self):
    pass
#Creamos el metodo para leer la temperatura y convertirala a fahrenheit
  def leerTemperatura(self,centigrados):
    #Recibimos la temperatura como parametro y la igualamos como propiedad en nuestra clase
    self.centigrados=centigrados
    #Convertimos la temperatura a fahenheit
    self.fahrenheit=(self.centigrados*1.8)+32
    
#Metodo para guardar la temperatura
  def guardarTemperatura(self,archivo):
    #recibimos como parametro el archivo txt y lo creamos en modo de escritura 
    file=open(archivo, 'a')
    #Convertimos nuestras variables en cadenas para poder darles formato
    self.centigrados=str(self.centigrados)+"\n"
    self.fahrenheit=str(self.fahrenheit)+"\n"
    #Guardamos nuestras variables en el archivo
    file.write(str(self.centigrados))
    file.write(str(self.fahrenheit))
    #Se cierra el archivo
    file.close()
    
    #metodo leer archivo
  def leerArchivo(self,archivo):
    #Creo un contador
    cont=0
    #Creamos y abrimos el archivo en modo de lectura
    file=open(archivo, 'r')
    #leemos el archivo con un for
    for line in file:
      #como en el archivo guardamos un valor en una linea y en otro el valor de otro aqui los obtendremos
      #Con eso obtendremos el promedio  
      if cont %2==0:
          self.promedioCenti+=float(line)
      else:
          self.promedioFare+=float(line)
      #Aumentamos nuestro contador conforme el for da un ciclo 
      cont+=1
      #Al terminar de leer los valores se cierra el for 
    file.close()
    #Como son dobles valores se cierra
    cont=cont/2
    #Calculamos los promedios
    self.promedioCenti=self.promedioCenti/cont
    self.promedioFare=self.promedioFare/cont
    #Imprimimos los promedios
    print("El promedio en fahrenheit es: "+str(self.promedioFare))
    print("El promedio en celcius es :"+str(self.promedioCenti))


    
#Menu
repetir="s"
while repetir=="s" or repetir=="S":#Se realizara mientras el usuario diga que si

  
    #Pedimos la temperatura
  temperatura=int(input("Ingresa la temperatura que deseas convertir\n"))  
  #creamos el objeto
  objtemperatura=ConversionTemperatura()
  #llamamos nuestros metods
  objtemperatura.leerTemperatura(temperatura)
  objtemperatura.guardarTemperatura("temperatura.txt")

  
  
  
  repetir=input("Desea repetir s/S:")
  if repetir != "s" and repetir!="S":#Opcion para evaluar si se realizara otra operacion o imprimir las temperaturas
    objtemperatura.leerArchivo("temperatura.txt")



