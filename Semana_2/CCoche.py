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
    print("En espera...\n \n")
  def apagarCarro(self):
    print("El carro: "+self.modelo+" ha apagado.")
    print("En espera...\n \n")
  def ArrancarCarro(self):
    print("El carro: "+self.modelo+" ha arrancado.")
    print("En espera...\n \n")
  def frenarCarro(self):  
    print("El carro: "+self.modelo+" ha frenado.")
    print("En espera...\n \n")  

objCCoche=CCoche("Mustang","Ford",4,"Gasolina",342343,"Rojo",43343.23,"Famimilar",1000,250)
objCCoche.encenderCarro()
objCCoche.apagarCarro()
objCCoche.ArrancarCarro()
objCCoche.frenarCarro()