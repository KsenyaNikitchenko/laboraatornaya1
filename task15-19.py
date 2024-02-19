from random import randint
N=10
print("Задание 15-19. Вариант ",(N-1)%12+1)

def sovpad(x,y):
    n=0
    for i in range(len(x)):
        if(y.count(x[i])!=0):
            n+=1
    return n
print("10. Даны два массива. Необходимо найти количество совпадающих по значению элементов.")
n=int(input("Введите количество элементов первого массива "))
mas1=[0]*n
for i in range(n):
    mas1[i]=randint(-10,10)
print(mas1)
n=int(input("Введите количество элементов первого массива "))
mas2=[0]*n
for i in range(n):
    mas2[i]=randint(-10,10)
print(mas2)
print("Количество совпадающих элементов равно ",sovpad(mas1,mas2))

def mininrange(mas,a,b):
    mas.sort()
    min=mas[-1]
    for i in range(len(mas)):
        if(a<=mas[i]<=b and mas[i]<=min):
            min =mas[i]
    if(min==mas[-1] and not a<=min<=b):
        return 0
    else:
        return mas.count(min)

print("22. Дан целочисленный массив и интервал a..b. Необходимо найти количество минимальных элементов в этом интервале.")
a=int(input("Введите левую границу отрезка "))
b=int(input("Введите правую границу отрезка "))
n=int(input("Введите количество элементов массива "))
mas=[0]*n
for i in range(n):
    mas[i]=randint(-10,10)
print(mas)
print("Количество минимальных элементов в интервале ",mininrange(mas,a,b))

def inrange(mas,a,b):
    inrange=[]
    for i in range(len(mas)):
        if(mas[i]>=a and mas[i]<=b):
            inrange.append(mas[i])
    return inrange
print("34. Дан целочисленный массив и отрезок a..b. Необходимо найти элементы, значение которых принадлежит этому отрезку.")
a=int(input("Введите левую границу отрезка "))
b=int(input("Введите правую границу отрезка "))
n=int(input("Введите количество элементов массива "))
mas=[0]*n
for i in range(n):
    mas[i]=randint(-10,10)
print(mas)
print("Количество совпадающих элементов равно ",inrange(mas,a,b))

def sort(x):
    masp=[]
    maso=[]
    for i in range(len(mas)):
        if(mas[i]>=0):
            masp.append(mas[i])
        else:
            maso.append(mas[i])
    return masp+maso
print("46. Дан целочисленный массив. Необходимо вывести вначале его положительные элементы, а затем – отрицательные.")
n=int(input("Введите количество элементов массива "))
mas=[0]*n
for i in range(n):
    mas[i]=randint(-10,10)
print(mas)
print("Отсортированный массив",sort(mas))
