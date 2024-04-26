'''
    希尔排序是插入排序的改版
    因为插入排序在数据有序的情况下时间复杂度近似O（n）
    希尔排序每次选择一个增量，间隔这个增量之间的数据进行排序
    这时候列表中的数据会相对有序，当增量为1时，，就是插入排序了
'''
def shell_Sort(a:list):
    len_a = len(a)
    gap = len_a // 2

    while gap > 0:
        for i in range(gap,len_a):
            index = i
            temp = a[i]
            while index - gap >= 0 and a[index - gap] > temp:
                a[index] = a[index - gap]
                index-=gap
            a[index] = temp
        print(a)
        gap//=2

a = [100,1,3,1000,56,34,22,2,1,10]
shell_Sort(a)