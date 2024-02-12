n=10
print("Задание 6-8. Вариант ",(n-1)%12+1)
print("4. Дана строка. Необходимо подсчитать количество чисел в этой строке, значение которых меньше 5.")

def kolnums(s):
    t=s.split()
    n=0
    for i in t:
        if(i.isdigit() and len(i)<2):
            if(ord(i)<53):
                n+=1
    return n
    
s=input("Введите строку: ")
print("Количество чисел в строке, которые меньше 5, равно ",kolnums(s))

print("15. Дана строка. Необходимо подсчитать количество цифр в этой строке, значение которых больше 5.")

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

s=input("Введите строку: ")
print("Количество цифр в строке, значение которых больше 5, равно ",kolnums5(s))
