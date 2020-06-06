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
  nombreBanco="Bancomer"
  rfc="DA32DFBBVA"
  nombreCliente="David"
  tipoCuenta="Credito"
  idCuenta=1719110304
  saldo=2343.21
  
  def __init__(self):
    pass
  def depositarCuenta(self):
    print("Transferencia exitosa "+ str(self.idCuenta))
  def consultarSaldo(self):
    idCuentaaux=int(input("Ingresa tu numero de cuenta:\n"))
    if idCuentaaux==self.idCuenta:
      print("Saldo consultado exitosamente")
      print("Banco: "+self.nombreBanco+"\nNombre del cliente: "+self.nombreCliente+"\nNumero de cliente: "+ str(self.idCuenta)+"\nTipo de cuenta: "+self.tipoCuenta+"\nSaldo: "+str(self.saldo)+"\n \n")
    else:
      print("Incorrecto")

objBanco= CBanco("BBVA","SDFGJ2390TH4-BBVA","Nomina","Oscar",1719110304,8212.12)
objBanco.aperturarCuenta()
objBanco.cerrarCuenta()
objBanco.consultarSaldo()
objBanco.editarDatos()

objBancomer=CBancomer()
objBancomer.aperturarCuenta()
objBancomer.cerrarCuenta()
objBancomer.editarDatos()
objBancomer.depositarCuenta()
objBancomer.consultarSaldo()