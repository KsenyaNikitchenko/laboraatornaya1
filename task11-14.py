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
