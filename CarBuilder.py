from abc import ABC, abstractclassmethod

class Car(ABC): #Interface Car
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> None:
        pass
    
    @abstractclassmethod
    def set_marca(self) -> None:
        pass
    
    @abstractclassmethod
    def set_modelo(self) -> None:
        pass
    
    @abstractclassmethod
    def set_cor(self) -> None:
        pass
    
    @abstractclassmethod
    def set_numero_de_portas(self) -> None:
        pass
    
    @abstractclassmethod
    def set_aro(self) -> None:
        pass
    
    @abstractclassmethod
    def set_motor(self) -> None:
        pass
    
    @abstractclassmethod
    def set_chassi(self) -> None:
        pass
    
    @abstractclassmethod
    def reset(self) -> None:
        pass
    
    @abstractclassmethod
    def build(self) -> None:
        pass
    

#Exemplo de ConcreateBuilder
#Cada concreate builder pode ter variações, como
#CarBuilder, CarManualBuilder, CarModelerBuilder
#como esta exemplificado no diagrama UML de classes

class CarBuilder(Car):
    def __init__(self, car: Car, marca: str, modelo: str, cor: str, numero_de_portas: int, aro: int, motor: str, chassi: str):
        self.__car = car
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__numero_de_portas = numero_de_portas
        self.__aro = aro
        self.__motor = motor
        self.__chassi = chassi
    
    @property
    def car(self):
        return self.__car
    
    @car.setter
    def car(self, car: Car):
        self.__car = Car 
        
    @property   
    def set_marca(self):
        return self.__marca
    
    @set_marca.setter
    def set_marca(self, marca: str):
        self.car.__marca = marca
    
    @property
    def set_modelo(self, ):
        return self.__modelo
    
    @set_modelo.setter
    def set_modelo(self, modelo: str):
        self.car.__modelo = modelo
    
    @property
    def set_cor(self):
        return self.__cor
    
    @set_cor.setter
    def set_cor(self, cor: str):
        self.car.__cor = cor

    @property
    def set_numero_de_portas(self):
        return self.__numero_de_portas
    
    @set_numero_de_portas.setter
    def set_numero_de_portas(self, numero_de_portas: int):
        self.car.__numero_de_portas = numero_de_portas
        
    @property
    def set_aro(self, aro):
        return self.__aro
    
    @set_aro.setter
    def set_aro(self, aro: int):
        self.car.__aro = aro
    
    @property
    def set_motor(self):
        return self.__motor
    
    @set_motor.setter
    def set_motor(self, motor: str):
        self.car.__motor = motor
    
    @property
    def set_chassi(self):
        return self.__chassi
    
    @set_chassi.setter
    def set_chassi(self, chassi):
        self.car.__chassi = chassi

    def build(self):
        car1 = self.car
        self.reset()
        return car1
    
    def reset(self):
        self.car.marca = None
        self.car.modelo = None
        self.car.cor = None
        self.car.numero_de_portas = None
        self.car.aro = None
        self.car.motor = None
        self.car.chassi = None
        
        return self.car
    
    
class Director():
    def __init__(self) -> None:
        self.__builder = None
    
    @property
    def builder(self) -> CarBuilder:
        return self.__builder
    
    @builder.setter
    def builder(self, builder: CarBuilder) -> None:
        self.__builder = builder        
    
    def build_sedan(self) -> None:
        self.__builder.set_marca("Toyota") 
        self.__builder.set_modelo("Corolla") 
        self.__builder.set_cor("Preto")
        self.__builder.set_numero_de_portas(4)
        self.__builder.set_aro(15)
        self.__builder.set_motor("I-4 1.8L")
        self.__builder.set_chassi("MacPherson Strut")
        return self.__builder.build()  
        
    def build_sport(self) -> None:
        self.__builder.set_marca("Lamborghi")
        self.__builder.set_modelo("Aventador")
        self.__builder.set_cor("Amarelo")
        self.__builder.set_numero_de_portas(2)
        self.__builder.set_aro(21)
        self.__builder.set_motor("V12 ")
        self.__builder.set_chassi("Double Wishbone")
        return self.__builder.build()
            
    def build_suv(self) -> None:
        self.__builder.set_marca("Rolls Royce")
        self.__builder.set_modelo("Phantom")
        self.__builder.set_cor("Preto")
        self.__builder.set_numero_de_portas(4)
        self.__builder.set_aro(22)
        self.__builder.set_motor("6.75 L V12")
        self.__builder.set_chassi("Rolls Royce Exclusive")
        return self.__builder.build()


def main():
    builder = CarBuilder()
    diretor = Director(builder)
    
    sedan = diretor.build_sedan()
    sport = diretor.build_sport()
    suv = diretor.build_suv()
    
    print(sedan)
    print(sport)
    print(suv)

if __name__ == "__main__":
    main()