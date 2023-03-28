from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        newdict = Counter(nums)
        newdict = newdict.most_common(k)
        mylist = []
        for keys, values in newdict:
            mylist.append(keys)
        return mylist
        