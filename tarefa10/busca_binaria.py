import func10

def main():
    lista = input().split()
    lista = list(map(int, lista))
    i = int(input())
    print(func10.contar(i, lista))

main()