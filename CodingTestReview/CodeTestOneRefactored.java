/// ChatGPT 를 참고하여 리팩토링 진행
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        char[][] input = {
                { 'A', 'B' },
                { 'A', 'C' },
                { 'A', 'D' }
                // ... (다른 문자 배열들)
        };

        // 선호 아이스크림 페어를 통해, 각 맛은 어떤 맛과 페어인지 매핑하고있는 hashmap을 만들었다.
        Map<Character, List<Character>> allFlavors = createFlavorsMap(input);
        System.out.println(allFlavors);

        List<String> allCombs = new ArrayList<>();
        // Set<Character> eaten = new HashSet<>();
        Map<Character, Boolean> eaten = new HashMap<>();
        for (Character k : allFlavors.keySet()) {
            eaten.put(k, false);
        }
        // 재귀적으로 가능한 모든 조합을 찾는 함수
        backtrack(allFlavors, eaten, new StringBuilder(), null, allCombs);
        // 문자열의 길이, 사전순으로 정렬
        allCombs.sort(Comparator.comparingInt(String::length).thenComparing(Comparator.naturalOrder()));
        System.out.println(allCombs.get(0));
    }

    public static Map<Character, List<Character>> createFlavorsMap(char[][] input) {
        Map<Character, List<Character>> allFlavors = new HashMap<>();

        for (char[] pair : input) {
            char x = pair[0];
            char y = pair[1];

            if (!allFlavors.containsKey(x)) {
                allFlavors.computeIfAbsent(x, k -> new ArrayList<Character>(5)).add(x);
            }
            if (!allFlavors.containsKey(y)) {
                allFlavors.computeIfAbsent(y, k -> new ArrayList<Character>(5)).add(y);
            }
            allFlavors.get(x).add(y);
            allFlavors.get(y).add(x);

        }

        return allFlavors;
    }

    public static void backtrack(Map<Character, List<Character>> allFlavors, Map<Character, Boolean> eaten,
            StringBuilder currentComb, Character currentKey, List<String> allCombs) {

        // if all values of eaten if true, then add currentcomb to list and reset all
        // eaten을 map 대신 hashset으로 두고, eaten안에 키가 존재하는지 그리고 eaten의 데이터 길이가 allflavor와
        // 같은지 등으로 사용하는 방법도 있다.

        if (currentKey == null) {
            // choose a random key that is not eaten yet
            for (Map.Entry<Character, List<Character>> entry : allFlavors.entrySet()) {
                if (!eaten.get(entry.getKey())) { // eaten.contains(entry.getKey())
                    backtrack(allFlavors, eaten, currentComb, entry.getKey(), allCombs);
                }
            }
        } else {
            currentComb.append(currentKey);
            if (eaten.get(currentKey)) {
                backtrack(allFlavors, eaten, currentComb, null, allCombs);
            } else {
                eaten.replace(currentKey, true); // eaten.add(currentKey)
                if (!eaten.containsValue(Boolean.FALSE)) { // if anything that has value false, result is false.
                                                           // eaten.size() == allFlavors.size()
                    allCombs.add(currentComb.toString());
                } else {
                    for (Character f : allFlavors.get(currentKey)) {
                        backtrack(allFlavors, eaten, currentComb, f, allCombs);
                    }
                }

                eaten.replace(currentKey, false); // eaten.remove(currentKey)
            }
            currentComb.deleteCharAt(currentComb.length() - 1);

        }
    }

}
