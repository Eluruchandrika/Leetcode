class Solution:
    def frequencySort(self, s: str) -> str:
        dic=dict()
        for i in s:
            dic[i]=dic.get(i,0)+1
        sorted_dict = sorted(dic.items(), key=lambda item:item[1], reverse=True)
        dic=dict(sorted_dict)
        res=""
        for i, j in dic.items():
            res+=i*j
        return res

        