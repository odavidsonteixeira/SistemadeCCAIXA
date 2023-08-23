class Cliente:
    cod = []
    nome = []

    def cadCliente(self):
        if len(self.cod)>0:
            Cliente.getClientes(self)

        num_cliente = len(self.cod)+1

        print(f'Código do cliente: {num_cliente}')
        nome_cli = input("Digite o nome do cliente: ")

        self.cod.append(num_cliente)
        self.nome.append(nome_cli)

        print("Cliente cadastrado com sucesso!")

    def getClientes(self):
        print(f'\nClientes cadastrados:')
        client = []
        for x in range(len(self.cod)):
            client.append(f'#{self.cod[x]}: {self.nome[x]}')

        print(client)