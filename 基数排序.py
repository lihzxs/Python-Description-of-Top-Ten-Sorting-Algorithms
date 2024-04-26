def radix_sort(a: list):
    max_a = max(a)   #获取最大值
    max_str = str(max_a)   
    max_str_len = len(max_str)  #获取最大值的位数
    base = 1
    cnt = 0

    s = []
    #生成0 ~ 9 个桶
    for i in range(10):
        s.append([])
    
    while cnt < max_str_len:
        for i in range(len(a)):
            result = a[i] // base % 10
            s[result].append(a[i])
        
        index = 0
        for i in range(len(s)):
            temp = s[i]
            for j in range(len(temp)):
                a[index] = temp[j]
                index+=1
            s[i] = []
        base*=10
        cnt+=1

a = [100, 1, 3, 0, 56, 34, 22]
radix_sort(a)
print(a)
