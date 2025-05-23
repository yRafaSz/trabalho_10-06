def cafe():
    return 14.99 # preço do café
print("Digite em número quantos cafés você irá querer: ")
quantidade = int(input())
preco = cafe() * quantidade
print("O valor total deu:", preco)
print()
print("Preço unitário: R$: 14,99")