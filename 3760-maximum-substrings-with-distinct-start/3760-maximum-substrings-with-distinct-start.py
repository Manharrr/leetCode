class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        new=[]
        for i in s:
            if i  not in new:
                new.append(i)
        return len(new)
        