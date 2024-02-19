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