class Solution(object):
    def matrixReshape(self, mat, r, c):
        list1=[]
        result=[]
        for i in mat:
            for j in i:
                list1.append(j)
        if len(list1) != r * c:
            return mat

        for i in range(r): 
            x=[]          
            for j in range(c):
                y=list1.pop(0)
                x.append(y)
            result.append(x)
        return result
                    