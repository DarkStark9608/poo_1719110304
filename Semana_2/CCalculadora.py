class CCalculadora:
  numeroa=0.0
  numerob=0.0
  resultado=0.0
  tipooperacion=""
  base=""
  forma=""
  color=""
  tipocalculadora=""
  tipobateria=""


  def __init__(self,numeroa,numerob,resultado,tipooperacion,base,forma,color,tipocalculadora,tipobateria):
    self.numeroa=numeroa
    self.numerob=numerob
    self.resultado=resultado
    self.tipooperacion=tipooperacion
    self.base=base
    self.forma=forma
    self.color=color
    self.tipocalculadora=tipocalculadora
    self.tipobateria=tipobateria
    

  def suma(self):
    self.resultado=self.numeroa+self.numerob
    print("El resultado de la suma es: "+ str(self.resultado))
     
  def resta(self):
    self.resultado=self.numeroa-self.numerob
    print("El resultado de la suma es: "+ str(self.resultado))
  def multiplicacion(self):
    self.resultado=self.numeroa*self.numerob
    print("El resultado de la suma es: "+ str(self.resultado))
     
  def division(self):
    self.resultado=self.numeroa/self.numerob
    print("El resultado de la suma es: "+ str(self.resultado))

  


objCCalculadora= CCalculadora(10,22.2,0,"Resta","10","Cuadrado","Azul","Cientifica","AAA")

objCCalculadora.suma()
objCCalculadora.resta()
objCCalculadora.division()
objCCalculadora.multiplicacion()
