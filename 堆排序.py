#递归版构造大根堆
def create_Max_Heap(a:list,root,len_a):

    #找寻root下标结点的左右孩子
    left = root * 2 + 1
    right = root * 2 + 2
    temp = root

    #找寻左右孩子的最大值
    if left < len_a and a[left] > a[temp]:
        temp = left
    if right < len_a and a[right] > a[temp]:
        temp = right
    
    #存在比它大的孩子结点
    if temp != root:
        a[temp],a[root] = a[root],a[temp]
        #以找到的孩子结点继续构造大根堆
        create_Max_Heap(a,temp,len_a)

#使用循环构造大根堆
def create_Max_Heap_Loop(a:list,root,len_a):
    son  =  root * 2 + 1  #获取左孩子
    while son < len_a:
        if son + 1 < len_a and a[son+1]>a[son]:
            son+=1
        if a[son] > a[root]:
            a[son],a[root] = a[root],a[son]
        else:
            break

        root = son
        son = son * 2 + 1

def heap_Sort(a:list):
    len_a = len(a)
    for i in range(len_a // 2 - 1, -1, -1):
        create_Max_Heap_Loop(a,i,len_a)

    #将最后一个元素与根节点交换，，并从根节点开始重新构造大根堆
    #再执行一次遍历，输出的结果就是降序序列
    for i in range(len_a - 1,0,-1):
        a[0],a[i] = a[i],a[0]
        create_Max_Heap_Loop(a,0,i)

a = [100,1,3,1000,56,34,22,2,1,10]
heap_Sort(a)
print(a)