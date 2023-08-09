#Binario para Decimal
def binToDec(bin):
    dec = 0
    i = 0
    tamanho = len(str(bin))
    while tamanho >= 0:
        resto = bin % 10
        dec += (resto * (2** i))
        i += 1
        tamanho -= 1
        bin //= 10
    return dec

#Decimal para Binario
def decToBin(dec):
    if dec == 0:
        return 0
    bin = ''
    while dec > 1:
        resto = dec % 2
        dec //= 2
        bin += str(resto)
    bin += '1'
    return bin[::-1]


#menuzinho
sair = False
while sair != True:
    print("------------------------")
    print("[1] Binario para Decimal")
    print("[2] Decimal para Binario")
    print("[9] SAIR")
    ans = int(input("\nDigite o numero da opcao: "))

    match ans:
        case 1:
            print("---------------------------")
            bin = int(input("Digite o valor na base 2: "))
            dec = binToDec(bin)
            print(f"Decimal: {dec}")
        case 2:
            print("---------------------------")
            dec = int(input("Digite o valor na base 10: "))
            bin = decToBin(dec)
            print(f"Binario: {bin}")
        case 9:
            sair = True
        case _:
            print("Codigo Invalido")