#include<stdio.h>
void sort();
struct employee{
    char name[30];
    int age;
    float bs;
    float exp;
}e[20];
void main()
{
    int i, x;
    printf("Enter number of employees");
    scanf("%d",&x);
    for(i=0;i<x;i++)
    {
        printf("Enter the name:");
        scanf("%s",e[i].name);
        printf("Enter Age:");
        scanf("%d",&e[i].age);
        printf("Enter Basic salary:");
        scanf("%f",&e[i].bs);
        printf("Enter Experiance");
        scanf("%f",&e[i].exp);
    }
    sort(e,20);
    printf("Name\t Age\t Basic salary\t Experiance\t\n");
    for(i=0;i<x;i++)
    {
        printf("%s\t%d\t%f\t%f\n",e[i].name,e[i].age,e[i].bs,e[i].exp);
    }
}
void sort(struct employee e[],int n)
{
    int i,j;
    struct employee t;
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-1;j++)
        {
            if(e[j].exp<e[j+1].exp)
            {
                t = e[j];
                e[j]=e[j+1];
                e[j+1]=t;
            }
        }
    }
}
