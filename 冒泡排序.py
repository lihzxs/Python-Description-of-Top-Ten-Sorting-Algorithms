def Babble_Sort(a:list):
    len_a = len(a)
    for i in range(len_a - 2):   #为什么是减2？？
        flag = False
        for j in range(0,len_a-i-1): #减i和减1是什么意思？？
            if a[j+1] < a[j]:
                a[j+1],a[j] = a[j],a[j+1]
                flag = True    #发生了交换
        if not flag:    #没有发生交换，，意味着前面已经有序了
            break
        print(a)

a = [100,1,3,0,56,34,22]

Babble_Sort(a)
    