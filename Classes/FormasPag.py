class FormasPag:
    cod = [1, 2, 3, 4]
    nome = ['Dinheiro', 'Crédito', 'Débito', 'Pix']

    def getPagamento(self):
        print(f'\nFormas de pagamento cadastradas:')
        forpag = []
        for x in range(len(self.cod)):
            forpag.append(f'#{self.cod[x]}: {self.nome[x]}')

        print(forpag)