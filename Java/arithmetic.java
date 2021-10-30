import java.util.Scanner;	
class arithmetic
{
	public static void main(String amal[])
	{
		Scanner input=new Scanner(System.in);	
		
		System.out.println("Enter a Number: ");
		int x=input.nextInt();

		System.out.println("Enter a Number: ");
		int y=input.nextInt();

		System.out.println("\n");

		sum obj1=new sum(x,y);
		diff obj2=new diff(x,y);
		product obj3=new product(x,y);
		divide obj4=new divide(x,y);
	}	
}

class sum
{	sum(int a,int b)
	{
		System.out.println("The Sum is : "+(a+b));
	
	}		
}
class diff
{
	diff(int a,int b)
	{
		System.out.println("The Diffrence is : "+(a-b));
	
	}		
}

class product
{
	product(int a,int b)
	{
		System.out.println("The product is : "+(a*b));
	
	}		
}
class divide
{
	divide(int a,int b)
	{
		System.out.println("The Quotient is : "+(a/b));
	
	}		
}
