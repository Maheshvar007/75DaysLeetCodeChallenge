import java.util.*;
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int n = intervals.length;
        int[][] arr = new int[n + 1][2];
        for (int i = 0; i < n; i++) {
            arr[i] = intervals[i];
        }
        arr[n] = newInterval;
        Arrays.sort(arr, (a, b) -> a[0] - b[0]);
        List<int[]> result = new ArrayList<>();
        for (int[] curr : arr) {
            if (result.isEmpty() ||
                result.get(result.size() - 1)[1] < curr[0]) {
                result.add(curr);
            } else {
                result.get(result.size() - 1)[1] =
                    Math.max(result.get(result.size() - 1)[1], curr[1]);
            }
        }
        return result.toArray(new int[result.size()][]);
    }
}