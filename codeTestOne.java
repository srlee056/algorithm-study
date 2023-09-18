import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        char[][] input = {
                { 'A', 'B' },
                { 'A', 'C' },
                { 'C', 'D' }
                // ... (다른 문자 배열들)
        };

        // 선호 아이스크림 페어를 통해, 각 맛은 어떤 맛과 페어인지 매핑하고있는 hashmap을 만들었다.
        Map<Character, List<Character>> allFlavors = new HashMap<>();

        for (int i = 0; i < input.length; i++) {
            Character x = Character.valueOf(input[i][0]);
            Character y = Character.valueOf(input[i][1]);

            if (!allFlavors.containsKey(x)) {
                allFlavors.put(x, new ArrayList<Character>(5));
                allFlavors.get(x).add(x);
            }
            allFlavors.get(x).add(y);
            if (!allFlavors.containsKey(y)) {
                allFlavors.put(y, new ArrayList<Character>(4));
                allFlavors.get(y).add(y);
            }

            allFlavors.get(y).add(x);

        }
        System.out.println(allFlavors);

        // 재귀적으로 가능한 모든 조합을 찾는 함수
        Map<Character, Boolean> eaten = new HashMap<>();
        for (Character k : allFlavors.keySet()) {
            eaten.put(k, false);
        }
        StringBuilder comb = new StringBuilder();
        List<String> allCombs = new ArrayList<>();
        backtrack(allFlavors, eaten, comb, null, allCombs);

        Comparator<String> c = new Comparator<String>() {
            public int compare(String s1, String s2) {
                if (Integer.compare(s1.length(), s2.length()) == 0) {
                    return s1.compareTo(s2);
                } else {
                    return Integer.compare(s1.length(), s2.length());
                }

            }
        };
        Collections.sort(allCombs, c);
        System.out.println(allCombs.get(0));
    }

    public static void backtrack(Map<Character, List<Character>> allFlavors, Map<Character, Boolean> eaten,
            StringBuilder currentComb, Character currentKey, List<String> allCombs) {

        // if all values of eaten if true, then add currentcomb to list and reset all

        if (currentKey == null) {
            // choose a random key that is not eaten yet
            for (Map.Entry<Character, List<Character>> entry : allFlavors.entrySet()) {
                entry.getKey();
                entry.getValue();

                if (!eaten.get(entry.getKey())) {
                    // System.out.printf("this is key: %S\n", entry.getKey());
                    // System.out.printf("this is value: %S\n", entry.getValue());
                    backtrack(allFlavors, eaten, currentComb, entry.getKey(), allCombs);
                }
            }
        } else {
            // System.out.printf("before: %s\n", currentComb);
            currentComb.append(currentKey);
            // System.out.printf("after: %s\n", currentComb);
            // System.out.println(currentComb);
            if (eaten.get(currentKey)) {
                backtrack(allFlavors, eaten, currentComb, null, allCombs);
            } else {
                // System.out.println(currentKey);
                eaten.replace(currentKey, true);
                if (!eaten.containsValue(Boolean.FALSE)) { // if anything that has value false, result is false.
                    allCombs.add(currentComb.toString());
                    // System.out.printf("%s added\n", currentComb);
                } else {
                    for (Character f : allFlavors.get(currentKey)) {
                        // System.out.printf("%s add to %s\n", f, currentComb);
                        backtrack(allFlavors, eaten, currentComb, f, allCombs);
                    }
                }

                eaten.replace(currentKey, false);
            }
            currentComb.deleteCharAt(currentComb.length() - 1);

        }
    }

}
