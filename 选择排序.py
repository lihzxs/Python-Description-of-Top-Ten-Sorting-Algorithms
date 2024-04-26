def seletion_Sort(a:list):
    len_a = len(a)

    for i in range(len_a):
        index = i
        for j in range(i+1,len_a):
            if a[j]<a[index]:
                index = j
        
        a[index],a[i] = a[i],a[index]
        print(a)

a = [100,1,3,0,56,34,22]

seletion_Sort(a)