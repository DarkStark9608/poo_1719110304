class CCoche:
  modelo=""
  marca="" 
  capacidad=4
  tipoCombustible="" 
  idMatricula=""
  color =""
  precio=0.0
  tipoCoche=""
  Peso =0
  velMaxima=0.0
  def __init__(self,modelo, marca, capacidad, tipoCombustible, idMatricula, color, precio, tipoCoche, Peso, velMaxima):
    self.modelo=modelo
    self.marca=marca
    self.capacidad=capacidad
    self.tipoCombustible=tipoCombustible
    self.idMatricula=idMatricula
    self.color=color
    self.precio=precio
    self.tipoCoche=tipoCoche
    self.Peso=Peso
    self.velMaxima=velMaxima

  def encenderCarro(self):
    print("El carro: "+self.modelo+" ha encendido.")
    print("En espera...\n ")
  def apagarCarro(self):
    print("El carro: "+self.modelo+" ha apagado.")
    print("En espera...\n ")
  def ArrancarCarro(self):
    print("El carro: "+self.modelo+" ha arrancado.")
    print("En espera...\n ")
  def frenarCarro(self):  
    print("El carro: "+self.modelo+" ha frenado.")
    print("En espera...\n ")  

class Deportivo(CCoche):
  modelo="Camaro"
  marca="Chevrolet" 
  capacidad=4
  tipoCombustible="Gasolina" 
  idMatricula=3434324
  color ="Verde"
  precio=500000.0
  tipoCoche="Deportivo"
  Peso =1000
  velMaxima=350.0

  def __init__(self):
    print("Coche deportivo")

  def cargarCombustible(self):  
    print("El coche esta cargando gasolina: "+self.modelo)
  def frenarCarro(self):  
    print("El carro esta frenando con sus frenos de disco")
    print("El carro: "+self.modelo+" ha frenado.")
    

objCCoche=CCoche("Mustang","Ford",4,"Gasolina",342343,"Rojo",43343.23,"Famimilar",1000,250)
objCCoche.encenderCarro()
objCCoche.apagarCarro()
objCCoche.ArrancarCarro()
objCCoche.frenarCarro()


objCamraro=Deportivo()
objCamraro.encenderCarro()
objCamraro.apagarCarro()
objCamraro.ArrancarCarro()
objCamraro.frenarCarro()
objCamraro.cargarCombustible()