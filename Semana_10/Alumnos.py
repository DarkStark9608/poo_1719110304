#Impotamos datetime 
import datetime
#Creamos la clase
class CAlumnos:
  #creamos su variables 
  nombre=""
  fecha_nacimiento=""
  grupo=""
  arreglo=[]
  
  #Creamos un constructor
  def __init__(self,nombre,fecha_nacimiento,grupo):
    #igualamos las varialbes
    self.nombre=nombre
    self.fecha_nacimiento=fecha_nacimiento
    self.grupo=grupo

#Metodo para guardar los datos del alumno
  def guardarAlumno(self,archivo):
    #recibimos como parametro el archivo txt y lo creamos en modo de escritura 
    file=open(archivo, 'a')
    #Convertimos nuestras variables en cadenas para poder darles formato
    self.grupo=self.grupo+"\n"
    variable=str(self.nombre)+", "+str(self.fecha_nacimiento)+", "+str(self.grupo)
    #Guardamos nuestras variables en el archivo
    file.write(variable)
    #Se cierra el archivo
    file.close()
    
    #metodo leer archivo
  def leerAlumno(self,archivo):
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
  def calcularEdad(self) :
      aux=[]
      #leamos nuestro arreglo en una columna especifica
      for i in range(len(self.arreglo)):
        #asignamos el valor de la dicha pocision
        prueba=self.arreglo[i][1]
        self.nombre=self.arreglo[i][0]
        #comenzamos a leer la palabra en partes 
        #para obtener el año, mes y dia
        año=prueba[7:11]
        año=int(año)
        
        mes=prueba[4:6]
        mes=int(mes)
        dia=prueba[1:3]
        dia=int(dia)
        #lso valores los convertiimos a fecha
        año_nacimiento=datetime.date(año,mes,dia)
        #obtenemos hoy
        hoy=datetime.date.today()
      #hacemoso la operacion de fechas
        edad=hoy-año_nacimiento
 #la convertimos a string y le damos formato
        edad=str(edad)
        edad=edad.split(" ")
        cont=0
        #leemos la palabra con un for para obtener e numero de dias y l agregamos en una nueva lista
        for x in edad:
            if cont==0:
                x=x
                x=int(x)
                x=x//365
                var=[self.nombre+ ", "+str(x) ]
                aux.append(var)
                
            cont+=1
            #imprimimos la lista
      for i in aux:
          print(i)
      
  
#Menu
repetir="s"
while repetir=="s" or repetir=="S":#Se realizara mientras el usuario diga que si
  
    #Pedimos los datos del alumno
  nombre=input("Ingrese el nombre del alumno:\n")  
  fecha=input("Ingresa la fecha de nacimiento en formato DD/MM/AAAA\n")
  grupo=input("Ingresa el grupo del alumno:\n")
  #creamos el objeto
  objtemperatura=CAlumnos(nombre,fecha,grupo)
  #llamamos nuestros metods
  objtemperatura.guardarAlumno("Alumnos.txt")

  repetir=input("Desea repetir s/S:")
  if repetir != "s" and repetir!="S":#Opcion para evaluar si se realizara otra operacion o imprimir las temperaturas
    #llamamos nuestros metodos
    objtemperatura.leerAlumno("Alumnos.txt")
    objtemperatura.calcularEdad()


