n=10
print("Задание 1. Вариант ",(n-1)%12+1)
print("Функция 1. Найти количество четных чисел, не взаимно простых с данным.")

def maxod(x,y):
    while(x!=0 and y!=0):
        if x>y:
            x%=y
        else:
            y%=x
    return x+y

def nsimplenums(x):
    n=0
    i=2
    while i<x:
        if maxod(x,i)!=1:
            n+=1
        i+=2
    return n

x=int(input("Введите число: "))
print(nsimplenums(x))