#include <stdio.h>
#include <string.h>
void main()
{
    char a[20];
    int len, i, j, flag=0;
    printf("Enter the string");
    gets(a);
    len=strlen(a);
    len=len-1;
    for(i=0; i<=len/2; i++)
    {
        if(a[i]!=a[len-i])
        {
            flag=1;
        }
    }
    if(flag==1)
    {
        printf("The string is not a palindrome");
    }
    else
    {
        printf("The string is paliandrome");
    }
} 
