class ContaCorrente:
    def __init__(self, numero: int, saldo: float, titular: str):
        self.numero = numero
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float) -> bool:
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def get_saldo(self) -> float:
        return self.saldo

    def __str__(self) -> str:
        return f"Conta número: {self.numero}, Titular: {self.titular}, Saldo: {self.saldo:.2f}"


# Programa principal para gerenciar as contas
if __name__ == "__main__":
    contas = []

    # Criando 10 instâncias de ContaCorrente com dados fornecidos pelo usuário
    for i in range(10):
        numero = int(input(f"Informe o número da conta {i + 1}: "))
        saldo = float(input(f"Informe o saldo inicial da conta {i + 1}: "))
        titular = input(f"Informe o nome do titular da conta {i + 1}: ")
        conta = ContaCorrente(numero, saldo, titular)
        contas.append(conta)

    # Função para encontrar uma conta pelo número
    def encontrar_conta(numero: int):
        for conta in contas:
            if conta.numero == numero:
                return conta
        print("Conta não encontrada.")
        return None

    # Menu de operações
    while True:
        print("\nOperações disponíveis:")
        print("1) Depositar")
        print("2) Sacar")
        print("3) Saldo")
        print("4) Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':  # Depositar
            numero = int(input("Digite o número da conta para depósito: "))
            conta = encontrar_conta(numero)
            if conta:
                valor = float(input("Digite o valor a ser depositado: "))
                conta.depositar(valor)
                print(f"Depósito de {valor:.2f} realizado com sucesso. Saldo atual: {conta.get_saldo():.2f}")

        elif opcao == '2':  # Sacar
            numero = int(input("Digite o número da conta para saque: "))
            conta = encontrar_conta(numero)
            if conta:
                valor = float(input("Digite o valor a ser sacado: "))
                if conta.sacar(valor):
                    print(f"Saque de {valor:.2f} realizado com sucesso. Saldo atual: {conta.get_saldo():.2f}")
                else:
                    print("Saldo insuficiente para realizar o saque.")

        elif opcao == '3':  # Saldo
            numero = int(input("Digite o número da conta para consultar saldo: "))
            conta = encontrar_conta(numero)
            if conta:
                print(f"Saldo da conta {numero}: {conta.get_saldo():.2f}")

        elif opcao == '4':  # Sair
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
