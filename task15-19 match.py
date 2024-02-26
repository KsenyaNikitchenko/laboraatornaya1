from random import randint

def sovpad(x,y):
    n=0
    for i in range(len(x)):
        if(y.count(x[i])!=0):
            n+=1
    return n

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

def inrange(mas,a,b):
    inrange=[]
    for i in range(len(mas)):
        if(mas[i]>=a and mas[i]<=b):
            inrange.append(mas[i])
    return inrange

def sort(x):
    masp=[]
    maso=[]
    for i in range(len(mas)):
        if(mas[i]>=0):
            masp.append(mas[i])
        else:
            maso.append(mas[i])
    return masp+maso

def suminlist(mas):
    n=0
    for i in range(len(mas)):
        for j in range(i+1,len(mas),+1):
            if(i!=j and mas[i]+mas[j] in mas):
                n+=1
    return n

print("Список доступных функций:")
print("1. Даны два массива. Необходимо найти количество совпадающих по значению элементов.")
print("2. Дан целочисленный массив и интервал a..b. Необходимо найти количество минимальных элементов в этом интервале.")
print("3. Дан целочисленный массив и отрезок a..b. Необходимо найти элементы, значение которых принадлежит этому отрезку.")
print("4. Дан целочисленный массив. Необходимо вывести вначале его положительные элементы, а затем – отрицательные.")
print("5. Для введенного списка вывести количество элементов, которые могут быть получены как сумма двух любых других элементов списка.")
n=int(input("Введите номер функции "))
match n:
    case 1:
        n=int(input("Введите количество элементов первого массива "))
        mas1=[0]*n
        for i in range(n):
            mas1[i]=randint(-50,50)
        print(mas1)
        n=int(input("Введите количество элементов первого массива "))
        mas2=[0]*n
        for i in range(n):
            mas2[i]=randint(-50,50)
        print(mas2)
        print("Количество совпадающих элементов равно ",sovpad(mas1,mas2))
    case 2:
        a=int(input("Введите левую границу отрезка "))
        b=int(input("Введите правую границу отрезка "))
        n=int(input("Введите количество элементов массива "))
        mas=[0]*n
        for i in range(n):
            mas[i]=randint(-50,50)
        print(mas)
        print("Количество минимальных элементов в интервале ",mininrange(mas,a,b))
    case 3:
        a=int(input("Введите левую границу отрезка "))
        b=int(input("Введите правую границу отрезка "))
        n=int(input("Введите количество элементов массива "))
        mas=[0]*n
        for i in range(n):
            mas[i]=randint(-10,10)
        print(mas)
        print("Элементы из отрезка ",inrange(mas,a,b))
    case 4:
        n=int(input("Введите количество элементов массива "))
        mas=[0]*n
        for i in range(n):
            mas[i]=randint(-50,50)
        print(mas)
        print("Отсортированный массив",sort(mas))
    case 5:
        m=list(map(int,input("Введите список чисел через пробел: ").split()))
        print("Количество элементов, которые являются суммой 2х других элементов, равно",suminlist(m))
    case _:
        print("Номер функции должен лежать в диапазоне от 1 до 5")