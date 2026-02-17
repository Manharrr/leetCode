class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sett=set()
        for i in nums:
            if i in sett:
                return True
               
            sett.add(i)
        return False
        
           
        