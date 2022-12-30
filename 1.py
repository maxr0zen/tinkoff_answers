'''         #1
Если B и Y внутри слова чередуются, то слово - правильное, нужно вывести количество неправильных слов
            Test 1
            in
7
Tinkoff
BYBYBYB
            out
0

            Test2
            in
27
Algorithms and Data Structures
BBBBBBBBBBBYBYYYYBBBBBBBBBB
            out
3
'''

letters_count = int(input())
words = str(input()).split()
colours = str(input())

if letters_count > 101: exit()

words_leight = []
colours_sep = []
incorrect_words: int = 0
now = 0

for item in words:
    words_leight = len(item)
    current_word = colours[now:words_leight + now:]
    now += words_leight
    for letter in range(1,len(current_word)):
        if current_word[letter] == current_word[letter - 1]:
            incorrect_words += 1
            break
        else: pass

print(incorrect_words)