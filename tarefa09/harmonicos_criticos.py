import func9
import math

def main():
    entradas = func9.ler_entradas()
    thdn = func9.calcular_thd(entradas, len(entradas)-1, entradas[0])
    thdm = 0
    i = 1
    limite = (80*thdn)/100
    soma = 0
    while thdm < limite:
        soma += entradas[i]**2
        thdm = (math.sqrt(soma)/entradas[0])*100
        n_harm = i
        i += 1
    func9.saidas(n_harm, thdm, thdn)

main()