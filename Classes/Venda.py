import Cliente
import Funcionario
import Produto
import FormasPag

class Venda:
    cod = []

    cliente = []
    funcionario = []
    produto = []
    quantidade = []
    valor_total = []
    pagamento = []

    def cadVendas(self):
        codVend = len(self.cod) + 1
        self.cod.append(codVend)
        print(f'Código de venda: {codVend}')

        cli = Cliente()
        cli.getClientes()
        client = int(input("\nEntre com o código do cliente: "))
        nome = cli.nome[client-1]
        print(nome)
        self.cliente.append(nome)

        func = Funcionario()
        func.getFuncionario()
        fnc = int(input("\nEntre com o código do funcionário: "))
        nome = func.nome[fnc-1]
        self.funcionario.append(nome)

        prd = Produto()
        prd.getProdutos()
        prod = int(input("\nEntre com o código do produto vendido: "))
        nome = prd.nome[prod-1]
        self.produto.append(nome)

        self.quantidade.append(int(input("Entre com a quantidade de itens: ")))

        self.valor_total.append(prd.valor[prod-1] * self.quantidade[codVend-1])
        print(f'O subtotal é R${self.valor_total[codVend - 1]}')

        pag = FormasPag()
        pag.getPagamento()
        pag_form = int(input("\nEscolha a forma de pagamento: "))
        nome = pag.nome[pag_form - 1]
        self.pagamento.append(nome)

    def getVendas(self):
        print(f"Vendas já efetuadas:")
        vend = []
        for x in range(len(self.cod)):
            vend.append(f'Compra #{self.cod[x]}: \n'
                        f'\tCliente: {self.cliente[x]}\n'
                        f'\tVendedor:{self.funcionario[x]}\n'
                        f'\tProduto: {self.produto[x]}\n'
                        f'\tQuantidade: {self.quantidade[x]}\n'
                        f'\tValor total: R${(self.valor_total[x])}\n'
                        f'\tPago por: {self.pagamento[x]}\n')
            print(vend[x])

        print("\n\n")