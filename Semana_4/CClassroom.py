import datetime
class CClassroom:
  materias=""
  tipoUsuario=""
  nombreUsuario=""
  tareas=""
  calendario=datetime.datetime.now()
  rubricas=""
  aula=""
  trabajos=""
  calificacion=0.0

  def __init__(self,materias,nombreUsuario, tipoUsuario, tareas, calendario, rubricas, aula, trabajos, calificacion):
    self.nombreUsuario=nombreUsuario
    self.materias=materias  
    self.tipoUsuario=tipoUsuario
    self.tareas=tareas
    self.calendario=calendario
    self.rubricas=rubricas
    self.aula=aula
    self.trabajos=trabajos
    self.calificacion=calificacion

  def ingresarSesion(self):
    print("Iniciando sesion...\n"+self.nombreUsuario+"\n \n")
     
  def entregarTrabajo(self):
    print("La tarea: "+self.tareas+" ha sido entregada")
    print(str(self.calendario) + "\n \n")

  def calificarTarea(self):
    print("La tarea: "+self.tareas+" ha sido calificada")
    print("Calificacion: "+str(self.calificacion)+"\n \n")

class CClassroom1(CClassroom):
  materias="Programacion"
  nombreUsuario="Juan"
  tipoUsuario="Profesor"
  tareas="2.4"
  calendario=datetime.datetime.now()
  rubricas="Digital"
  aula="Lab"
  trabajos="Trabajo"
  calificacion=10.0
  fecha=datetime.datetime.now()

  def __init__(self):
    print("Classroom 1:")
  
  def crearTarea(self):
    print("Tarea creada ")
  def ingresarSesion(self):
    print("Iniciando sesion...\n"+self.nombreUsuario+"\n" +self.tipoUsuario +"\n")

fecha=datetime.datetime.now()
objClassroom=CClassroom("Ingles","Oscar David","Estudiante","2.3 Creacion de clases",fecha,"Estricto","C23","tareas",9.2)
objClassroom.ingresarSesion()
objClassroom.calificarTarea()
objClassroom.entregarTrabajo()

objClassroom1=CClassroom1()
objClassroom1.ingresarSesion()
objClassroom1.calificarTarea()
objClassroom1.entregarTrabajo()
objClassroom1.crearTarea()
  