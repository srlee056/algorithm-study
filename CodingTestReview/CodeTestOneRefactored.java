/// Used ChatGPT to refactor
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        char[][] input = {
            { 'A', 'B' },
            { 'A', 'C' },
            { 'C', 'D' }
            // ... (다른 문자 배열들)
        };

        Map<Character, List<Character>> allFlavors = createFlavorsMap(input);
        System.out.println(allFlavors);

        List<String> allCombs = findAllCombinations(allFlavors);
        allCombs.sort(Comparator.comparingInt(String::length).thenComparing(String::compareTo));
        
        if (!allCombs.isEmpty()) {
            System.out.println(allCombs.get(0));
        }
    }

    public static Map<Character, List<Character>> createFlavorsMap(char[][] input) {
        Map<Character, List<Character>> allFlavors = new HashMap<>();
        
        for (char[] pair : input) {
            char x = pair[0];
            char y = pair[1];
            
            allFlavors.computeIfAbsent(x, k -> new ArrayList<>()).add(y);
            allFlavors.computeIfAbsent(y, k -> new ArrayList<>()).add(x);
        }
        
        return allFlavors;
    }

    public static List<String> findAllCombinations(Map<Character, List<Character>> allFlavors) {
        List<String> allCombs = new ArrayList<>();
        Set<Character> eaten = new HashSet<>();
        
        for (Character key : allFlavors.keySet()) {
            if (!eaten.contains(key)) {
                backtrack(allFlavors, eaten, new StringBuilder(), key, allCombs);
            }
        }
        
        return allCombs;
    }

    public static void backtrack(Map<Character, List<Character>> allFlavors, Set<Character> eaten,
            StringBuilder currentComb, Character currentKey, List<String> allCombs) {

        currentComb.append(currentKey);
        eaten.add(currentKey);

        if (eaten.size() == allFlavors.size()) {
            allCombs.add(currentComb.toString());
        } else {
            for (Character flavor : allFlavors.get(currentKey)) {
                if (!eaten.contains(flavor)) {
                    backtrack(allFlavors, eaten, currentComb, flavor, allCombs);
                }
            }
        }

        currentComb.deleteCharAt(currentComb.length() - 1);
        eaten.remove(currentKey);
    }
}
