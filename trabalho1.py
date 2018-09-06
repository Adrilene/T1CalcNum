# coding: utf-8

# f(d) = a*e^d - 4*d^2
e = 2.71
def mov(d, a):
    r = a*(e**d)-4*(d**2)
    return r


def bissecao(n, a, ep):
    #intervalo
    y = 0.0
    z = 1.0
    if (mov(y,a)*mov(z,a) > 0):
        print("Erro intervalo") 
    
    while(abs(z-y)>ep) :
        x = float((y+z)/2)
        if (mov(y,a) * mov(x,a) < 0):
            z = x
        elif (mov(y,a) * mov(x,a) >0):
            y = x        

    print ('Intervalo: ', y, ' a ', z)
def main():
    print("--------------------------------")
    print("Escolha opção: ")
    print("1 - Bisseção")
    print("2 - Newton-Raphson")
    print("3 - Secante")
    op = input("Digite opção: ")
    print("--------------------------------")
   
    a = float(input("Digite o valor de a: "))
    n = input("Digite o número de repetições: ")
    ep = float(input("Digite o valor da precisão: "))

    print(" ")
    if op == 1:
        print("Você escolheu bisseção")
        bissecao(n, a, ep)
    elif op == 2: 
        print("Você escolheu Newton-Raphson")
    elif op == 3:
        print("Você escolheu Secante")

main()