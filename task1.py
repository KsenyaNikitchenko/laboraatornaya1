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
print("Количество четных чисел, не взаимно простых с данным, равно",nsimplenums(x))

print("Функция 2. Найти максимальную цифру числа, не делящуюся на 3.")

def numbernot3(x):
    tmax=-1
    while(x>0):
        t=x%10
        if(t%3!=0 and tmax <t):
            tmax=t
        x//=10
    return tmax

x=int(input("Введите число: "))
if(numbernot3(x)!=-1):
    print("Максимальная цифра числа, не делящаяся на 3, равна ", numbernot3(x))
else:
    print("В данном числе все цифры делятся на 3")
