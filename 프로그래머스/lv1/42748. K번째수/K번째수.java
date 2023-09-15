import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int commandNum = commands.length;
        
        int[] answer = new int[commandNum];
        
        for(int i = 0; i<commandNum; i++){
            int[] slicedArr = sliceIt(array, commands[i][0],commands[i][1] );
            
            Arrays.sort(slicedArr);
            System.out.println(Arrays.toString(slicedArr));
            System.out.println(slicedArr[commands[i][2]-1]);
            answer[i] = slicedArr[commands[i][2]-1];
        }
        
        
        return answer;
    }
    
    public int[] sliceIt(int[] array, int startIdx, int endIdx){
        int[] result = new int[endIdx-startIdx+1];
        
        for (int i = 0; i<endIdx-startIdx+1; i++){
            result[i] = array[i+startIdx-1];
        }
        return result;
        
    }
}