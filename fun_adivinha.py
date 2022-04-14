negrito = '\033[;1m'
vermelhor = '\033[1;31m'
verde = '\033[1;32m'
cyan = '\033[1;36m' 
margenta = '\033[1;95m'

def game_dif():
    while True:
        print(f'Escolha a dificudade:\n{negrito}(1)\033[m Fácil = 15\n{negrito}(2)\033[m Médio = 10\n{negrito}(3)\033[m Díficl = 5')
        dificultade = leiaInt()

        if dificultade == 1:
            return 15
        elif dificultade == 2:
            return 10
        elif dificultade == 3:
            return 5
        else:
            print(f'\n{vermelhor}Digite apenas uma das opções\033[m')
            

def acerta_num(dificuldade, num_secreto, tent):
    while tent <= dificuldade:
        print(f'\n{cyan}{tent} de {dificuldade} tentativas\033[m')
        user = leiaInt()
        
        if user == num_secreto:
            print(f'\n{verde}Parabéns, você acertou em {tent} tentativas. O número era {num_secreto}\033[m')
            break
        
        elif user > 100 or user < 1:
            print(f'{vermelhor}Valor invalido. Digite numeros entre [1 e 100]\033[m')

        else:
            if user > num_secreto:
                print(f'{vermelhor}Errado.\033[m O valor é {negrito}menor\033[m')
            else:
                print(f'{vermelhor}Errado.\033[m O valor é {negrito}maior\033[m')

            tent += 1
            if tent > dificuldade:
                print(f'\n{margenta}Infelizmente você não acertou. O número era {num_secreto}\033[m')


def leiaInt():
    while True:
        try:
            num = int(input('Digite um número: '))
        except (TypeError, ValueError):
            print(f'{vermelhor}Digite apenas números inteiros\033[m')
        else:
            return num