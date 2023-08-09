#Binario para um numero Real decimal
def binToDec_Real(bin):
    dec = 0
    for n in range(2, len(bin)):
        dec += int(bin[n]) * 2**(-n)
    dec *= 2
    return dec

#Real decimal para um numero binario
def decToBin_Real(dec):
    bin = ""
    while dec > 0:
        dec *= 2
        if dec >= 1:
            bin += "1"
            dec -= 1
        else:
            bin += "0"
    return "0." + bin

#menuzinho
sair = False
while sair != True:
    print("------------------------")
    print("[1] Binario para Real Decimal")
    print("[2] Real Decimal para Binario")
    print("[9] SAIR")
    ans = int(input("\nDigite o numero da opcao: "))

    match ans:
        case 1:
            print("---------------------------")
            bin = input("Digite o valor na base 2 (comecando com 0.): ")
            dec = binToDec_Real(bin)
            print(f"Decimal: {dec}")
        case 2:
            print("---------------------------")
            dec = float(input("Digite o valor na base 10 (< 1): "))
            bin = decToBin_Real(dec)
            print(f"Binario: {bin}")
        case 9:
            sair = True
        case _:
            print("Codigo Invalido")