class Solution(object):
    def totalFruit(self, fruits):
        l = ans = 0
        cnt = {}
        for r, f in enumerate(fruits):
            cnt[f] = cnt.get(f, 0) + 1
            while len(cnt) > 2:
                cnt[fruits[l]] -= 1
                if cnt[fruits[l]] == 0:
                    del cnt[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans