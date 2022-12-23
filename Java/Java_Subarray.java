import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        
        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        
        int negative = 0;

        for(int i = 0; i < n; i++){
            for(int j = i; j <= n; j++){
                int curr= 0;
                
                for(int k = i; k < j; k++){
                    curr += arr[k];
                }
                
                if(curr < 0)
                    negative++;
            }
        }
        
        System.out.println(negative);
    }
}
