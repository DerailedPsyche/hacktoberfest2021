#include<stdio.h>
main()
{
    int i,j,n,temp;
    printf("Enter number of elements");
    scanf("%d",&n);
    int a[n];
    for(i=0; i<n; i++)
    {
        printf("Enter number\t");
        scanf("%d",&a[i]);
    }
    printf("\n Entered numbers\n");
    for(i=0; i<n; i++)
    {
        printf("%d\t", a[i]);
    }
    for(i=0; i<n-1; i++)
    {
        for(j=0; j<n-1; j++)
        {
            if(a[j]<a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;

            }
        }
    }
    printf("\nAfter sorting\n");
    for(i=0; i<n; i++)
    {
        printf("%d\t",a[i]);
    }
}
