n=10
print("Задание 2-4. Вариант ",(n-1)%12+1)
print("4. Дана строка. Необходимо проверить, является ли она палиндромом.")

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

s=input("Введите строку: ")
print(polindrom(s))