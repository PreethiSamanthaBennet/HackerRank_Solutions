import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        try{
            Scanner sc = new Scanner(System.in);
            int a = sc.nextInt();
            int b = sc.nextInt();

            System.out.println(a/b);
        }
        
        catch(InputMismatchException e){
            System.out.println("java.util.InputMismatchException");
        }
        
        catch(Exception e){
            System.out.println(e);
        }
    }
}
