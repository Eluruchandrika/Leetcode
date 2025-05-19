class Solution(object):
    def largestAltitude(self, gain):
        altitudes=[0]
        for i in range(len(gain)):
            curr=gain[i]+altitudes[-1]
            altitudes.append(curr)
        return max(altitudes)

        