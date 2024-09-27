def fibonacci(n):
    if n <= 0:
        return "Posição inválida. Insira um número maior que 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def main():
    try:
        pos = int(input("Digite a posição na sequência de Fibonacci: "))
        resultado = fibonacci(pos)
        print(f"O número na posição {pos} da sequência de Fibonacci é: {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()