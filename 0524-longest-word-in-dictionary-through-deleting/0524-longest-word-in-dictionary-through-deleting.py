class Solution(object):
    def findLongestWord(self, s, dictionary):
        maxx = 0
        word = ""
        for i in dictionary:
            s_iter = 0
            i_iter = 0
            while i_iter < len(i) and s_iter < len(s):
                if s[s_iter] == i[i_iter]:
                    i_iter += 1
                s_iter += 1

            if i_iter == len(i):
                if i_iter > maxx or (i_iter == maxx and i < word):
                    maxx = i_iter 
                    word = i
        return word





        