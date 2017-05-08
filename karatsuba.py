class multiply(object):
    def divide(self, num1, num2):
        mid1 = (len(str(num1))-1)//2
        A = int(str(num1)[:mid1+1])
        B = int(str(num1)[mid1+1:])
        mid2 = (len(str(num2))-1)//2
        C = int(str(num2)[:mid2+1])
        D = int(str(num2)[mid2+1:])
#        st = str(num2)[mid2+1:]
#        print (st)
#        print (str(num2))
#        print(len(str(num2)) / (mid2+1))
#        print (mid2)
#        D = int(st)
        return ((A, B), (C, D))
    def main(self, num, num2):
        if len(str(num)) == 1 or len(str(num)) == 0:
            return num*num2
        var = self.divide(num, num2)
        AC = self.main(var[0][0], var[1][0])
        BD = self.main(var[0][1], var[1][1])
        ABCD = self.main((var[0][0]+var[0][1]), (var[1][0]+var[1][1]))
        ADBC = ABCD - (BD + AC)
        n = len(str(num))
        ret_val = (10**n)*AC+(10**(n//2))*ADBC + BD
        return ret_val
