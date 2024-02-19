print("Задание 5. Дана строка. Необходимо найти все даты, которые описаны в виде '31 февраля 2007'.")
s=input("Введите строку: ")
months=['января','февраля','марта','арпеля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
slist=list(s.split())
datelist=[]
for i in months:
    if (i in slist):
        for j in range(slist.count(i)):
            n=slist.index(i)
            date=[slist[n-1],slist[n],slist[n+1]]
            datelist.append(" ".join(date))
print("Список дат ",datelist)