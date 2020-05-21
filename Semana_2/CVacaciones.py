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

objCVacaciones=CVacaciones("Navideñas","1 mes","10-12-2020","10-1-2021","Acapulco","Hotel","Avion",4,"Divertido","Visitar playas")

objCVacaciones.iniciar()
objCVacaciones.finalizar()
objCVacaciones.reservar()