palavra = input("escreva uma palavra para ser invertida: ")
invertido = [""] * (len(palavra) + 1)
i = len(palavra)
for char in palavra:
    invertido[i] = char
    i -= 1
print(''.join(invertido))