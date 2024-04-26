def counting_Sort(a:list):
    min_a = min(a)
    max_a = max(a)
    temp = [0] * (max_a - min_a + 1)
    for i in range(len(a)):
        temp[a[i] - min_a]+=1
    
    for i in range(len(temp)):
        cnt = temp[i]
        while cnt != 0:
            print(i+min_a,end=' ')
            cnt-=1


''' 
    没必要生成0 ~ 100长度的数组，，太浪费内存了
    可以生成   99 - 90 + 1 个桶  枚举各个元素减去最小值90，
    放入对应的桶中，排序完加上90就行。
'''
a = [90,99,98,97,96,95,93,94,91,90]
counting_Sort(a)