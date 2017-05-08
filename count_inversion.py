from merge_sort import merge_sort
def count(array):
    n = len(array)
    if n == 1:
        return 0
    else:
        mid = (n-1)//2
        x = count(array[mid+1:])
        y = count(array[:mid+1])
        init = merge_sort()
        b = init.main(array[mid+1:])
        c = init.main(array[:mid+1])
        z = countSplitInv(c,b)
        return x+y+z
def countSplitInv(L1, L2):
#    import ipdb; ipdb.set_trace()
    i = 0
    j = 0
    C = []
    inv = 0
    for l in range(len(L1)+len(L2)):
        C.append(0)
    for k in range(len(L1)+len(L2)):
        if j > (len(L2)-1):
            C[k] = L1[i]
            i+=1
        elif i > (len(L1)-1):
            C[k] = L2[j]
            j+=1
        elif L1[i]<L2[j]:
            C[k] = L1[i]
            i+=1
        else:
            C[k] = L2[j]
            inv += len(L1)-i
            j +=1
    return (inv)
