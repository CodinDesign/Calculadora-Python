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
