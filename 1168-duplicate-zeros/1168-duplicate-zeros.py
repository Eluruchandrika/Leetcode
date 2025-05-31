class Solution(object):
    def duplicateZeros(self, arr):
        size=len(arr)
        i=0
        while i<size:
            if arr[i]==0:
                arr.insert(i,0)
                arr.pop()
                i+=1
            i+=1
            
        print(arr)

        
        