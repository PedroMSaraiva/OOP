from abc import ABC, abstractmethod

# Interface abstrata para a construção de um carro.
class Car(ABC):
    @abstractmethod
    def set_marca(self, marca: str):
        pass
    
    @abstractmethod
    def set_modelo(self, modelo: str):
        pass
    
    @abstractmethod
    def set_cor(self, cor: str):
        pass
    
    @abstractmethod
    def set_numero_de_portas(self, numero_de_portas: int):
        pass
    
    @abstractmethod
    def set_aro(self, aro: int):
        pass
    
    @abstractmethod
    def set_motor(self, motor: str):
        pass
    
    @abstractmethod
    def set_chassi(self, chassi: str):
        pass
    
# Implementação concreta da interface Car.
class CarConcrete(Car):
    def set_marca(self, marca: str):
        self.__marca = marca
        return self

    def set_modelo(self, modelo: str):
        self.__modelo = modelo
        return self
    
    def set_cor(self, cor: str):
        self.__cor = cor
        return self   

    def set_numero_de_portas(self, numero_de_portas: int):
        self.__numero_de_portas = numero_de_portas
        return self   

    def set_aro(self, aro: int):
        self.__aro = aro
        return self

    def set_motor(self, motor: str):
        self.__motor = motor
        return self
    
    def set_chassi(self, chassi):
        self.__chassi = chassi
        return self

# Classe responsável por construir o carro seguindo o padrão Builder.
class CarBuilder:
    # Inicializa o builder, preparando para a construção.
    def __init__(self):
        self.reset()

    # Reinicia o processo de construção iniciando um novo objeto CarConcrete.
    def reset(self):
        self.__car = CarConcrete()

    def set_marca(self, marca: str):
        self.__car.set_marca(marca)
        return self

    def set_modelo(self, modelo: str):
        self.__car.set_modelo(modelo)
        return self

    def set_cor(self, cor: str):
        self.__car.set_cor(cor)
        return self

    def set_numero_de_portas(self, numero_de_portas: int):
        self.__car.set_numero_de_portas(numero_de_portas)
        return self

    def set_aro(self, aro: int):
        self.__car.set_aro(aro)
        return self

    def set_motor(self, motor: str):
        self.__car.set_motor(motor)
        return self

    def set_chassi(self, chassi: str):
        self.__car.set_chassi(chassi)
        return self

    # Finaliza a construção e retorna o carro construído.
    def build(self):
        car = self.__car
        self.reset()
        return car

    
#  Classe que direciona o processo de construção do carro.
class Director:
    # Inicialização opcional do builder.
    def __init__(self, builder: CarBuilder = None):
        self.__builder = builder

    # Métodos para obter e definir o builder.
    @property
    def builder(self) -> CarBuilder:
        return self.__builder

    @builder.setter
    def builder(self, builder: CarBuilder):
        self.__builder = builder

    def build_sedan(self):
        return (self.builder
                .set_marca("Toyota")
                .set_modelo("Corolla")
                .set_cor("Preto")
                .set_numero_de_portas(4)
                .set_aro(15)
                .set_motor("I-4 1.8L")
                .set_chassi("MacPherson Strut")
                .build())

    def build_sport(self):
        return (self.builder
                .set_marca("Lamborghini")
                .set_modelo("Aventador")
                .set_cor("Vermelho")
                .set_numero_de_portas(2)
                .set_aro(20)
                .set_motor("V12")
                .set_chassi("Monocoque")
                .build())

    def build_suv(self):
        return (self.builder
                .set_marca("Rolls Royce")
                .set_modelo("Phantom")
                .set_cor("Preto")
                .set_numero_de_portas(4)
                .set_aro(22)
                .set_motor("6.75 L V12")
                .set_chassi("Rolls Royce Exclusive")
                .build())

#Execução e teste do codigo
def main():
    builder = CarBuilder()
    diretor = Director()
    diretor.builder = builder

    sedan = diretor.build_sedan()
    sport = diretor.build_sport()
    suv = diretor.build_suv()

    print(sedan)
    print(sport)
    print(suv)

if __name__ == "__main__":
    main()
