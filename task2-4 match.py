def polindrom(s):
    f=1
    n=len(s)
    for i in range (n):
        if s[i]!=s[n-1-i]:
            f=0
            break
    if f!=0:
        return "Строка является полиндромом"
    else:
        return "Строка не является полиндромом"

def difnums(x):
    t=[x%10]; x//=10
    while (x>0):
        if(t.count(x%10)==0):
            t.append(x%10)
        x//=10
    n=0
    for i in t:
        n+=1
    return n

print("Список доступных функций:")
print("1. Проверить, является ли строка палиндромом.")
print("2. Необходимо посчитать количество слов, записанных через пробел")
print("3. Найти количество различных цифр в десятичной записи натурального числа")

n=int(input("Введите номер функции "))
match n:
    case 1:
        s=input("Введите строку: ")
        print(polindrom(s))
    case 2:
        s=input("Введите строку: ")
        t=s.split()
        print("Число слов в строке равно ",len(t))
    case 3:
        x=int(input("x = "))
        print("Число различных цифр в числе равно ",difnums(x))
    case _:
        print("Номер функции должен лежать в диапазоне от 1 до 3")