class Car: #Interface
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> None:
        pass
    
    
class CarBuilder:
    def __init__(self):
        self.car = Car()
        
    def set_marca(self, marca):
        self.car.marca = marca
        return self
    
    def set_modelo(self, modelo):
        self.car.modelo = modelo
        return self
    
    def set_cor(self, cor):
        self.car.cor = cor
        return self
    
    def set_numero_de_portas(self, numero_de_portas):
        self.car.numero_de_portas = numero_de_portas
        return self
    
    def build(self):
        return self.car
    
    
class Director:
    def __init__(self, builder):
        self.__builder = builder
    
    def build_sedan(self):
        self.__builder.set_marca("Toyota") 
        self.__builder.set_modelo("Corolla") 
        self.__builder.set_cor("Preto")
        self.__builder.set_numero_de_portas(4)
        return self.__builder.build()  
        
    def build_sport(self):
        self.__builder.set_marca("Lamborghi")
        self.__builder.set_modelo("Aventador")
        self.__builder.set_cor("Amarelo")
        self.__builder.set_numero_de_portas(2)
        return self.__builder.build()
            
    def build_suv(self):
        self.__builder.set_marca("Rolls Royce")
        self.__builder.set_modelo("Phantom")
        self.__builder.set_cor("Preto")
        self.__builder.set_numero_de_portas(4)
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