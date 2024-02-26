N=10
print("Задание 11-14. Вариант ",(N-1)%12+1)

def razn(s):
    ns=ng=0
    glasn=['a','e','i','o','q','u','y','а','е','ё','и','о','у','ы','э','ю','я']
    for i in s:
        if(i.isalpha()):
            if(i in glasn):
                ng+=1
            else:
                ns+=1
    return ns-ng
print("1. В порядке увеличения разницы между количеством согласных и количеством гласных букв в строке.")
n=int(input("Введите количество элементов списка "))
slist=[]
for i in range(n):
    slist.append(input())
print(slist)
print("Отсортированный список:",sorted(slist,key=razn))


print("""5. В порядке увеличения квадратичного отклонения частоты встречаемости самого часто встречаемого
в строке символа от частоты его встречаемости в текстах на этом алфавите.""")

def element_in_string(s):
    alpha=""
    counteleminstr=0
    for i in s:
        if(s.count(i)>counteleminstr):
            alpha=i
            counteleminstr=s.count(i)
    return alpha
def elements_in_text(text):
    alpha=""
    elements={}
    for i in text:
        alpha=element_in_string(i)
        if(alpha not in elements):
            elements[alpha]=i.count(alpha)
        else:
            elements[alpha]+=i.count(alpha)
    return elements

def deviation(string,text):
    element=element_in_string(string)
    countelintext=elements_in_text(text)[element]
    deviation=((string.count(element)-countelintext)**2)**0.5
    return deviation

def sort_by_frequency(text):
    for i in range(len(text)-1):
        for j in range(len(text)-i-1):
            if(deviation(text[j],text)>deviation(text[j+1],text)):
                text[j],text[j+1]=text[j+1],text[j]
    return text

spisok=["Hello world","I am bobr","apple banana kiwi melon","Alla Bob Jon Ivan"]
print("Изначальный список ",spisok)
print("Отсортированный список ",sort_by_frequency(spisok))


def max_w(s):
    max_weigh=0
    for i in range(0,len(s),+3):
        small=s[i:i+3]
        n=sum(ord(j) for j in small)/3
        if(n>=max_weigh):
            max_weigh=n
    return max_weigh
def otkl(s):
    return max_w(s[0])-max_w(s[1])
print("""11. В порядке квадратичного отклонения дисперсии максимального среднего веса ASCII-кода тройки 
      символов в строке от максимального среднего веса ASCII-кода тройки символов в первой строке.""")
n=int(input("Введите количество элементов списка "))
slist=[]
for i in range(n):
    slist.append(input())
for i in slist:
    print(i, max_w(i))
print("Отсортированный список:",sorted(slist,key=max_w))
