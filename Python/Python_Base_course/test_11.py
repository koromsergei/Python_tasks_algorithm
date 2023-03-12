# cache = {}
# n = int(input())
# while n != 0:
#     n_2 = round(pow(n, 0.5), 2)
#     if cache.get(n) is not None:
#         print(f"значение из кэша: {cache.get(n)}")
#     else:
#         print(n_2)
#     cache[n] = n_2
#     n = int(input())
# lst_in = ['ustanovka-i-zapusk-yazyka',
#           'ustanovka-i-poryadok-raboty-pycharm',
#           'peremennyye-operator-prisvaivaniya-tipy-dannykh',
#           'arifmeticheskiye-operatsii',
#           'ustanovka-i-poryadok-raboty-pycharm']
#
# d = {}
# key = "HTML-страница для адреса"
# for i in lst_in:
#     if i not in d:
#         d[i] = key
#         print(d.get(i), i)
#     else:
#         print(f"Взято из кэша: {d.get(i) +  i} " )
morze = {"А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": ".", "Ё": ".", "Ж": "...-", "З": "--..",
         "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.", "Р": ".-.",
         "С": "...", "Т": "-", "У": "..-", "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.",
         "Ш": "----", "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--", "Ь": "-..-", "Э": "..-..", "Ю": "..--", "Я": ".-.-",
         " ": "-...-"}

message = input().split()
converted_message = []
for i in message:
    converted_message.append(morze[i])
print(*converted_message)
