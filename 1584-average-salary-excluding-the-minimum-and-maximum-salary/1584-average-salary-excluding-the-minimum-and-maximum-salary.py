class Solution(object):
    def average(self, salary):
        total=0
        minimum=salary[0]
        maximum=salary[0]

        for i in salary:
            total+=i
            if i<minimum:
                minimum=i
            if i>maximum:
                maximum=i
        total=total-maximum-minimum
        return float(total)/(len(salary)-2)
        