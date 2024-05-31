import sequencias

def coletar_entradas():
    """
    Pede as entradas necessárias ao usuário e devolve-as
    """
    
    tamanho_janela = int(input())
    genoma_referencia = input()
    genoma_variante = input()
    
    return tamanho_janela, genoma_referencia, genoma_variante
    
def main():
    tamanho_janela,genoma_referencia, genoma_variante = coletar_entradas()
    diferencas = sequencias.diferencas(genoma_referencia, genoma_variante, tamanho_janela)

    for i in range(len(diferencas)):
        referencia_variante = [sequencias.janela(genoma_referencia, diferencas[i], tamanho_janela), sequencias.janela(genoma_variante, diferencas[i], tamanho_janela)]
        print(f"Diferença {i+1}:")
        print("   Posição:", diferencas[i],)
        print("Referência:", referencia_variante[0])
        print("  Variante:", referencia_variante[1])
        print(" Distância:", sequencias.distancia_hamming(referencia_variante[0], referencia_variante[1]))
        print()
        
main()
