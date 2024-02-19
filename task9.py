print("Задание 9. Прочитать список строк с клавиатуры. Упорядочить по длине строки.")
n=int(input("Введите количество элементов списка "))
slist=[]
for i in range(n):
    slist.append(input())
print("Отсортированный список:",sorted(slist,key=len))