class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in order:
            if i in friends:
                new.append(i)

        return(new)
      