'''     #6
ввод: 1 строка - кол-во запросов, далее множество
Формат выходных данных
Выведите q строк, чтобы i-ая строка содержала
единственное целое число xi; — максимальное
значение исключающего ИЛИ по всем парам чисел
из множества после первых i операций.
        Test1
        in
4
3
2
5
2
        out
0
1
7
7
'''
a = int(input())
all_numbs = []
for item in range(a):
    all_numbs.append(int(input()))
bass = []
biggestXOR: int = 0
for item in all_numbs:
    if item not in bass:
        bass.append(item)
    if len(bass) > 1:
        for i in range(len(bass)):
            for j in range(i,len(bass)):
                XOR = bass[j] ^ bass[i]
                biggestXOR = max(biggestXOR, XOR)
    print(biggestXOR)