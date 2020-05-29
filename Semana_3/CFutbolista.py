class CFutbolista:
  nombreFutbolista=""
  apellidoPaternoFutbolista=""
  apellidoMaternoFutbolista=""
  genero=""
  fechaNacimiento=""
  equipo=""
  identificador=0
  edad=0
  peso=0.0
  altura=0.0

  def __init__(self,nombreFutbolista, apellidoPaternoFutbolista, apellidoMaternoFutbolista, genero, fechaNacimiento, equipo, matricula, edad, peso, altura):
    self.nombreFutbolista=nombreFutbolista
    self.apellidoPaternoFutbolista=apellidoPaternoFutbolista
    self.apellidoMaternoFutbolista=apellidoMaternoFutbolista
    self.genero=genero
    self.fechaNacimiento=fechaNacimiento
    self.equipo=equipo
    self.matricula=matricula
    self.edad=edad
    self.peso=peso
    self.altura=altura

  def entrenar(self):
    print(self.nombreFutbolista +" "+self.apellidoPaternoFutbolista+" "+self.apellidoMaternoFutbolista+" "+" esta entrenando. \n \n")
    
  def anotar(self):
    print(self.nombreFutbolista +" "+self.apellidoPaternoFutbolista+" "+self.apellidoMaternoFutbolista+" "+" ha metido gooool.\n \n")
  def jugarFutbol(self):
    print("El estudiante: "+self.nombreFutbolista +"self.apellidoPaterno"+ " "+self.apellidoMaternoFutbolista+" esta jugando futbol.\n \n")

class CFutbolistaJR(CFutbolista):
  nombreFutbolista="Juan"
  apellidoPaternoFutbolista="Lpoez"
  apellidoMaternoFutbolista="Soto"
  genero="Masculino"
  fechaNacimiento=""
  equipo="RM"
  identificador=21345
  edad=24
  peso=74.6
  altura=180.0

  def __init__(self):
    print("Futbolista JR")
  def calentar(self):
    print(self.nombreFutbolista+" esta calentando")  


objFutbolista=CFutbolista("Oscar","Rodriguez","Marin","Hombre","08-01-1996","Real Madrid",1719110304,24,77,1.70)
objJr= CFutbolistaJR()

objFutbolista.anotar()
objFutbolista.entrenar()
objFutbolista.jugarFutbol()

objJr.anotar()
objJr.entrenar()
objJr.jugarFutbol()
objJr.calentar()