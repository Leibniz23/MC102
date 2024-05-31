from operator import index
import func_7

def main():
    entradas = func_7.ler_entradas()
    imgs = []
    for entrada in entradas:
        match entrada[0]:
            case "carregar":
                m, n, matriz = func_7.carregar(entrada[1])
                imgs.append(matriz)
                print(f"Carregado arquivo {entrada[1]} em imagem {imgs.index(matriz)}.")
            case "gravar":
                func_7.gravar(entrada[1], imgs[int(entrada[2])])
                print(f"Gravado arquivo {entrada[1]} com imagem {entrada[2]}.")
            case "binarizar":
                limiar = entrada[2]
                matriz = imgs[int(entrada[1])]
                cont, img_final = func_7.binarizar(matriz, int(limiar))
                imgs[int(entrada[1])] = img_final
                print(f"Imagem {entrada[1]} modificada: {str(cont)} pixels maiores que zero.")
            case "normalizar":
                indice = int(entrada[1])
                matriz = imgs[indice]
                cont= func_7.normalizar(imgs[indice])
                print(f"Imagem {entrada[1]} modificada: {str(cont)} pixels maiores que zero.")
            case "multiplicar":
                ind_a = int(entrada[1])
                ind_b = int(entrada[2])
                r = func_7.multiplicar(imgs[ind_a], imgs[ind_b])
                imgs[ind_a] = r[1]
                print(f"Imagem {str(ind_a)} modificada: {str(r[0])} pixels maiores que zero.")
            case "filtrar":
                if entrada[2] == "Laplaciano":
                    ind = int(entrada[1])
                    cont = func_7.laplace(imgs[ind])
                    print(f"Imagem {entrada[1]} modificada: {cont} pixels maiores que zero.")


main()

