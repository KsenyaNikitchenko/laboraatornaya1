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

print("Функция 3. Найти произведение максимального числа, не взаимно простого с данным,\nне делящегося на наименьший делитель исходно числа, и суммы цифр числа, меньших 5.")

def minod(x):
    tmin=1
    i=2
    while (i<x):
        if (x%i==0):
            tmin=i
            break
        i+=1
    return tmin

def number(x):
    t=x
    i=x
    n=minod(x)
    while i>0:
        if (maxod(x,i)!=1 and i%n!=0):
            t=i
            break
        i-=1
    return t

def sum5(x):
    sum=0
    while (x!=0):
        if(x%10<5):
            sum+=x%10
        x//=10
    return sum

x=int(input("Введите число: "))
print("Произведение равно ",x*number(x))
print("Сумма цифр в произведении, меньших 5, равна ",sum5(x*number(x)))
x=int(input("Введите число: "))
if(numbernot3(x)!=-1):
    print("Максимальная цифра числа, не делящаяся на 3, равна ", numbernot3(x))
else:
    print("В данном числе все цифры делятся на 3")
