// Q. Find factorial of a number using for loop
package javacode;

public class factorial {
    public static void main(String[] args){
        long number =25;
        long fact=1;
        for(int i=1;i<=number;i++){
            fact*=i;
        }
        System.out.println("fact "+fact);
    }
}