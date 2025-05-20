class Solution(object):
    def setZeroes(self, matrix):
        rows=set()
        cols=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] ==0:
                    rows.add(i)
                    cols.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows:
                    matrix[i][j]=0
                elif j in cols:
                    matrix[i][j]=0
