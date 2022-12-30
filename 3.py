'''         #3
ввод - число а, нужно вывести пару чиссел, которые в сумме дают а и НОК которых будет минимальным
            Test1
            in
3
            out
1 2
            Test2
            in
6
            out
3 3
            Test3
            in
9
            out
3 6
'''
answer = int(input())
pares = []
nod = []
min = 999

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

for item in range(1,answer//2 + 1):
    a = item
    b = answer - item
    pares.append([a, b])
    nod.append(a * b // gcd(a,b))

for index in range(len(nod)):
    if min > nod[index]:
        min = nod[index]
        foo = index
    else: pass

min_a, min_b = pares[foo]
print(min_a, min_b)