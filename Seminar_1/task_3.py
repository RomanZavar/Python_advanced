# Программа загадывает число от 0 до 1000. Необходимо угадать число
# за 10 попыток. Программа должна подсказывать «больше» или «меньше»
#  после каждой попытки. Для генерации случайного числа используйте код:



# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT) 

import random
print('Отгадай число от 0 до 1000. Я буду давать подсказки у тебя 10 попыток')
the_number = random.randint(1, 1001)
user = int(input("Ваше предположение: "))
attempts = 9
while user != the_number:
    if user > the_number:
        print("Меньше (；⌣̀_⌣́)")
    else:
        print("Больше (」°ロ°)」")
    if attempts == 0:
        break
    user = int(input("Ваше предположение : "))
    attempts -= 1
 
if user != the_number:
    print("Глупые человеки 凸(￣ヘ￣)凸 скоро мы вас поработим")
else:
    print("Угадал ヽ(・∀・)ﾉ")