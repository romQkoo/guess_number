from random import randint

# Загаданное компьютером число
number_abcd = randint(1, 100)
print("Угадай число :)")
cnt = 0

# Сам цикл с игрой
def aaa():
    while True:
        num_player = int(input("Введи число: "))

        # Если меньше
        if num_player < number_abcd:
            print("Твое число меньше загаданного")
            cnt += 1

        # Если больше
        if num_player > number_abcd:
            print("Твое число больше загаданного")
            cnt += 1

        # Если равно
        if num_player == number_abcd:
            print("Твое число равно загаданному, поздравляю!")
            break

print(f"Красавчик, вообще лучший, молодцом! Количество попыток равно {cnt}")


aaa()