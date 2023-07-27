alphabet_RU = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_ru = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
s = input('')
s1 = ''
k = int(input())
for c in s:
    if c in alphabet_RU:
        s1 += alphabet_RU[(alphabet_RU.find(c) + k) % 32]
    elif c in alphabet_ru:
        s1 += alphabet_ru[(alphabet_ru.find(c) + k) % 32]
    else:
        s1 += c
print(s1)
