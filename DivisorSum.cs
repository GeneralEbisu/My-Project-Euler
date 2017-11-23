using System;
using System.Collections.Generic;

class DivisorSums{
	static void Main(){
		
		var x = DivisorSums.Factorial(4);
		var y = DivisorSums.pow(10,6);
		
		Console.WriteLine(DivisorSums.D(x,y));
	}
	//=============================================================
	
	//Calculating D(m,n)
	public static int D(int m, int n){
		int S = 0;
		foreach(var d in DivisorSums.ListDivisor(m)){
			for(int k=1;k<=n;k++){
				S = S + DivisorSums.sigma(k*d);
			}
		}
		return S;
	}
	
	public static int sigma(int n){
		// Returns the number of divisors of n.
		int s = 0;
		for(int i=1;i<=n;i++){
			if(DivisorSums.isDivide(i,n)){
				s = s+1;
			}
		}
		return s;
	}
	
	public static List<int> ListDivisor(int x){
		List<int> L = new List<int>(); //Create an Empty list of int
		for(int i=1;i<=x;i++){
			if(DivisorSums.isDivide(i,x)){
				L.Add(i);
			}
		}
		return L;
	}
	
	public static bool isDivide(int divisor, int dividend){
		if(dividend%divisor==0){
			return true;
		}else{
			return false;
		}
	}
	
	public static int Factorial(int n){
		if (n >= 2) return n * Factorial(n - 1);
		return 1;
	}
	
	public static int pow(int b, int n){
		//Return b^n <=> b*b*...*b, n times
		int mul = 1;
		for(int i=1;i<=n;i++){
			mul = mul*b;
		}
		return mul;
	}
}





