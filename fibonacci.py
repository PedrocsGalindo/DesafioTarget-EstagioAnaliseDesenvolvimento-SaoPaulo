numero = int(input("informe um numero"))
aux = 0
naux = 0
numeroAtual = 1
if (numero == 0):
    print("Pertence a senquencia de Fibonacci")
while (numeroAtual < numero and numeroAtual != numero):
    aux = numeroAtual
    numeroAtual = numeroAtual + naux
    naux = aux

if (numeroAtual == numero):
    print("Pertence a senquencia de Fibonacci")
else:
    print("Não pertence a senquencia de Fibonacci")

