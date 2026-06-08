class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tail = new int[nums.length];
        int size = 0;
        for (int x : nums) {
            int l = 0, r = size;
            while (l < r) {
                int m = (l + r) / 2;
                if (tail[m] < x) l = m + 1;
                else r = m;
            }
            tail[l] = x;
            if (l == size) size++;
        }
        return size;
    }
}