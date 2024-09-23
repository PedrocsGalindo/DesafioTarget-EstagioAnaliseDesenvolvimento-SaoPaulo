class Estado:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.representacao = 0

    def setRepresentacao(self, representacao):
        self.representacao = representacao
estados = []
faturamentoTotal = 0
nEstado = "true"
while nEstado != "" :
    nEstado = input("\ninsira o nome do estado, caso deseje encerrar não digite nada: ")
    if nEstado == "":
        break  
    faturamento = float(input(f"Insira o faturamento para {nEstado}: "))
    estado = Estado(nEstado, faturamento)
    faturamentoTotal += faturamento
    estados.append(estado)

print (faturamentoTotal)
for estado in estados:
    estado.setRepresentacao(estado.valor/faturamentoTotal * 100)
    print(estado.nome  + " " + str(estado.representacao))

