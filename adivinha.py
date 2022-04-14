from random import randrange
import fun_adivinha

num_secreto = randrange(1, 101)
tent = 1

print('Tente acerta o número entre \033[;1m[1 e 100]\033[m\n')

dificuldade = fun_adivinha.game_dif()
fun_adivinha.acerta_num(dificuldade, num_secreto, tent)

