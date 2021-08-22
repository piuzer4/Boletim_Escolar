from decimal import Decimal, getcontext
import os

traco = "----------------------------------------------------"
media = 7.0
ponto = 1.0

getcontext().prec = 2


class cor:
    PEX = '\033[31m'
    NORMAL = '\033[0m'
    POSITIVO = '\033[34m'


def fisica():
    print(traco)
    print("Seja bem-vindo ao seu boletim")
    print(traco)
    print("Qual a sua média em fisica no 1 BI?")
    fisicabi1 = float(input())
    pontoex1 = Decimal(fisicabi1) - Decimal(media)
    if fisicabi1 <= media:
        print("Você está devendo um total de:", pontoex1)
        print(traco)
    else:
        print("Seus ponto extras é de:", pontoex1)
        print(traco)

    print("Qual a sua média em fisica 2 Bi?")
    fisicabi2 = float(input())
    pontoex2 = Decimal(fisicabi2) - Decimal(media)
    pontosext = Decimal(pontoex1) + Decimal(pontoex2)
    if fisicabi2 <= 1:
        print("Você está devendo um total de:", pontosext)
        print(traco)
    else:
        print("Seus pontos extras é de", pontosext)
        print(traco)

    print("Qual a sua média em fisica 3 Bi?")
    fisicabi3 = float(input())
    pontoex3 = Decimal(fisicabi3) - Decimal(media)
    pontosex123 = Decimal(pontosext) + Decimal(pontoex3)
    if fisicabi3 <= media:
        print("Você está devendo um total de", pontosex123)
        print(traco)
    else:
        print("Seus pontos extras é de:", pontosex123)
        print(traco)

    print("Qual a sua média em fisica 4 Bi?")
    fisicabi4 = float(input())
    pontoex4 = Decimal(fisicabi4) - Decimal(media)
    pontosex1234 = Decimal(pontosex123) + Decimal(pontoex4)
    if fisicabi4 <= media:
        print("Você está devendo um total de", pontosex1234)
        print(traco)
    else:
        print("Seus pontos extras é de:", pontosex1234)
        print(traco)
    os.system('cls')

    aprovado1 = Decimal(fisicabi1) + Decimal(fisicabi2)
    aprovado2 = Decimal(fisicabi3) + Decimal(fisicabi4)
    aprovadot = Decimal(aprovado1) + Decimal(aprovado2)
    passo = Decimal(aprovadot) / Decimal(4)
    reprovado = Decimal(passo) - Decimal(7)

    if passo >= 7:
        print("Você foi aprovado com uma média de", passo)

    else:
        print("Infelizmente você foi reprovado faltando", reprovado)


if __name__ == '__main__':
    fisica()
