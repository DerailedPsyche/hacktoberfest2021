#include <stdio.h>
#include <string.h>
void main()
{
    char a[20], b[20];
    int i=0, j;
    printf("Enter the string\n");
    gets(a);
    j=strlen(a)-1;
    for(i; j>=0; i++)
    {
        b[i]=a[j];
        j--;
    }
    b[i]='\0';
    puts(b);
}
