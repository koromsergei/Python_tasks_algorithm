import string
import re


def delta(k):
    if k in string.punctuation or k in string.whitespace:
        k = 0
    else:
        k = 1
    return k


def words_counter(w):
    d = 0
    i = 0
    while True:
        if len(w) == 0:
            d = 0
            break
        if delta(w[i]) == 1:
            if i == len(w) - 1:
                d += 1
                break
            if delta(w[i + 1]) == 0:
                d += 1
            i += 1
        if delta(w[i]) == 0:
            if i == len(w) - 1:
                break
            i += 1
    return d


def words_game_assistant(ws):
    # сперва вносится начальный набор слов.
    # команда выдаёт кол-во слов.
    # затем если вы слушаете слова собеседника - вы
    # вводите слова и они убираются из основного
    # списка, а также вносятся в список вычеркнутых # слов. (надо написать кто вы сейчас)
    # если вы называете слова, то вы пишите слово
    # со знаком "+", если такого слова ниукого нет,
    # тогда это слово остается в основном списке.
    # если это слово у кого-то есть, то вы пишите
    # его со знаком "-" и оно удаляется из
    # основного списка и добавляется в список
    # вычеркнутых слов.
    # в конце игры выводятся два списка:
    # 1)список уникальных слов и их кол-во
    # 2)список вычеркнутых слов и их кол-во
    print(words_counter(ws))
    words = [i for i in re.split(rf"[{string.punctuation + string.whitespace + string.digits}]+", ws) if i != '']
    deleted_words = []
    unique_words = []

    while True:
        you = input("кто вы? (слушатель/говорящий/конец игры)")
        if you == 'конец игры':
            break
        if you == "слушатель":
            listening = True
            while listening:
                input_word = input('введите слово, если слов больше нет, то напишите "всё"')
                if input_word == "всё":
                    break

                if not (input_word in words):
                    print("такого нет")
                else:
                    deleted_words.append(input_word)
                    print("такое есть")
            unique_words = words

        if you == "говорящий":
            for word in words:
                print(word)
                input_word = [word,
                     input('введите "+" если этого слова ни у кого нет / введите "-" если это слово у кого-то есть')]
                if input_word[1] == "+":
                    unique_words.append(word)
                if input_word[1] == '-':
                    deleted_words.append(word)

    return [('уникальные слова:', unique_words, 'кол-во:', len(unique_words)), ('вычеркнутые слова', set(deleted_words), 'кол-во :', len(deleted_words))]


print(words_game_assistant(input("ваш начальный список слов")))
