def Insertion_Sort(a:list):
    len_a = len(a)
    for i in range(1,len_a):
        index = i         #保存当前的值
        temp = a[i]

        while index - 1 >= 0 and a[index - 1] > temp:   #找前面比他小的
            a[index] = a[index - 1]
            index-=1
        a[index] = temp
        print(a)

a = [100,1,3,0,56,34,22]
Insertion_Sort(a)