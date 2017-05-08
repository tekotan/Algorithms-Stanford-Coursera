class merge_sort(object):
    def __init__(self):
#        import ipdb; ipdb.set_trace()
        pass
    def merge(self, L1, L2, C):
        i = 0
        j = 0
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
                j +=1
        return (C)
    def main(self, input_list):
        if len(input_list) == 1 or len(input_list) == 0:
            return (input_list)
        mid = (len(input_list)-1)//2
        A = self.main(input_list[:mid+1])
        B = self.main(input_list[mid+1:])
        return (self.merge(A, B, input_list))
