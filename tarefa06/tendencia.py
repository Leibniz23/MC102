import func

def main():
    dados = func.ler_arquivo()
    dados_ord = func.ordenar_dados(dados)
    temp_ano = func.temp_media(dados_ord)
    desvio_ano = func.desvio_anual(dados_ord)
    outliers = func.calcular_outliers(dados_ord, temp_ano, desvio_ano)
    med_normal = func.media_sem_outlier(dados_ord, outliers)

    print("Outliers:")
    for i in range(len(outliers)):
        print(outliers[i][0],"/",outliers[i][1], sep="")
        #print(f"{outliners[i][0]}/{outliners[i][1]}") é outra forma de formatar a saída

    print()

    print("Tendência de média anual:")
    k = 0
    for i in range(len(med_normal)):
        print(f"{dados_ord[k][1]}: {med_normal[i]:.2f}")
        k += 12
   
main()