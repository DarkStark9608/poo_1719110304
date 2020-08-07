#creamos nuestra calse
class CPeliculas:
     #creamos su variables 
  nombre=""
  fecha_estreno=""
  genero=""
  arreglo=[]
#creamos el crt
  def __init__(self,nombre,fecha_estreno,genero):
      #igualamos variables
      self.nombre=nombre
      self.fecha_estreno=fecha_estreno
      self.genero=genero
  #metodo para guardar la pelicula en un arreglo
  def guardarPelicula(self):
    #creamos una varible que es guarda un arreglo
      variable=[self.nombre, self.fecha_estreno,self.genero]
      #guardamos la variable en el objeto
      self.arreglo.append(variable)

      #metodo para imorimir el arreglo
  def imprimirPelicula(self):
    #corremos un for y lo imprimimos
      for i in self.arreglo:
          print(i)
          #metodo para buscar un genero
  def buscarGenero(self):
      #se le pide al usuario el genero
      seleccion_genero=input("Ingresa el genero que deseas buscar\n")
    #con un for se buasca el genero sabiendo que el genero esta en i,2 en nuestro arreglo
      for i in range(len(self.arreglo)):
                   
          if  self.arreglo[i][2]== seleccion_genero:
              print (self.arreglo[i])
      

#Menu
repetir="s"
while repetir=="s" or repetir=="S":#Se realizara mientras el usuario diga que si
  
    #Pedimos los datos del alumno
  nombre=input("Ingrese el nombre de la pelicula:\n")  
  fecha=input("El año de lanzamiento\n")
  genero=input("Ingresa el genero:\n")
  #creamos el objeto
  objPelicula=CPeliculas(nombre,fecha,genero)
  #llamamos nuestros metods
  objPelicula.guardarPelicula()

  repetir=input("Desea repetir s/S:")
  if repetir != "s" and repetir!="S":#Opcion para evaluar si se realizara 
    #llamamos nuestros metodos
    
    objPelicula.imprimirPelicula()
    objPelicula.buscarGenero()


