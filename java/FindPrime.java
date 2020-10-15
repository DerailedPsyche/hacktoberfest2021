import java.util.Scanner;	
class FindPrime
{
	public static void main(String amal[])
	{
		Scanner Var=new Scanner(System.in);	//system.in for accepting from keyboard
		System.out.println("Enter a Number : ");
		int Var2=Var.nextInt();
		if(checkPrime(Var2))
		{
			System.out.println(Var2+"is a prime number");	
		}
		else
		{
			System.out.println(Var2+"is not a prime number");	
		}
	}
	public static boolean checkPrime(int Var2)
	{
		if(Var2<=1)
		{
			return false;
		}
		for(int i=2;i<Math.sqrt(Var2);i++)
		{
			if(Var2%i==0)
				return false;
		}
		return true;
	}
	

}
