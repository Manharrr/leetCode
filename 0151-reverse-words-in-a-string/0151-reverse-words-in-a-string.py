class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        clean= " ".join(s.split())
        rev=" ".join(clean.split()[::-1])
        return rev
        