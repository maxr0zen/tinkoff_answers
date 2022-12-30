'''     #2
1 строка ввода - ценности валют, 2 - количество, нужно вывести кол-во различных троек значений, которое можно получить путем обменных операций
        Test1
        in
1 1 1
1 0 2
        out
10

        Test2
        in
1 2 3
3 5 4
        out
28
'''
A,B,C = map(int, input().split())
a,b,c = map(int, input().split())

counter: int = (a//A) + (b//B) + (c//C) + 1
print(int(counter * (counter + 1) / 2))