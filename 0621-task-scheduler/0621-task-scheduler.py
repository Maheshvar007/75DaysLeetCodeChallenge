class Solution(object):
    def leastInterval(self, tasks, n):
        c = [tasks.count(x) for x in set(tasks)]
        return max(len(tasks), (max(c)-1)*(n+1)+c.count(max(c)))