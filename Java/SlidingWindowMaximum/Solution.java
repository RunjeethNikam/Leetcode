import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;


class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        Map<Integer, Integer> freq = new HashMap<>();
        int[] result = new int[nums.length - k + 1];

        for (int i = 0; i < k; i++) {;
            maxHeap.add(nums[i]);
            freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);
        }

        result[0] = maxHeap.peek();
        int index = 1;
        for (int i = k; i < nums.length; i++) {
            maxHeap.add(nums[i]);
            freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);

            int outElement = nums[i-k];
            freq.put(outElement, freq.get(outElement) - 1);

            while (freq.getOrDefault(maxHeap.peek(), 0) == 0) {
                maxHeap.poll();
            }
            result[index++] = maxHeap.peek();
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] result = solution.maxSlidingWindow(new int[] { 1, 3, 1, 2, 0, 5 }, 3);
        System.out.println(Arrays.toString(result));
    }
}