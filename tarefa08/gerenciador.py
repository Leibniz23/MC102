from traceback import print_tb
import func8

def main():
    entradas = func8.ler_entradas()
    arquivos = []
    for entrada in entradas:
        match entrada[0]:
            case "terminar":
                print("até mais!")

            case "entrar":
                ativo = entrada[1]
                print(f"{ativo} entrou!")

            case "criar":
                arq_vazio = func8.arquivo(entrada[1],[], ativo)
                if arq_vazio in arquivos:
                    print(f"arquivo {entrada[1]} existente")
                else:
                    arquivos.append(arq_vazio)
                    print(f"{entrada[1]} criado")

            case "carregar":
                conteudo = func8.ler_arquivo(entrada[1])
                arq_local = func8.arquivo(entrada[2], conteudo, ativo)
                arquivos.append(arq_local)
                print(f"{entrada[1]} carregado como {entrada[2]}")

            case "digitar":
                for arquivo in arquivos:
                    if entrada[1] == arquivo[0]:
                        linha = []
                        for i in range(2,len(entrada)):
                            linha.append(entrada[i])
                        linha[len(linha)-1] += "\n"
                        arquivo[1].append(linha)
                        linhas = len(arquivo[1])
                print(f"{entrada[1]} modificado: {linhas} linhas")

            case "mostrar":
                print(f"--- início de {entrada[1]} ---")
                for arquivo in arquivos:
                    if arquivo[0] == entrada[1]:
                        for i in range(len(arquivo[1])):
                            for j in range(len(arquivo[1][i])):
                                if "\n" not in arquivo[1][i][j]:
                                    print(*arquivo[1][i][j], end = ' ', sep = '')
                                else:
                                    print(*arquivo[1][i][j], end = '', sep = '')
                print(f"--- final de {entrada[1]} ---")

            case "listar":
                if len(entrada) > 1:
                    for arquivo in arquivos:
                        print(arquivo[0],arquivo[2])
                else:
                    arq_ord = func8.ord_lista(arquivos)
                    for i in arq_ord:
                        print(arquivos[i][0],arquivos[i][2])
                print(f"{len(arquivos)} arquivos existentes")

            case "substituir":
                for arquivo in arquivos:
                    if arquivo[0] == entrada[1]:
                        for i in range(len(arquivo[1])):
                            for j in range(len(arquivo[1][i])):
                                if arquivo[1][i][j] == entrada[2] + "\n":
                                    arquivo[1][i][j] = entrada[3] + "\n"

                                elif arquivo[1][i][j] == entrada[2]:
                                    arquivo[1][i][j] = entrada[3]
                        print(f"{entrada[1]} modificado: {len(arquivo[1])} linhas")

            case "comparar":
                for i in range(len(arquivos)):
                    if arquivos[i][0] == entrada[1]:
                        arquivo1 = arquivos[i][1]
                    elif arquivos[i][0] == entrada[2]:
                        arquivo2 = arquivos[i][1]
                diff = func8.comparar(arquivo1, arquivo2)
                func8.unix(diff)

            case "buscar":
                correspondentes = []
                for arquivo in arquivos:
                    if(func8.in_arq(arquivo[1],entrada[1])):
                        func8.ord_nomes(correspondentes,arquivo[0])
                for correspondente in correspondentes:
                    print(f"{correspondente} contém {entrada[1]}")
                print(f"{len(correspondentes)} arquivos encontrados")

main()