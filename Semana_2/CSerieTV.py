class CSerieTv:

  nombreSerie=""
  duracion=""
  noCapitulo=0
  noTemporadas=0
  personajes=""
  genero=""
  productor=""
  director=""
  audiencia=""
  televisora=""
    

  def __init__(self,nombreSerie, duracion, noCapitulo, noTemporadas, personajes, genero, productor, director, audiencia, televisora):
    self.nombreSerie=nombreSerie
    self.duracion=duracion
    self.noCapitulo=noCapitulo
    self.noTemporadas=noTemporadas
    self.personajes=personajes
    self.genero=genero
    self.productor=productor
    self.director=director
    self.audiencia=audiencia
    self.televisora=televisora

  def empezar(self):
    print(self.nombreSerie+" esta reproduciendo. \n \n")
    
  def pausar(self):
    print(self.nombreSerie+" esta pausado.\n \n")
  def terminar(self):
    print(self.nombreSerie+" esta jugando terminada.\n \n")
objCSerie=CSerieTv("Rick and Morty","20 minutos",5,4, "animados","caricaturas","rick´s","diversion","alta","Online")

objCSerie.empezar()
objCSerie.pausar()
objCSerie.terminar()