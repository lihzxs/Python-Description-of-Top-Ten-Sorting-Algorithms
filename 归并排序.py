def merge(a:list,start:int,mid:int,end:int):   #合并元素的函数
    temp = []     #临时列表

    l = start
    r = mid + 1

    while l <= mid and r <= end:
        if a[l] <= a[r]:
            temp.append(a[l])
            l+=1
        else:
            temp.append(a[r])
            r+=1
    while l <= mid:
        temp.append(a[l])
        l += 1
    while r <= end:
        temp.append(a[r])
        r += 1
    
    #再将临时列表中的元素拷贝回a列表
    #将临时列表中的元素拷贝回a列表
    a[start:end+1] = temp
    print(a)

def merge_Sort(a:list,start:int,end:int):
    if start == end:
        return
    
    mid = (start + end) // 2
    merge_Sort(a,start,mid)   #先对左区间进行归并排序
    merge_Sort(a,mid+1,end)   
    merge(a,start,mid,end)


a = [100,1,3,0,56,34,22]

merge_Sort(a,0,len(a)-1)