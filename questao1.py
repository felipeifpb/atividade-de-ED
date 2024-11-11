class Data:
    def __init__(self, dia: int, mes: int, ano: int):
        # Atributos privados
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    # Métodos acessores
    def get_dia(self) -> int:
        return self.__dia

    def get_mes(self) -> int:
        return self.__mes

    def get_ano(self) -> int:
        return self.__ano

    # Métodos modificadores
    def set_dia(self, dia: int):
        self.__dia = dia

    def set_mes(self, mes: int):
        self.__mes = mes

    def set_ano(self, ano: int):
        self.__ano = ano

    # Método para representação da data como string
    def __str__(self) -> str:
        return f"{self.__dia:02}/{self.__mes:02}/{self.__ano}"

# Programa para criar objetos da classe Data e testar os métodos
if __name__ == "__main__":
    # Criando um objeto da classe Data
    data = Data(15, 11, 2024)
    
    # Testando o método __str__
    print("Data formatada:", data)

    # Testando os métodos acessores
    print("Dia:", data.get_dia())
    print("Mês:", data.get_mes())
    print("Ano:", data.get_ano())

    # Testando os métodos modificadores
    data.set_dia(25)
    data.set_mes(12)
    data.set_ano(2025)
    
    # Exibindo a data após as modificações
    print("Data modificada:", data)
