import os
import math
#creamos nuestra clase
class CExcepcion:
  lista=[]
  numero=0.0

  def __init__(self,numero):
    self.numero=numero
  
  def guardarNumero(self):
    try:
      self.lista.append(self.numero)
    except Exception as error:
      print("Ingrese un dato valido")
      print("Error: "+ str(error.args))
      
  def imprimirNumeros(self):
    try:
      for i in range(len(self.lista)):
        print("Posicion: "+str(i )+" numero: "+str(self.lista[i]))
      seleccion_num=int(input("Ingresa la posicion del numero que deseas buscar:\n"))
      obj =CExcepcion(seleccion_num)
      obj.operarNumero(seleccion_num)
    except Exception as error:
      os.system("clear")
      print("Error"+ str(error.args))
      print("Ingresa una pocision correcta")
      obj =CExcepcion(0)
      obj.imprimirNumeros()  
  def operarNumero(self,numero):
    
    numero=self.lista[numero] 
    print("El numero que escogiste es : "+ str(numero))
    #Numero par
    if numero%2==0:
      print("El numero: "+str(numero) +" es par")
    else:
      print("No es par")
    
    raiz=math.sqrt(numero)
    print("La raiz cuadrada del numero: "+str(numero)+" es: "+str(raiz))
    cubo=numero**3
    print("El cubo del numero: "+str(numero)+" es :"+str(cubo))


total_num=int(input("Ingresa la cantidad de numeros a registrar\n"))
for i in range(total_num):    
  numero=float(input("Ingrese el numero:\n"))

  #creamos el objeto
  objExcepcion=CExcepcion(numero)
  #llamamos nuestros metods
  objExcepcion.guardarNumero()
objExcepcion.imprimirNumeros()
repetir=input("Desea repetir s/S:")
if repetir == "s" or repetir=="S":
  objExcepcion.imprimirNumeros()
    



