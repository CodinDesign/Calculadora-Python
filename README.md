# README - Calculadora Simples em Python

## Descrição

Este projeto consiste em uma calculadora simples implementada em Python, que permite ao usuário realizar operações básicas de aritmética: soma, subtração, multiplicação e divisão. A aplicação é interativa e solicita que o usuário escolha uma operação e insira os números para realizar o cálculo.

## Funcionalidades

A calculadora possui as seguintes operações:

1. **Somar**: Adiciona dois números.
2. **Subtrair**: Subtrai o segundo número do primeiro.
3. **Multiplicar**: Multiplica dois números.
4. **Dividir**: Divide o primeiro número pelo segundo (cuidado com a divisão por zero).

## Como Usar

1. Execute o código em um ambiente Python.
2. Ao iniciar, você verá um menu com as opções de operações.
3. Digite o número correspondente à operação desejada (1, 2, 3 ou 4).
4. Insira os dois números que deseja calcular.
5. O resultado da operação será exibido no terminal.

## Código

Aqui está o código da calculadora:

```python
# Função para somar dois números
def somar(a, b):
    return a + b

# Função para subtrair dois números
def subtrair(a, b):
    return a - b
	
# Função para multiplicar dois números
def multiplicar(a, b):
    return a * b
	
# Função para dividir dois números
def dividir(a, b):
    return a / b

# Função principal
def calculadora():
    print("Selecione a Operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    # Recebendo a escolha do usuário
    escolha = input("Digite sua escolha (1/2/3/4): ")

    # Verificando se a escolha é válida
    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
		
        if escolha == '1':
            print(f"{num1} + {num2} = {somar(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Escolha inválida!")

# Chamando a função
calculadora()
