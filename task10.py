def slova(s):
    slist=s.split()
    return len(slist)
print("Задание 10. Дан список строк с клавиатуры. Упорядочить по количеству слов в строке.")
n=int(input("Введите количество элементов списка "))
slist=[]
for i in range(n):
    slist.append(input())
print("Отсортированный список:",sorted(slist,key=slova))