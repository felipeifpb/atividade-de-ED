class Pais:
    def __init__(self, nome: str, capital: str, dimensao: float):
        # Atributos privados
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__fronteiras = []

    # Métodos de acesso para os atributos
    def get_nome(self) -> str:
        return self.__nome

    def get_capital(self) -> str:
        return self.__capital

    def get_dimensao(self) -> float:
        return self.__dimensao

    # Método para retornar a lista de países que fazem fronteira
    def get_fronteiras(self) -> list:
        return self.__fronteiras

    # Método para adicionar um país à lista de fronteiras
    def adiciona_fronteira(self, pais: str):
        if pais not in self.__fronteiras:
            self.__fronteiras.append(pais)
        else:
            print(f"{pais} já está na lista de fronteiras de {self.__nome}.")

    # Método para representação textual do objeto País
    def __str__(self) -> str:
        fronteiras_str = ", ".join(self.__fronteiras) if self.__fronteiras else "Nenhuma"
        return (f"País: {self.__nome}\n"
                f"Capital: {self.__capital}\n"
                f"Dimensão: {self.__dimensao} km²\n"
                f"Fronteiras: {fronteiras_str}")


# Programa para criar objetos da classe Pais e testar os métodos
if __name__ == "__main__":
    # Criando um objeto da classe Pais
    brasil = Pais("Brasil", "Brasília", 8515767)

    # Testando os métodos acessores
    print("Nome do país:", brasil.get_nome())
    print("Capital:", brasil.get_capital())
    print("Dimensão:", brasil.get_dimensao(), "km²")

    # Adicionando fronteiras
    brasil.adiciona_fronteira("Argentina")
    brasil.adiciona_fronteira("Uruguai")
    brasil.adiciona_fronteira("Paraguai")
    brasil.adiciona_fronteira("Argentina")  # Tentativa de adicionar fronteira já existente

    # Exibindo as fronteiras
    print("Lista de países que fazem fronteira:", brasil.get_fronteiras())

    # Exibindo a representação textual do objeto País
    print("\nInformações do país:")
    print(brasil)
