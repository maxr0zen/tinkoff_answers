'''         #4
ввод - число n, которое означает кол-во уголов правильного - n угольника, нужно заполнить этот n-угольник 
треугольниками так, чтобы суммарная площадь треугольников была максимальной. Вывести суммарную площадь n-угольника

            Test1
            in
3
            out
0.433013
            Test2
            in
10
            out
3.553212
'''
import math


n_corners = int(input())
part = n_corners//3

figure = []
triangles = []
triangles_leight = []

output_first_method: float = 0



def Small_Trangles(figure):
    a_point, b_point, c_point = figure[0], figure[len(figure)//2], figure[-1]
    if [a_point, b_point, c_point] not in triangles:
        triangles.append([a_point, b_point, c_point])
    if b_point - a_point > 2:
        a_range = [i for i in range(a_point + 1, b_point)]
        if len(a_range) > 2:
            Small_Trangles(figure= a_range)
    if c_point - b_point > 2:
        b_range = [i for i in range(a_point + 1, b_point)]
        if len(b_range) > 2:
            Small_Trangles(figure= b_range)
    if len(figure) - c_point > 2:
        c_range = [i for i in range(c_point + 1, len(figure))]
        if len(c_range) > 2:
            Small_Trangles(figure= c_range)
    return figure,triangles


def Triangle_first_solution(figure):
    current_part = len(figure)//3
    a_point, b_point, c_point = figure[0], figure[current_part], figure[-current_part]
    triangles.append([a_point,b_point,c_point])
    if b_point - a_point > 2:
        a_range = [figure[i] for i in range(a_point + 1,b_point )]
        if len(a_range) > 2:
            Small_Trangles(figure= a_range)
    if c_point - b_point > 2:
        b_range = [figure[i] for i in range(b_point + 1,c_point )]
        if len(b_range) > 2:
            Small_Trangles(figure= b_range)
    if len(figure) - c_point > 2:
        c_range = [figure[i] for i in range(c_point + 1, len(figure))]
        if len(c_range) > 2:
            Small_Trangles(figure= c_range)
    return figure

def Leight(triangles,n_corners):
    for item in triangles:
        a_point, b_point, c_point = item
        a_leight = Leight_calc(a=a_point,b=b_point,n_corners=n_corners)
        b_leight = Leight_calc(a=b_point,b=c_point,n_corners=n_corners)
        c_leight = Leight_calc(a=a_point,b=c_point,n_corners=n_corners)
        triangles_leight.append([a_leight,b_leight,c_leight])

def Leight_calc(a,b,n_corners):
    single_angle = 360/n_corners
    radian = (math.pi*single_angle)/180
    other_single_angle = (180 - single_angle) / 2
    other_radian = (math.pi*other_single_angle)/180
    current_sin = math.sin(radian)
    other_current_sin = math.sin(other_radian)
    radius = other_current_sin/current_sin


    if b - a > 1:
        current_angle = (b-a)*(360/n_corners)
        if current_angle == 180:
            final = 2 * radius
        else:
            if current_angle > 180: current_angle = 360 - current_angle
            current_other_angle = (180 - current_angle) / 2
            current_angle_sin = math.sin((math.pi*current_angle)/180)
            current_other_angle_sin = math.sin((math.pi*current_other_angle)/180)
            final = radius * current_angle_sin/current_other_angle_sin
    else: final = 1
    return final

def S_calc(triangles_leight):
    final:float = 0
    for item in triangles_leight:
        a,b,c = item
        p = (a + b + c) / 2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        final += s
    output = final
    return output


def Prog(n_corners):
    for i in range(n_corners): figure.append(i)
    Triangle_first_solution(figure)
    Leight(triangles,n_corners)
    output_first_method = S_calc(triangles_leight)
    triangles.clear();triangles_leight.clear();figure.clear()
    print(round(output_first_method,6))
Prog(n_corners)