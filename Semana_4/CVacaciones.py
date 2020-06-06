class CVacaciones:
  tipoVacaciones=""
  duracion=""
  fechaInicio=""
  fechaFinal=""
  destino=""
  alojamiento=""
  transporte=""
  noPersonas=0
  tipoViaje=""
  intinirario=""
  
  def __init__(self,tipoVacaciones, duracion, fechaInicio, fechaFinal, destino, alojamiento, transporte, noPersonas, tipoViaje, itinirario):
    self.tipoVacaciones=tipoVacaciones
    self.duracion=duracion
    self.fechaInicio=fechaInicio
    self.fechaFinal=fechaFinal
    self.destino=destino
    self.alojamiento=alojamiento
    self.transporte=transporte
    self.noPersonas=noPersonas
    self.tipoViaje=tipoViaje
    self.intinirario=itinirario

  def iniciar(self):
    print(self.tipoVacaciones+" estan iniciando. \n \n")
    
  def finalizar(self):
    print(self.tipoVacaciones+" estan finalizando.\n \n")
  def reservar(self):
    print(self.tipoVacaciones+" estan resrevadas.\n \n")

class CSemanaSanta(CVacaciones):
  tipoVacaciones="Cuaresma"
  duracion="1 semana "
  fechaInicio="20 abril"
  fechaFinal="27 de abril"
  destino="Cancun"
  alojamiento="Hostal"
  transporte="Autobus"
  noPersonas=2
  tipoViaje="Aventureto"
  intinirario="Vistar la ribera Maya"

  def __init__(self):
    print("Vacaciones: "+self.tipoVacaciones)
  
  def divertirse(self):
    print(self.intinirario)
  def iniciar(self):
    print("Semana Santa ha comenzado")

objCVacaciones=CVacaciones("Navideñas","1 mes","10-12-2020","10-1-2021","Acapulco","Hotel","Avion",4,"Divertido","Visitar playas")
objCVacaciones.iniciar()
objCVacaciones.finalizar()
objCVacaciones.reservar()

objCCuaresma= CSemanaSanta()
objCCuaresma.iniciar()
objCCuaresma.finalizar()
objCCuaresma.reservar()
objCCuaresma.divertirse()