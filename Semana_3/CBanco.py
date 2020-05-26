class CBanco:
  nombreBanco=""
  rfc=""
  nombreCliente=""
  tipoCuenta=""
  idCuenta=0
  saldo=0.0


  def __init__(self,nombreBanco, rfc, tipoCuenta,nombreCliente,idCuenta,saldo):
    self.nombreBanco=nombreBanco
    self.rfc=rfc
    self.nombreCliente=nombreCliente
    self.tipoCuenta=tipoCuenta
    self.idCuenta=idCuenta
    self.saldo=saldo
  
  def aperturarCuenta(self):
    print("Cuenta creada exitosamente")
    print("Banco: "+self.nombreBanco+"\nNombre del cliente: "+self.nombreCliente+"\nNumero de cliente: "+ str(self.idCuenta)+"\nTipo de cuenta: "+self.tipoCuenta+"\n \n")
     
  def cerrarCuenta(self):
    print("Cuenta cerrada exitosamente")
    print("Banco: "+self.nombreBanco+"\nNombre del cliente: "+self.nombreCliente+"\nNumero de cliente: "+ str(self.idCuenta)+"\nTipo de cuenta: "+self.tipoCuenta+"\n \n")
  def editarDatos(self):
    print("Cuenta editada exitosamente")
    print("Banco: "+self.nombreBanco+"\nNombre del cliente: "+self.nombreCliente+"\nNumero de cliente: "+ str(self.idCuenta)+"\nTipo de cuenta: "+self.tipoCuenta+"\n \n")
  def consultarSaldo(self):
    print("Saldo consultado exitosamente")
    print("Banco: "+self.nombreBanco+"\nNombre del cliente: "+self.nombreCliente+"\nNumero de cliente: "+ str(self.idCuenta)+"\nTipo de cuenta: "+self.tipoCuenta+"\nSaldo: "+str(self.saldo)+"\n \n")

class CBancomer(CBanco):
  def __init__(self):
    self.nombreBanco=CBanco.nombreBanco
    self.rfc=CBanco.rfc
    self.nombreCliente=CBanco.nombreCliente
    self.tipoCuenta=CBanco.tipoCuenta
    self.idCuenta=CBanco.idCuenta
    self.saldo=CBanco.saldo
    print("Bancomer")

objBanco= CBanco("BBVA","SDFGJ2390TH4-BBVA","Nomina","Oscar",1719110304,8212.12)
objBanco.aperturarCuenta()
objBanco.cerrarCuenta()
objBanco.consultarSaldo()
objBanco.editarDatos()

objBancomer=CBancomer()
objBancomer.aperturarCuenta()
objBancomer.cerrarCuenta()
objBancomer.consultarSaldo()
objBancomer.editarDatos()