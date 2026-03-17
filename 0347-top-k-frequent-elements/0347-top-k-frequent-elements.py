class Solution(object):
   def topKFrequent(self,nums, k):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    result = []
    for i in range(k):
        result.append(sorted_items[i][0])
    return result


        