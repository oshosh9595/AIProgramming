package test.java;
import java.util.Scanner;

public class silver4 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[] coin = new int[n];
		
		int conut = 0;
		for(int i = 0; i < n; i++) {
			coin[i] = sc.nextInt();
		}
		
		for(int i = n-1; i > n; i--) {
			if(k / coin[i] >= 0) {
				conut += k/coin[i];
			}
			
			k -= (k/coin[i]) * coin[i];
		}
		
		System.out.println(conut);
	}
}
