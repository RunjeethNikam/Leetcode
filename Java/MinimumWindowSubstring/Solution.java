package Practise.Java.MinimumWindowSubstring;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> windowFreq = new HashMap<>();
        Map<Character, Integer> tFreq = new HashMap<>();

        Integer result = Integer.MAX_VALUE;
        String resultStr = "";
        Integer left = null;
        Integer count = 0;

        for (char c : t.toCharArray()) {
            tFreq.put(c, tFreq.getOrDefault(c, 0) + 1);
        }

        for (int index = 0; index < s.length(); index++) {
            char value = s.charAt(index);
            if (tFreq.containsKey(value)) {
                if (left == null) {
                    left = index;
                }
                windowFreq.put(value, windowFreq.getOrDefault(value, 0) + 1);
                if (windowFreq.getOrDefault(value, 0) <= tFreq.getOrDefault(value, 0)) {
                    count++;
                }
                while (windowFreq.getOrDefault(s.charAt(left), 0) > tFreq.getOrDefault(s.charAt(left), 0)) {
                    windowFreq.put(s.charAt(left), windowFreq.getOrDefault(s.charAt(left), 0) - 1);
                    left++;
                    while (left < s.length() && !tFreq.containsKey(s.charAt(left))) {
                        left += 1;
                    }
                }
                if (count == t.length() && (index - left + 1) < result) {
                    result = index - left + 1;
                    resultStr = s.substring(left, index + 1);
                }
            }
        }

        return resultStr;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.minWindow("ADOBECODEBANC", "ABC"));
    }
}