class Produto:
    cod = []
    nome = []
    valor = []

    def cadProduto(self):
        if len(self.cod)>0:
            Produto.getProdutos(self)

        num_prod = len(self.cod) + 1

        print(f'Código do produto: {num_prod}')
        desc_prod = input("Digite a descrição do produto: ")
        value = float(input("Digite o valor do produto: "))

        self.cod.append(num_prod)
        self.nome.append(desc_prod)
        self.valor.append(value)

        print("Produto cadastrado com sucesso!")

    def getProdutos(self):
        print(f'\nProdutos cadastrados:')
        prod = []
        for x in range(len(self.cod)):
            prod.append(f'#{self.cod[x]}: {self.nome[x]} - R${format(self.valor[x])}')

        print(prod)