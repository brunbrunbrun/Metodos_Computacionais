import math

# Funções das equações
def func1(x):
    return 7*x**3 - x**2 - 28*x + 4

def func2(x):
    return 6*x**4 - 7*x**3 - 33*x**2 + 35*x + 15

# Método da Bissecção
def bissec(func, a, b, epsilon):
    ak = a
    bk = b
    xk = (a + b) / 2
    k = 0
    while abs(bk - ak) > epsilon:
        xk = (ak + bk) / 2
        if func(xk) * func(ak) < 0:
            bk = xk
        else:
            ak = xk
        k += 1
    return k, ak, bk, xk, func(ak), func(bk), func(xk), bk - ak

# Método da Posição Falsa
def posicao_falsa(func, a, b, epsilon, iteracoes_maximas=1000):
    ak = a
    bk = b
    f_ak = func(ak)
    f_bk = func(bk)
    
    if f_ak * f_bk >= 0:
        raise ValueError("Intervalo não contem uma raiz")

    for k in range(1, iteracoes_maximas + 1):
        xk = ak - (f_ak * (bk - ak)) / (f_bk - f_ak)
        f_xk = func(xk)
        
        if abs(f_xk) < epsilon:
            return k, ak, bk, xk, f_ak, f_bk, f_xk, bk - ak
        
        if f_xk * f_ak < 0:
            bk = xk
            f_bk = f_xk
        else:
            ak = xk
            f_ak = f_xk
    
    raise ValueError("Numero maximo de iterações alcançado")

# Método de Newton
def newton(func, func_primo, x0, epsilon):
    xk = x0
    k = 0
    while abs(func(xk)) > epsilon:
        xk = xk - func(xk) / func_primo(xk)
        k += 1
    return k, xk, func(xk)

# Método da Secante
def secante(func, x0, x1, epsilon):
    xk_menos_1 = x0
    xk = x1
    k = 0
    while abs(func(xk)) > epsilon:
        xk_mais_1 = xk - (func(xk) * (xk - xk_menos_1)) / (func(xk) - func(xk_menos_1))
        xk_menos_1 = xk
        xk = xk_mais_1
        k += 1
    return k, xk, func(xk)


# Primeira função com apenas um intervalo
funcoes = [(func1, '7x^3 - x^2 - 28x + 4')]
intervalos = [([0, 1], 'Intervalo [0, 1]')]
precisoes = [1e-5]

# Execução do programa
for func, func_nome in funcoes:
    print(f"Função: {func_nome}\n")
    for intervalo, intervalo_nome in intervalos:
        print(f"Intervalo: {intervalo_nome}")
        for epsilon in precisoes: 
            x_escolhido = 0         
            print(f"\nPrecisão: {epsilon}")
            print("Metodo\t k\t ak\t\t bk\t\t xk\t\t f(ak)\t\t f(bk)\t\t f(xk)\t\t bk - ak")
            print("="*121)
            
            # Bissecção
            k, ak, bk, xk, f_ak, f_bk, f_xk, bk_ak = bissec(func, intervalo[0], intervalo[1], epsilon)
            print(f"Bissec\t {k}\t {ak:.6f}\t {bk:.6f}\t {xk:.6f}\t {f_ak:.6f}\t {f_bk:.6f}\t {f_xk:.6f}\t {bk_ak:.6f}")            
            # Pegar o X se o f(xk) for entre 1e-7 e -1e-7
            if(f_xk < 0.0000001 and f_xk > -0.0000001):
                x_escolhido = xk

            # Posição Falsa            
            try:
                k, ak, bk, xk, f_ak, f_bk, f_xk, bk_ak = posicao_falsa(func, intervalo[0], intervalo[1], epsilon)
                print(f"P_Falsa\t {k}\t {ak:.6f}\t {bk:.6f}\t {xk:.6f}\t {f_ak:.6f}\t {f_bk:.6f}\t {f_xk:.6f}\t {bk_ak:.6f}")
                # Pegar o X se o f(xk) for entre 1e-7 e -1e-7
                if(f_xk < 0.0000001 and f_xk > -0.0000001):
                    x_escolhido = xk                   
            except ValueError as e:
                print(f"P_Falsa\t -\t -\t -\t -\t -\t -\t {e}\t -")
            
            # Newton
            func_primo = lambda x: (func(x + epsilon) - func(x)) / epsilon
            k, xk, f_xk = newton(func, func_primo, sum(intervalo) / 2, epsilon)
            print(f"Newton\t {k}\t -\t\t -\t\t {xk:.6f}\t -\t\t -\t\t {f_xk:.6f}\t -")
            # Pegar o X se o f(xk) for entre 1e-7 e -1e-7
            if(f_xk < 0.0000001 and f_xk > -0.0000001):
                x_escolhido = xk
            
            # Secante
            k, xk, f_xk = secante(func, intervalo[0], intervalo[1], epsilon)
            print(f"Secante\t {k}\t {intervalo[0]:.6f}\t {intervalo[1]:.6f}\t {xk:.6f}\t {func(intervalo[0]):.6f}\t {func(intervalo[1]):.6f}\t {f_xk:.6f}\t {intervalo[1] - intervalo[0]:.6f}")
            # Pegar o X se o f(xk) for entre 1e-7 e -1e-7
            if(f_xk < 0.0000001 and f_xk > -0.0000001):
                x_escolhido = xk
            print("-"*121)
            print(f"\t\t\t\t\tX escolhido: {x_escolhido:.6f}")
        print("\n")

    print("=|"*60+"=")
    print("\n")


