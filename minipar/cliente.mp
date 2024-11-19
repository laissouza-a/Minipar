# Cliente (computador_1)
c_channel calculadora computador_1 computador_2

SEQ
Output("Bem-vindo à calculadora!\n")
Output("Escolha uma operação: +, -, *, /\n")
operacao = Input("Operação: ")
valor1 = Input("Digite o primeiro valor: ")
valor2 = Input("Digite o segundo valor: ")
calculadora.send(operacao, valor1, valor2, resultado)

SEQ
Output("Aguardando o resultado...\n")
calculadora.receive(resultado)
Output("Resultado: ", resultado, "\n")
