class CAvion:
  nombreAvion=""
  modelo=""
  velocidad=0.0
  tipoAvion=""
  alturaMinima=0.0
  alturaMaxima=0.0
  Capacidad=0
  Aerolinea=""
  Marca=""
  idAvion=""

  def __init__(self,nombreAvion,modelo,velocidad,tipoAvion,alturaMaxima,alturaMinima,Capacidad,Aerolinea,Marca,idAvion):
    self.nombreAvion=nombreAvion
    self.modelo=modelo
    self.velocidad=velocidad
    self.tipoAvion=tipoAvion
    self.alturaMinima=alturaMinima
    self.alturaMaxima=alturaMaxima
    self.Capacidad=Capacidad
    self.Aerolinea=Aerolinea
    self.Marca=Marca
    self.idAvion=idAvion
  
  def encenderAvion(self):
    print("El avion: "+self.nombreAvion+" ha encendido.")
    print("En espera...\n \n")
  def apagarAvion(self):
    print("El avion: "+self.nombreAvion+" ha apagado.")
    print("En espera...\n \n")
  def despegarAvion(self):
    print("El avion: "+self.nombreAvion+" ha depegado.")
    print("En espera...\n ")
  def aterrizarAvion(self):
    print("El avion: "+self.nombreAvion+" ha aterrizado.")
    print("En espera...\n")
  def llenarAvion(self):  
    print("El avion: "+self.nombreAvion+" ha esta cargando pasajeros")
    print("En espera...\n ")

class AvionComercial(CAvion):
  nombreAvion="Volaris"
  modelo="2017"
  velocidad=350.0
  tipoAvion="Privado"
  alturaMinima=1500.0
  alturaMaxima=500.0
  Capacidad=500.0
  Aerolinea="Volaris"
  Marca="Volaris"
  idAvion="LKSSKJ-VOLARIS"

  def __init__(self):
    print("Avion: "+ self.idAvion)
  
  def cargarConbustible(self):
    print("El avion: "+self.nombreAvion+" esta cargando combusible")
#Aqui el polimorfismo
  def llenarAvion(self):  
    print("El avion: "+self.nombreAvion+" ha esta cargando mercancia")
    print("En espera...\n ")  
#Aca termino
objCAvion= CAvion("Avioncito","2020",400.14,"Comercial",1000,15000,300,"Volaris","Airbus","DFVBVMK2242-AVIONCITO")
objCAvion.encenderAvion()
objCAvion.despegarAvion()
objCAvion.aterrizarAvion()
objCAvion.llenarAvion()
objCAvion.apagarAvion()

objVolarisCAvion= AvionComercial()
objVolarisCAvion.encenderAvion()
objVolarisCAvion.despegarAvion()
objVolarisCAvion.aterrizarAvion()
objVolarisCAvion.llenarAvion()
objVolarisCAvion.apagarAvion()
objVolarisCAvion.cargarConbustible()
