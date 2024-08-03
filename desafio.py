
''
import json
class CuentaBancaria :
   def __init__(self, titular_de_la_cuenta, numero_de_cuenta, dni, saldo) :
     self.dni = self.validar_dni=(dni)
     self.titular_de_la_cuenta = titular_de_la_cuenta,
     self.numero_de_cuenta = numero_de_cuenta,
     self.saldo = self.validar_saldo=(saldo)
     @property
     def dni(self):
       return self.dni
     @property
     def titular_de_la_cuenta(self):
      return self.titular_de_la_cuenta.capitalize()
     @property
     def numero_de_cuenta(self):
        return self.numero_de_cuenta
     @property
     def saldo(self):
        return self.saldo
     @saldo.setter
     def saldo(self, nuevo_saldo):
      self.saldo = self.validar_saldo(nuevo_saldo)

   def validar_dni(self, dni):
        try:
            dni_num = int(dni)
            if len(str(dni)) not in [7, 8]:
                raise ValueError("El DNI debe tener 8 dígitos.")
            if dni_num <= 0:
                raise ValueError("El DNI debe ser número positivo.")
            return dni_num
        except ValueError:
            raise ValueError("El DNI debe ser numérico y estar compuesto por 8 dígitos.")

   def validar_saldo(self, saldo):
        try:
            saldo_num = float(saldo)
            if saldo_num <= 0:
                raise ValueError("El saldo debe ser numérico positivo.")
            return saldo_num
        except ValueError:
            raise ValueError("El salario debe ser un número válido.") 

   def to__dict(self):
     return {
        "DNI" : self.dni,
        "Titular de la Cuenta" : self.titular_de_la_cuenta,
        "Número de Cuenta" : self.numero_de_cuenta,
        "Saldo":  self.saldo
     }
     

   def __str__(self):

    return f"(Se ha abierto la Cuenta Bancaria { self.numero_de_cuenta }, a nombre de  = {self.titular_de_la_cuenta}, {self.dni})"

class CuentaBancariaCorriente (CuentaBancaria) :
     def __init__(self, titular_de_la_cuenta,  numero_de_cuenta, dni, saldo):
      super().__init__(numero_de_cuenta, dni, saldo) 
      self.titular_de_la_cuenta : titular_de_la_cuenta

     @property
     def numero_de_cuenta(self):
      return self.numero_de_cuenta
     
     def Depositar(self, saldo):
        if saldo < 0:
           print("ERROR: monto no puede ser negativo")
        else:
         self.saldo += saldo
        print ("Se depositó {saldo} en la cuenta {self.numero_de_cuenta}. Nuevo saldo es {self.saldo}")


     def Retirar(self, saldo) :
        
       if saldo < 0:
           print("ERROR: el monto no puede ser negativo")
       elif saldo > self.saldo:  
        print("ERROR: fondos insuficientes")
       else:
            self.saldo += saldo
       print("Se retiró {saldo} en la cuenta {self.numero_de_cuenta}. Nuevo saldo es {self.saldo}")


     def Transferir(self, saldo, otra_cuenta):
       if saldo < 0:
           print("ERROR: el monto no puede ser negativo")
       elif saldo > self.saldo:
        print("ERROR: fondos insuficientes")
       if otra_cuenta not in CuentaBancaria:
        print("ERROR: Cuenta destino no existe.")
       else:
        self.saldo -= saldo 
       CuentaBancaria[otra_cuenta].saldo += saldo
       print("Se transfirió {saldo} en la cuenta {otra_cuenta}. Nuevo saldo es {self.saldo}")


   
class CuentaBancariaAhorro (CuentaBancaria) :
     def __init__(self, titular_de_la_cuenta,  numero_de_cuenta, dni, saldo):
      super().__init__(numero_de_cuenta, dni, saldo) 
      self.titular_de_la_cuenta : titular_de_la_cuenta

     @property
     def numero_de_cuenta(self):
      return self.numero_de_cuenta
     
     def to_dict(self):
        data = super().to_dict()
        data["CuentaBancaria"] = self.saldo
        return data

     def __str__(self):
        return f"{super().__str__()} - Cuenta Bancaria: {self.saldo}"


     def Depositar(self, saldo):
        if saldo < 0:
           print("ERROR: monto no puede ser negativo")
        else:
         self.saldo += saldo
        print ("Se depositó {saldo} en la cuenta {self.numero_de_cuenta}. Nuevo saldo es {self.saldo}")


     def Retirar(self, saldo) :
        
       if saldo < 0:
           print("ERROR: el saldo no puede ser negativo")
       elif saldo > self.saldo:  
        print("ERROR: fondos insuficientes")
       else:
            self.saldo += saldo
       print("Se retiró {saldo} en la cuenta {self.numero_de_cuenta}. Nuevo saldo es {self.saldo}")


     def Transferir(self, saldo, otra_cuenta):
       if saldo < 0:
           print("ERROR: el saldo no puede ser negativo")
       elif saldo > self.saldo:
        print("ERROR: fondos insuficientes")
       if otra_cuenta not in CuentaBancaria:
        print("ERROR: Cuenta destino no existe.")
       else:
        self.saldo -= saldo
       CuentaBancaria[otra_cuenta].saldo += saldo
       print("Se transfirió {saldo} en la cuenta {otra_cuenta}. Nuevo saldo es {self.saldo}")

class CuentasdeBancoCH:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                titular_de_la_cuenta = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return titular_de_la_cuenta

    def guardar_datos(self, titular_de_la_cuenta):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(titular_de_la_cuenta, file, indent=9)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')

    def crear_cliente(self, numero_de_cuenta, cliente):
        try:
            numero_de_cuenta = self.leer_datos()
            dni = cliente.dni
            if not str(dni) in numero_de_cuenta.keys():
                cliente[dni] = numero_de_cuenta.to_dict()
                self.guardar_numero_de_cuenta(numero_de_cuenta)
                print(f'Guardado exitoso')
            else:
                print(f'Colaborador con DNI {dni} ya existe')
        except Exception as error:
            print(f'Error inesperado al crear colaborador: {error}')


