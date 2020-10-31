#include<stdio.h> 
#include<stdlib.h>
#include<string.h>
int main() 
{ 
 int n, i,nd,d,sum=0,temp; 
 char str[100];
 printf("Enter a number: \n"); 
 scanf("%d", &n); 
 sprintf(str,"%d",n);
        nd=strlen(str);
        temp=n;
        while(temp!=0)
        {
        d=temp%10;
        sum=sum+pow(d,nd);
        temp=temp/10;
        }
 if ( n==sum) 
  printf("%d is an Armstrong number\n", n); 
 else 
  printf("%d is not a Armstrong number\n", n); 
} 