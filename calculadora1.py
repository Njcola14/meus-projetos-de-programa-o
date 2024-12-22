import time
def somar(x,y):
    return x + y

def subtração(x , y):
    return x - y

def mutiplicação(x,y):
    return x * y

def divisão(x,y):
    return x / y

def calculadora():
    while True:
        print(" =============================================")
        print("|                                             |")
        print("|                 1-somar                     |")
        print("|                 2-subtração                 |")
        print("|                 3-mutiplicação              |")
        print("|                 4-divisão                   |")
        print("|                 5-sair                      |")
        print(" =============================================")
        try:
            escolha = int(input("escolha um numero de 1-5: "))
            if escolha == 5:
                break
            if escolha not in [1,2,3,4]:
                print("escolha apenas numeros de 1 a 5 !!!!!")
                continue
            numero1 = float(input("escreva o seu 1 numero"))
            numero2 = float(input("escreva o seu 2 numero"))
            if escolha == 1:
                print(f"a soma de {numero1} e {numero2} é: {somar(numero1,numero2)}")
            elif escolha == 2:
                print(f"a subtração de {numero1} e {numero2} é: {subtração(numero1,numero2)}")
            elif escolha == 3:
                print(f"a mutiplicação de {numero1} e {numero2} é: {mutiplicação(numero1,numero2)}")
            elif escolha == 4:
                print(f"a divisão de {numero1} e {numero2} é: {divisão(numero1,numero2)}")
        except ValueError:
            print("apenas numeros!!!")
calculadora()
