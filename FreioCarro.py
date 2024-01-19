from abc import ABC, abstractmethod

# Interface Strategy
class TipoFreiar(ABC):
    @abstractmethod
    def freiar(self, velocidade_de_freio: float):
        #Método abstrato para definir a estratégia de frenagem.
        pass
    
# Concrete Strategy 1
class Freio(TipoFreiar):
    def freiar(self, velocidade_de_freio: float):
        #Implementação da estratégia de frenagem normal
        return self.freiar_normal(velocidade_de_freio)

    def freiar_normal(self, velocidade_de_freio: float):
        print(f"Freiando normalmente a {velocidade_de_freio}m/s².")

# Concrete Strategy 2
class FreioABS(TipoFreiar):

    def freiar(self, velocidade_de_freio: float):
        #Implementação da estratégia de frenagem com ABS.
        return self.freiar_eficiente(velocidade_de_freio)

    def freiar_eficiente(self, velocidade_de_freio: float):
        print(f"Freiando eficientemente a {velocidade_de_freio}m/s² com ABS.")
        
# Context
class Carro:
    def __init__(self, tipo_freiar: TipoFreiar):
        self._tipo_freiar = tipo_freiar

    def freiar(self, velocidade_de_freio: float):
        #Método para realizar a frenagem usando a estratégia atual.
        self._tipo_freiar.freiar(velocidade_de_freio)

    @property
    def tipo_freiar(self) -> TipoFreiar:
        #Getter para o tipo de frenagem.
        return self._tipo_freiar

    @tipo_freiar.setter
    def tipo_freiar(self, tipo_freiar: TipoFreiar):
        #Setter para alterar o tipo de frenagem.
        self._tipo_freiar = tipo_freiar
        
# Client code
if __name__ == "__main__":
    # O carro pode mudar de estratégia em tempo de execução.
    carro = Carro(Freio())
    carro.freiar(5.0) # Uso da estratégia inicial (Freio normal)

    carro._tipo_freiar = FreioABS() # Mudança de estratégia para FreioABS
    carro.freiar(7.0) # Uso da nova estratégia (FreioABS)