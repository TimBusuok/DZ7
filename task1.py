# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                     Вывод:Парам пам-пам
# пара-ра-рам рам-пам-папам па-ра-па-дам

def check_stroki(stroki):
    words = stroki.split()
    rifma = []
    for word in words:
        rifma.append((word.count('а') + word.count('е') + word.count('ё') + word.count('и') + word.count('о') + word.count('у') + word.count('ы') + word.count('э') + word.count('ю') + word.count('я')))
         
    if len(set(rifma)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'


stroki = input('Введите строчку: ')
print(check_stroki(stroki))