from abc import ABC, abstractmethod
from typing import List


# Component
class EnterpriseComponent(ABC):
    @abstractmethod
    def gerar_produto(self):
        pass

    @abstractmethod
    def transportar_produto(self):
        pass

    @abstractmethod
    def efetuar_pagamento(self, valor: float):
        pass

    @abstractmethod
    def atender_cliente(self):
        pass


# Leaf
class Produto(EnterpriseComponent):
    def gerar_produto(self):
        print("Produto gerado.")

    def transportar_produto(self):
        pass  # Produto não implementa transportar_produto

    def efetuar_pagamento(self, valor: float):
        pass  # Produto não implementa efetuar_pagamento

    def atender_cliente(self):
        pass  # Produto não implementa atender_cliente
    

# Leaf
class Atendimento(EnterpriseComponent):
    def gerar_produto(self):
        pass  # Atendimento não implementa gerar_produto

    def transportar_produto(self):
        pass  # Atendimento não implementa transportar_produto

    def efetuar_pagamento(self, valor: float):
        pass  # Atendimento não implementa efetuar_pagamento

    def atender_cliente(self):
        print("Cliente atendido.")
        
        
# Leaf
class Pagamento(EnterpriseComponent):
    def gerar_produto(self):
        pass  # Pagamento não implementa gerar_produto

    def transportar_produto(self):
        pass  # Pagamento não implementa transportar_produto

    def efetuar_pagamento(self, valor: float):
        print(f"Pagamento efetuado: {valor}")

    def atender_cliente(self):
        pass  # Pagamento não implementa atender_cliente
    

# Composite
class GerenteOperacional(EnterpriseComponent):
    def __init__(self):
        self.children = []

    def add(self, component: EnterpriseComponent):
        self.children.append(component)

    def remove(self, component: EnterpriseComponent):
        self.children.remove(component)

    def gerar_produto(self):
        for child in self.children:
            child.gerar_produto()

    def transportar_produto(self):
        for child in self.children:
            child.transportar_produto()

    def efetuar_pagamento(self, valor: float):
        for child in self.children:
            child.efetuar_pagamento(valor)

    def atender_cliente(self):
        for child in self.children:
            child.atender_cliente()
            
if __name__ == "__main__":
    # Criar objetos leaf
    produto = Produto()
    atendimento = Atendimento()
    pagamento = Pagamento()

    # Criar composite
    gerente_operacional = GerenteOperacional()

    # Adicionar leafs ao composite
    gerente_operacional.add(produto)
    gerente_operacional.add(atendimento)
    gerente_operacional.add(pagamento)

    # Executar métodos composite, que delegam para os leafs
    gerente_operacional.gerar_produto()
    gerente_operacional.atender_cliente()
    gerente_operacional.efetuar_pagamento(1000.0)