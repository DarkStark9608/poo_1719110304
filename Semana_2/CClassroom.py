import datetime

class CClassroom:

  materias=""
  nombreAlumno=""
  nombreProfesores=""
  tareas=""
  calendario=datetime.datetime.now()
  rubricas=""
  aula=""
  trabajos=""
  calificacion=0.0


  def __init__(self,materias, nombreAlumno, nombreProfesores, tareas, calendario, rubricas, aula, trabajos, calificacion):
    
    self.materias=materias  
    self.nombreAlumno=nombreAlumno
    self.nombreProfesores=nombreProfesores
    self.tareas=tareas
    self.calendario=calendario
    self.rubricas=rubricas
    self.aula=aula
    self.trabajos=trabajos
    self.calificacion=calificacion

  def ingresarSesion(self):
    print("Iniciando sesion...\n"+self.nombreAlumno+"\n \n")
     
  def entregarTrabajo(self):
    print("La tarea: "+self.tareas+" ha sido entregada")
    print(str(self.calendario) + "\n \n")

  def calificarTarea(self):
    print("La tarea: "+self.tareas+" ha sido calificada")
    print("Calificacion: "+str(self.calificacion)+"\n \n")
  
fecha=datetime.datetime.now()
objClassroom=CClassroom("Ingles","Oscar David","Salvador","2.3 Creacion de clases",fecha,"Estricto","C23","tareas",9.2)
objClassroom.ingresarSesion()
objClassroom.calificarTarea()
objClassroom.entregarTrabajo()

  