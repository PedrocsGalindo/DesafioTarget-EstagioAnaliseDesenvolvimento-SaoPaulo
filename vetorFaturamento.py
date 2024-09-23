fatura = 1
faturas = []
totalFatura= 0

while fatura != 0 :
    fatura  = int(input("digita a fatura de cada dia, quando encerrar digite 0: "))
    if fatura == 0:
        break
    faturas.append(fatura)
    totalFatura += fatura

faturaMedia = totalFatura / len(faturas)

menorFatura = faturas[0]
maiorFatura = faturas[0]
faturaMaiorMedia = []
for fatura in faturas:
    if menorFatura > fatura:
        menorFatura = fatura
    if maiorFatura < fatura:
        maiorFatura = fatura
    if fatura > faturaMedia:
        faturaMaiorMedia.append(fatura)

print('menor fatura '+ str(menorFatura))
print('maior fatura ' + str(maiorFatura))
print("Faturas maiors que a media' " + str(faturaMedia) + " '")
for fatura in faturaMaiorMedia:
    print(str(fatura))