# Segunda função com ademais intervalos
funcoes = [(func2, '6x^4 - 7x^3 - 33x^2 + 35x + 15')]
intervalos = [([-3, -2], 'Intervalo [-3, -2]'), ([-1, 0], 'Intervalo [-1, 0]'), ([1, 2], 'Intervalo [1, 2]'), ([2, 3], 'Intervalo [2, 3]')]
precisoes = [1e-7]

# Execução do programa
for func, func_nome in funcoes:
    print(f"Função: {func_nome}\n")
    for intervalo, intervalo_nome in intervalos:
        print(f"Intervalo: {intervalo_nome}")
        for epsilon in precisoes:
            x_escolhido = 0 
            print(f"\nPrecisão: {epsilon}")
            print("Metodo\t k\t ak\t\t bk\t\t xk\t\t f(ak)\t\t f(bk)\t\t f(xk)\t\t bk - ak")
            print("="*121)
            
            # Bissecção
            k, ak, bk, xk, f_ak, f_bk, f_xk, bk_ak = bissec(func, intervalo[0], intervalo[1], epsilon)
            print(f"Bissec\t {k}\t {ak:.6f}\t {bk:.6f}\t {xk:.6f}\t {f_ak:.6f}\t {f_bk:.6f}\t {f_xk:.6f}\t {bk_ak:.6f}")
            # Pegar o X se o f(xk) for entre 1e-7 e -1e-7
            if(f_xk < 0.0000001 and f_xk > -0.0000001):
                x_escolhido = xk

            # Posição Falsa            
            try:
                k, ak, bk, xk, f_ak, f_bk, f_xk, bk_ak = posicao_falsa(func, intervalo[0], intervalo[1], epsilon)
                print(f"P_Falsa\t {k}\t {ak:.6f}\t {bk:.6f}\t {xk:.6f}\t {f_ak:.6f}\t {f_bk:.6f}\t {f_xk:.6f}\t {bk_ak:.6f}")
                # Pegar o X se o f(xk) for entre 1e-7 e -1e-7
                if(f_xk < 0.0000001 and f_xk > -0.0000001):
                    x_escolhido = xk
            except ValueError as e:
                print(f"P_Falsa\t -\t -\t -\t -\t -\t -\t {e}\t -")
            
            # Newton
            func_primo = lambda x: (func(x + epsilon) - func(x)) / epsilon
            k, xk, f_xk = newton(func, func_primo, sum(intervalo) / 2, epsilon)
            print(f"Newton\t {k}\t -\t\t -\t\t {xk:.6f}\t -\t\t -\t\t {f_xk:.6f}\t -")
            # Pegar o X se o f(xk) for entre 1e-7 e -1e-7
            if(f_xk < 0.0000001 and f_xk > -0.0000001):
                x_escolhido = xk

            # Secante
            k, xk, f_xk = secante(func, intervalo[0], intervalo[1], epsilon)
            print(f"Secante\t {k}\t {intervalo[0]:.6f}\t {intervalo[1]:.6f}\t {xk:.6f}\t {func(intervalo[0]):.6f}\t {func(intervalo[1]):.6f}\t {f_xk:.6f}\t {intervalo[1] - intervalo[0]:.6f}")
            # Pegar o X se o f(xk) for entre 1e-7 e -1e-7
            if(f_xk < 0.0000001 and f_xk > -0.0000001):
                x_escolhido = xk
            print("-"*121)
            print(f"\t\t\t\t\tX escolhido: {x_escolhido:.6f}")
        print("\n")
    print("=|"*60+"=")
    print("\n")