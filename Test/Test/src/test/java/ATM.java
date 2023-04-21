package test.java;

import java.util.Arrays;
import java.util.Scanner;

public class ATM {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		int[] n = new int[t];
		
		for(int i=0; i < t; i++) {
			n[i] = sc.nextInt();
		}
		
		//정렬
		Arrays.sort(n);
		
		//시간합계
		int conut = 0;
		//누적사람
		int sum = 0;
		
		for(int i=0; i < t; i++) {
			sum += conut + n[i];
			
			conut += n[i];
			
		}
		System.out.println(sum);
	}
	
}
