import random

def main():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while tentativas < max_tentativas:
        tentativa = int(input("Tentativa {}: ".format(tentativas + 1)))

        if tentativa < numero_secreto:
            print("O número secreto é maior.")
        elif tentativa > numero_secreto:
            print("O número secreto é menor.")
        else:
            print("Parabéns! Você acertou o número secreto em {} tentativas.".format(tentativas + 1))
            return
        
        tentativas += 1

    print("Suas {} tentativas acabaram. O número secreto era {}.".format(max_tentativas, numero_secreto))

main()