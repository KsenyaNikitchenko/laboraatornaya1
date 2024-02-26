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


print("""9. В порядке увеличения квадратичного отклонения между наибольшим ASCII-кодом символа строки и максимальной
разницы в ASCII-кодах пар зеркально расположенных символов строки (относительно ее середины).""")

def max_ASCII(stroka):
    maxcod=0
    for i in stroka:
        if(ord(i)>=maxcod):
            maxcod=ord(i)
    return maxcod

def max_dif_elements(stroka):
    max_difference=0
    for i in range(len(stroka)//2):
        if(abs(ord(stroka[i])-ord(stroka[-i-1]))>max_difference):
            max_difference=abs(ord(stroka[i])-ord(stroka[-i-1]))
    if(len(stroka)%2!=0):
        if(ord(stroka[len(stroka)//2])>max_difference):
            max_difference=ord(stroka[len(stroka)//2])
    return max_difference

def deviation_ASCII_and_dif_elements(stroka):
    deviation=((max_ASCII(stroka)-max_dif_elements(stroka))**2)**0.5
    return deviation

def sort_by_ASCII(spisok):
    return sorted(spisok,key=deviation_ASCII_and_dif_elements)

spisok=["It was sunny yesterday","Hello world","Today is Febryary 26th","Soring is in 3 days","Alla Bob Jon Ivan"]
print("Изначальный список ",spisok)
print("Отсортированный список ",sort_by_ASCII(spisok))


print("""11. В порядке квадратичного отклонения дисперсии максимального среднего веса ASCII-кода тройки 
      символов в строке от максимального среднего веса ASCII-кода тройки символов в первой строке.""")

def max_weight_triple(stroka):
    maxweight=0
    for i in range(0,len(stroka),+3):
            small=stroka[i:i+3]
            weightsmall=sum(ord(j) for j in small)/len(small)
            if(weightsmall>=maxweight):
                maxweight=weightsmall
    return maxweight

def deviation_weight_triple(stroka,text):
    deviation=((max_weight_triple(stroka)-max_weight_triple(text[0]))**2)**0.5
    return deviation

def sort_by_weight_triple(text):
    for i in range(len(text)-1):
        for j in range(len(text)-i-1):
            if(deviation_weight_triple(text[j],text)>deviation_weight_triple(text[j+1],text)):
                text[j],text[j+1]=text[j+1],text[j]
    return text

spisok=["It was sunny yesterday","Hello world","Today is Febryary 26th","Soring is in 3 days","Alla Bob Jon Ivan"]
print("Изначальный список ",spisok)
print("Отсортированный список ",sort_by_weight_triple(spisok))
