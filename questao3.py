def area(largura, altura):
 return (largura * altura)
print("Digite a largura do triângulo: ")
largura = int(input())
print("Digite a altura do triângulo: ")
altura = int(input())
print()
calculo = area(largura, altura)  # chama a função para calcular a área
print("A área total do triângulo é:", calculo)
print()
input("Clique uma tecla para sair...")
