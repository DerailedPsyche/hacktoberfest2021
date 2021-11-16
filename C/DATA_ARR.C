/* data structures program(array) 14/1/20
1)Creation of an array and displaying it
2)Deletion of an element from the array
3)Insertion of an element into the array
4)linear searching from the array */
#include<stdio.h>
#include<conio.h>
void main()
{
  int  a[10],k,n,b,c,i,e,j,y;
  int f[10],p;
  int ins,ele=0;
  int del;
  clrscr();
  printf("Please enter the array size:\n");
  scanf("%d",&n);
  for(i=0;i<n;i++)
   {
    printf("Enter the element for location %d: ",i+1);
    scanf("%d",&a[i]);
   }
y:
 printf("Program Menu:\n"
	"1:Searching\n"
	"2:Insertion\n"
	"3:Deletion\n"
	"4:Display\n"
	"5:Reverse\n");
 scanf("%d",&b);

 switch(b)
  {
    case 1:
	   printf("Please enter the element you want to search:\n");
	   scanf("%d",&c);
	   for(i=0;i<n;i++)
	     {
	       if(a[i]==c)
		{
		  printf("The element is found at location %d",i+1);
		  e=1;

		}
	     }
	       if(e!=1)
		{
		 printf("Element not found");
		}
	     break;
  case 2:
       printf("Please enter the location where you want to insert the element: \n");
       scanf("%d",&ins);
       printf("Please enter the element:\n");
       scanf("%d",&ele);
       for(i=n;i>=ins;i--)
	{
	 a[i+1]=a[i];
	}
	a[ins]=ele;
	for(i=0;i<n+1;i++)
	 {
	  printf("%d is the element\n",a[i]);
	 }
	 break;
  case 3:
      printf("Please enter the position  you want to delete:\n");
      scanf("%d",&del);
      for(i=del;i<=n-1;i++)
       {
	 a[i]=a[i+1];
       }
       for(i=0;i<n-1;i++)
	{
	 printf("this is the element %d:\n",a[i]);
	}
	break;


  case 4:
       for(i=0;i<n;i++)
	{
	 printf("%d is the element at location %d at memory adress %d \n",a[i],(i+1),&a[i]);
	}
	break;
  case 5:
     for(i=n-1,p=0;i>=0,p<n;i--,p++)
      {
	f[p]=a[i];
      }
     for(i=0;i<n;i++)
      printf("%d is the element\n",f[i]);
      break;
 }
 printf("\nDo you wish to continue press 1 to continue and 2 to exit: ");
 scanf("%d",&j);
 if(j==1)
  {
   goto y;
  }
 else
  {
   printf("Thankyou");
  }
 getch();
}






