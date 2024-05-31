import func

def main():
    dados = func.ler_arquivo()
    dados_ord = func.ordenar_dados(dados)
    media_total, desvio_total = func.media_desvio(dados_ord)
    discrepancias = func.calcular_discrepancias(dados_ord, media_total, desvio_total)
    N_discrepancias = func.maiores_discrepancias(discrepancias, 10)
    discrepancia_ord = func.ordenar_dados(N_discrepancias)
    for discrepancia in discrepancia_ord:
        print(f"{discrepancia[0]}/{discrepancia[1]}: {discrepancia[2]:.2f}")

main()