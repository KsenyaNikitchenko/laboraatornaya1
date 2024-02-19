from random import randint
N=10
print("Задание 15-19. Вариант ",(N-1)%12+1)


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
print(inrange(mas,a,b))