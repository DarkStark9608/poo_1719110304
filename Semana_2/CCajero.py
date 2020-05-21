class CCajero:
  idCajero=""
  ubicacion=""
  nombreCliente=""
  capacidad=0
  idCliente=""
  banco=""
  cantidadMaxima=0
  tipoPantalla="2"
  botones=""
  tarjeta=0
  saldo=0.0


  def __init__(self,idCajero,ubicacion,nombreCliente,capacidad,idCliente,banco,cantidadMaxima,tipoPantalla,tarjeta,seguridad,saldo):
    self.idCajero=idCajero
    self.ubicacion=ubicacion
    self.nombreCliente=nombreCliente
    self.capacidad=capacidad
    self.idCliente=idCliente
    self.banco=banco
    self.cantidadMaxima=cantidadMaxima
    self.tipoPantalla=tipoPantalla
    self.tarjeta=tarjeta
    self.seguridad=seguridad
    self.saldo=saldo

  def ingresarTarjeta(self):
    print("La tarjeta: "+str(self.tarjeta)+" se esta leyendo...")
    print("Espere un momento por favor...\n \n")
     
  def retirar(self):
        print(self.nombreCliente+" seleccione la cantidad a retirar\n \n")

  def cambiarNip(self):
    print(self.nombreCliente+" su cambio de nip esta procesando")
    print("Numero de tarjeta: "+ str(self.tarjeta))
  def mostrarMovimiento(self):
    print("Los movientos son: "+str(self.saldo))


objCajero= CCajero("FGDFGFDF232","CENTRO-CDMX","Oscar",2000,"fdffdRDZ","BBVA",17000,"LED",557901543456346754,"alta",12000)
objCajero.ingresarTarjeta()
objCajero.retirar()
objCajero.cambiarNip()
