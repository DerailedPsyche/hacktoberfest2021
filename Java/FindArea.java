//Finding Area of Circle,Triangle,Reactangle.

import java.util.Scanner;	
class FindArea
{
	public static void main(String amal[])
	{
		Scanner input=new Scanner(System.in);	
		
		System.out.println("Enter radius of the Cirlcle: ");
		float rad=input.nextFloat();

		System.out.println("Enter the base length of the Triangle: ");
		double blength=input.nextDouble();
	
		System.out.println("Enter the height of the triangle: ");
		double height=input.nextDouble();

		System.out.println("Enter the length of the rectangle: ");
		int length=input.nextInt();
		
		System.out.println("Enter the length of the rectangle: ");
		int breadth=input.nextInt();
		
		System.out.println("Area of the Circle: "+Area(rad));
		System.out.println("Area of triangle : "+Area(blength,height));
		System.out.println("Area of the rectangle: "+Area(length,breadth));
	}
	
	public static float Area(float rad)
	{
		float ar=(3.14F*rad*rad);
		return ar;
	}
	
	public static double Area(double blength,double height)
	{
		double ar=(0.5*blength*height);
		return ar;
	}

	public static int Area(int length,int breadth)
	{
		int ar=(length*breadth);
		return ar;
	}
	

}
