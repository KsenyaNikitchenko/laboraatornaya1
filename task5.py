def date_in_string(string):
    months=['января','февраля','марта','арпеля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
    slist=list(string.split())
    datelist=[]
    for i in months:
        if (i in slist):
            for j in range(slist.count(i)):
                n=slist.index(i)
                if(slist[n-1].isdigit() and slist[n+1].isdigit()):
                    date=[slist[n-1],slist[n],slist[n+1]]
                    datelist.append(" ".join(date))
    return datelist

print("Задание 5. Дана строка. Необходимо найти все даты, которые описаны в виде '31 февраля 2007'.")
listofdates=input("Введите строку: ")
print("Список дат: ",date_in_string(listofdates))
