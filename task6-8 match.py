def kolnums(s):
    t=s.split()
    n=0
    for i in t:
        if(i.isdigit() and len(i)<2):
            if(ord(i)<53):
                n+=1
    return n

def notabc(s):
    abc=[]
    n=0
    for i in s:
        if(i.isalpha() and abc.count(i.lower())==0):
            abc.append(i.lower())
    abc.sort()
    nots=[]
    if(len(abc)!=26):
        for i in range(97,123,+1):
            if(abc.count(chr(i))!=1):
                n+=1
                nots.append(chr(i))
    return nots

def kolnums5(s):
    t=s.split()
    n=0
    for i in t:
        if(i.isdigit() and len(i)<2):
            if(ord(i)<53):
                n+=1
        elif (i.isdigit()and len(i)>=2):
            for j in range(len(i)):
                if(ord(i[j])>53 and ord(i[j])<=57):
                    n+=1
    return n

print("Список доступных функций:")
print("1. Дана строка. Необходимо подсчитать количество чисел в этой строке, значение которых меньше 5.")
print("2. Дана строка. Необходимо найти все незадействованные символы латиницы в этой строке.")
print("3. Дана строка. Необходимо подсчитать количество цифр в этой строке, значение которых больше 5.")
n=int(input("Введите номер функции "))
match n:
    case 1:
        s=input("Введите строку: ")
        print("Количество чисел в строке, которые меньше 5, равно ",kolnums(s))
    case 2:
        s=input("Введите строку: ")
        nots=notabc(s)
        print("В данной строке отсутствует ",len(nots)," символов латинского алфавита")
        print(nots)
    case 3:
        s=input("Введите строку: ")
        print("Количество цифр в строке, значение которых больше 5, равно ",kolnums5(s))
    case _:
        print("Номер функции должен лежать в диапазоне от 1 до 3")