'''
    为什么要有随机快速排序？？
    因为快排在数列有序的时候时间复杂度为 O（n*n）
    随机枚举一个基准数可以有效解决
'''
#到入随机数模块
import random
def quickly_Sort(a:list,left:int,right:int):
    if left >= right:
        return 
    s = random.randint(left,right)
    a[left],a[s] = a[s],a[left]
    l = left
    r = right
    temp = a[l]

    while l < r:
        while l < r and a[r] >= temp:
            r-=1
        if l < r:
            a[l] = a[r]
        while l < r and a[l] <= temp:
            l+=1
        if l < r:
            a[r] = a[l]
    
    a[l] = temp
    print(a)
    quickly_Sort(a,left,l)
    quickly_Sort(a,l+1,right)

a = [100,1,3,0,56,34,22]
quickly_Sort(a,0,len(a)-1)