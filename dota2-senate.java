import java.util.ArrayDeque;


class Solution {
    public String predictPartyVictory(String senate) {
        ArrayDeque<Integer> r = new ArrayDeque<>(), d = new ArrayDeque<>();
        int index = 0;
        for (; index < senate.length(); index++) {
            char value = senate.charAt(index);
            if (value == 'R'){
                r.add(index);
            } else {
                d.add(index);
            }
        }

        while (!r.isEmpty() && !d.isEmpty()) {
            if (r.peek() < d.peek()) {
                r.add(index++);
            } else {
                d.add(index++);
            }
            r.removeFirst();
            d.removeFirst();
        }

        if (r.isEmpty()) {
            return "Dire";
        } else {
            return "Radiant";
        }
    }

    // public static void main(String[] args) {
    //     Solution s = new Solution();
    //     System.out.println(s.predictPartyVictory("DRR"));
    // }
}