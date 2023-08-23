class Funcionario:
    cod = []
    nome = []

    def cadFuncionario(self):
        if len(self.cod)>0:
            Funcionario.getFuncionario(self)

        num_func = len(self.cod) + 1

        print(f'Código do funcionário: {num_func}')
        nome_func = input("Digite o nome do funcionário: ")

        self.cod.append(num_func)
        self.nome.append(nome_func)

        print("Funcionário cadastrado com sucesso!")

    def getFuncionario(self):
        print(f'\nFuncionários cadastrados:')
        func = []
        for x in range(len(self.cod)):
            func.append(f'#{self.cod[x]}: {self.nome[x]}')

        print(func)