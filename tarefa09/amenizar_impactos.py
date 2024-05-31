import math
import func9

def main():
    entradas = func9.ler_entradas()
    grupos = func9.gerar_grupos(entradas)
    maiores = func9.encontrar_maiores(grupos)
    n_maior = func9.encontrar_grupo(maiores)
    func9.saidas2(n_maior, grupos)
    
main()