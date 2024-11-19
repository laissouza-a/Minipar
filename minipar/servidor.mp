# Servidor (computador_2)
c_channel calculadora computador_1 computador_2

SEQ
Output("Servidor pronto para calcular...\n")
calculadora.receive(operacao, valor1, valor2, resultado)

PAR
if operacao == "+" {
    resultado = valor1 + valor2
}
if operacao == "-" {
    resultado = valor1 - valor2
}
if operacao == "*" {
    resultado = valor1 * valor2
}
if operacao == "/" {
    if valor2 != 0 {
        resultado = valor1 / valor2
    } else {
        resultado = "Erro: Divisão por zero."
    }
}
if operacao != "+" && operacao != "-" && operacao != "*" && operacao != "/" {
    resultado = "Erro: Operação inválida."
}

SEQ
calculadora.send(resultado)
Output("Cálculo realizado. Resultado enviado!\n")
