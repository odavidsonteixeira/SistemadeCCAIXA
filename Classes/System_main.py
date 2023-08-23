import Cliente
import Funcionario
import Produto
import Venda


class System:
    caixa = []

    cli = Cliente()
    func = Funcionario()
    prod = Produto()
    compra = Venda()

    def getCaixa(self):
        while True:
            option = int(input("O que você deseja?\n"
                  "1 - Acessar clientes;\n"
                  "2 - Acessar funcionários;\n"
                  "3 - Acessar produtos;\n"
                  "4 - Acessar compras;\n"
                  "5 - Finalizar o programa;\n\n"
                               "Sua opção: "))

            if option == 1:
                option_cli = int(input("\n\nDigite a opção referente ao que você deseja:\n"
                                         "1 - Cadastrar cliente;\n"
                                         "2 - Vizualizar clientes;;\n"
                                         "3 - Voltar;\n\n"
                                       "Sua opção: "))

                if option_cli == 1:
                    self.cli.cadCliente()
                    print("\n\n\n")

                if option_cli == 2:
                    self.cli.getClientes()
                    print("\n\n\n")

                if option_cli == 3:
                    print("\n\n\n")

            if option == 2:
                option_func = int(input("\n\nDigite a opção referente ao que você deseja:\n"
                                         "1 - Cadastrar funcionário;\n"
                                         "2 - Vizualizar funcionários;;\n"
                                         "3 - Voltar;\n\n"
                                       "Sua opção: "))

                if option_func == 1:
                    self.func.cadFuncionario()
                    print("\n\n\n")

                if option_func == 2:
                    self.func.getFuncionario()
                    print("\n\n\n")

                if option_func == 3:
                    print("\n\n\n")

            if option == 3:
                option_prod = int(input("\n\nDigite a opção referente ao que você deseja:\n"
                                         "1 - Cadastrar produto;\n"
                                         "2 - Vizualizar produtos;;\n"
                                         "3 - Voltar;\n\n"
                                       "Sua opção: "))

                if option_prod == 1:
                    self.prod.cadProduto()
                    print("\n\n\n")

                if option_prod == 2:
                    self.prod.getProdutos()
                    print("\n\n\n")

                if option_prod == 3:
                    print("\n\n\n")

            if option == 4:
                option_vend = int(input("\n\nDigite a opção referente ao que você deseja:\n"
                                         "1 - Efetuar compra;\n"
                                         "2 - Vizualizar compras;;\n"
                                         "3 - Voltar;\n\n"
                                       "Sua opção: "))

                if option_vend == 1:
                    self.compra.cadVendas()
                    print("\n\n\n")

                if option_vend == 2:
                    self.compra.getVendas()
                    print("\n\n\n")

                if option_vend == 3:
                    print("\n\n\n")

            if option == 5:
                print("Obrigado por usar nosso sistema de caixa!!!")
                break

            else:
                continue