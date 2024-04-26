def selection_Sort(a:list):
    len_a = len(a)
    for i in range(len_a):
        index = i
        for j in range(i+1,len_a):
            if a[j] < a[index]:
                index = j

        a[index],a[i] = a[i],a[index]      

def bucket_Sort(a:list):
    #生成三个桶，，对每个桶内元素进行单独排序
    #桶内排序使用选择排序
    s = [[],[],[]]
    #枚举a列表中的元素满足范围的放入不同的桶
    for i in range(len(a)):
        if a[i] >= 0 and a[i] < 10:
            s[0].append(a[i])
        elif a[i] >= 10 and a[i] < 30:
            s[1].append(a[i])
        else:
            s[2].append(a[i])
    
    #对三个桶中的元素进行选择排序
    selection_Sort(s[0])
    selection_Sort(s[1])
    selection_Sort(s[2])

    for i in range(len(s)):
        if isinstance(s[i],list):
            for j in range(len(s[i])):
                print(s[i][j],end=' ')

a = [100,1,3,0,56,34,22]
bucket_Sort(a)