# Herencia.
from os import system
system("cls")

class Cuenta ():

    def __init__(self, titular, cantidad):
        self.titular=titular
        self.cantidad=cantidad

    def imprime(self): 
         print('Class Cuenta')
         print(self.titular,self.cantidad)
         print()

class PlazoFijo (Cuenta):
  
    def imprime(self): 
         print('Class Plazo Fijo')
         print(self.titular,self.cantidad) 

class Caja_Ahorro(Cuenta):
          
    def __init__(self, plazo, interes, titular, cantidad):
            super().__init__(titular, cantidad)
            self.plazo = plazo
            self.interes = interes
        
    def imprime(self):
            print('Class Plazo Fijo')
            print(self.titular,self.cantidad,self.plazo,self.interes)
    
    def calculo(self):
        print()
        print("Caja de  Ahorro")
        print ("Titular :",self.titular,"Interes cobrado  :",(self.cantidad*self.interes)/100,"pesos")
        
        



luis=Cuenta ('Luis', 500000)

catalina=PlazoFijo('catalina',70000)

roberto=Caja_Ahorro(30,2,'Roberto', 2000)



luis.imprime()

catalina.imprime()


roberto.calculo()
