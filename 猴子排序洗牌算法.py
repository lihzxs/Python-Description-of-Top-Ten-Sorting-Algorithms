import random 
def swap_List(a):
    len_a = len(a)
    for i in range(len_a - 1,-1,-1):
        swap_index = random.randint(0,i)
        print(f'swap_index = {swap_index}')
        a[swap_index],a[i] = a[i],a[swap_index]
    print(a)

a = [100,1,3,1000,56,34,22,2,1,10]
swap_List(a)