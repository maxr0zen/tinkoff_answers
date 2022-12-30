'''     #5
ввод: первая строка - кол-во городов и рейсов, далее рейс(начальный город, конечный город, четность дня)
вывод: максимальная длинна коротчайшего маршрута, или -1, если можно построить такой маршрут, при котором не получится
достичь последнего города
        Test1
        in
3 3
1 2 0
1 3 1
2 3 0
        out
-1
011
        Test2
        in
4 6
1 3 0
3 4 0
3 4 1
1 2 1
2 3 1
2 4 0
        out
3
1111
'''
n, m = map(int, input().split())
stopFlag = False


def dfs(graph,start,visited):
    if start + 1 == n: return visited
    if len(graph[start]) == 0: return -1
    result = graph[start]
    for item in result: return dfs(graph, item, visited + 1)
    everyFalse = False
    if -1 in result: everyFalse = len(set(result))
    if len(result) > 1 and len(result) != everyFalse:

        for idx in range(0,len(result)):
            if result[idx] == -1: result.remove(result[idx + 1])
    return min(result)


races = []
for item in range(0,m):
    start, finish, day = map(int, input().split())
    races.append([start - 1,finish - 1,day])

races_in_dict = [{'odd':[], 'even':[]} for i in range(0,n)]


for item in races:
    if item[2] == 0:
        races_in_dict[item[0]]['even'] = races_in_dict[item[0]].get('even',[]) + [item[1]]
    else: races_in_dict[item[0]]['odd'] = races_in_dict[item[0]].get('odd',[]) + [item[1]]


all_races_str = []


for item in range(0,n**2):
    current_race = str(bin(item))[2::]
    if len(current_race) <= n:
        if len(current_race) != n:
            current_race = current_race.rjust(n,'0')
        all_races_str.append(current_race)


all_races_int = []
graph = []
all_answers = []

for part in all_races_str:
    foo = []
    foo_2 = [[] for i in range(0,n)]
    for item in range(len(part)):
        foo.append(int(part[item]))
    all_races_int.append(foo)
    all_items = ''
    for item in range(0,len(foo)):
        all_items += str(foo[item])
        if foo[item] == 1: foo_2[item] += (races_in_dict[item]['odd'])
        elif foo[item] == 0: foo_2[item] += (races_in_dict[item]['even'])
        else: foo_2[item] += []
        minPath = dfs(foo_2,0,0)
    answer = {'min': 0, 'binary': ''}
    if minPath == -1 or minPath != stopFlag:
        answer['min'] = minPath
        answer['binary'] = str(all_items)
        stopFlag = True
    if answer['min'] == None and answer['min'] != stopFlag:
        answer['min'] = minPath
        answer['binary'] = str(all_items)
    if answer['min'] != None and answer['min'] != stopFlag:
        if answer['min'] <= minPath:
            answer['min'] = minPath
            answer['binary'] = str(all_items)
    all_answers.append(answer)
final_with = []
final_without = []
max = 0
for item in all_answers:
    if item['min'] == -1:
        final_with.append(item)
    if item['min'] >= max:
        final_without.append(item)
if len(final_with) > 0:
    print(final_with[-1]['min'])
    print(final_with[-1]['binary'])
else:
    print(final_without[-1]['min'])
    print(final_without[-1]['binary'])