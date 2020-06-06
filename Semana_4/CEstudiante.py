class CEstudiante:
  nombreEstudiante=""
  apellidoPaterno=""
  apellidoMaterno=""
  genero=""
  fechaNacimiento=""
  grupo=""
  matricula=0
  edad=0
  peso=0.0
  altura=0.0

  def __init__(self,nombreEstudiante, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, grupo, matricula, edad, peso, altura):
    self.nombreEstudiante=nombreEstudiante
    self.apellidoPaterno=apellidoPaterno
    self.apellidoMaterno=apellidoMaterno
    self.genero=genero
    self.fechaNacimiento=fechaNacimiento
    self.grupo=grupo
    self.matricula=matricula
    self.edad=edad
    self.peso=peso
    self.altura=altura

  def estudiar(self):
    print("El estudiante: "+self.nombreEstudiante +"self.apellidoPaterno"+ " "+self.apellidoMaterno+" esta estudiando.")
    
  def dormir(self):
    print("El estudiante: "+self.nombreEstudiante +"self.apellidoPaterno"+ " "+self.apellidoMaterno+" esta durmieno.")
  def hacerTarea(self):
    print("El estudiante: "+self.nombreEstudiante +"self.apellidoPaterno"+ " "+self.apellidoMaterno+" esta haciendo la tarea.")

class CUniversitario(CEstudiante):
  nombreEstudiante="David"
  apellidoPaterno="Rodriguez"
  apellidoMaterno="Marin"
  genero="Masculino"
  fechaNacimiento="08-01-1996"
  grupo="tic21"
  matricula=1719110303
  edad=24
  peso=77.0
  altura=1.71

  def __init__(self):
    print("Estudiante universitario")
  def estudiar(self):
    print(self.nombreEstudiante+"El estudiante esta estudiando online")
  def obtenerCedula(self):
    print("El estudiante: "+self.nombreEstudiante +"self.apellidoPaterno"+ " "+self.apellidoMaterno+" obtuvo su cedula profecional.")

objCEstudiante=CEstudiante("Oscar","Rodriguez","Marin","Hombre","08-01-1996","tic22",1719110304,24,77,1.70)
objCEstudiante.estudiar()
objCEstudiante.dormir()
objCEstudiante.hacerTarea()


objCUniversitario= CUniversitario()
objCUniversitario.estudiar()
objCUniversitario.dormir()
objCUniversitario.hacerTarea()


