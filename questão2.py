class Aluno:
    def __init__(self, matricula: int, nome: str, notas: list = None):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas if notas is not None else []

    # Métodos acessores
    def get_nome(self) -> str:
        return self.nome

    def get_matricula(self) -> int:
        return self.matricula

    # Método para calcular a média das notas
    def media(self) -> float:
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0.0

    # Método para alterar o nome
    def set_nome(self, nome: str):
        self.nome = nome

    # Método para adicionar uma nota à lista de notas
    def adiciona_nota(self, nota: float):
        self.notas.append(nota)

    # Representação textual do objeto Aluno
    def __str__(self) -> str:
        return f"Aluno(matrícula={self.matricula}, nome={self.nome}, notas={self.notas}, média={self.media():.2f})"


# Programa para criar objetos da classe Aluno e testar os métodos
if __name__ == "__main__":
    # Criando um objeto Aluno
    aluno = Aluno(12345, "Carlos Silva")
    
    # Adicionando notas
    aluno.adiciona_nota(7.5)
    aluno.adiciona_nota(8.0)
    aluno.adiciona_nota(9.5)

    # Exibindo informações do aluno
    print(aluno)
    
    # Testando os métodos acessores
    print("Nome do aluno:", aluno.get_nome())
    print("Matrícula do aluno:", aluno.get_matricula())

    # Testando o cálculo da média
    print("Média das notas:", aluno.media())

    # Alterando o nome do aluno
    aluno.set_nome("Carlos Santos")
    print("Nome atualizado:", aluno.get_nome())
