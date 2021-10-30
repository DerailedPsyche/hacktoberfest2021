#include <stdio.h>
int main()
    {
    int r1, r2, c1, c2, a[100][100], b[100][100], sum[100][100], mul[100][100], i, j, k;
    printf("Enter the order of 1st matrix:\n");
    scanf("%d" "%d", &r1, &c1);
    printf("Enter the order of 2nd matrix:\n");
    scanf("%d" "%d", &r2, &c2);
    printf("\nEnter elements of 1st matrix:\n");
    for(i=0;i<r1;++i)
       {
        for(j=0;j<c1;++j)
           {
            scanf("%d", &a[i][j]);
           }
       } 
    printf("Enter elements of 2nd matrix:\n");
    for(i=0;i<r2;++i)
       {
       for(j=0;j<c2;++j)
          {
            scanf("%d", &b[i][j]);
          }
       }
    if(r1==r2 && c1==c2)
      {
      for(i=0;i<r1;++i)
         {
          for(j=0;j<c1;++j)
             {
              sum[i][j] = a[i][j] + b[i][j];
             }
         }
      printf("\nSum of two matrices: \n");
      for(i=0;i<r1;++i)
         {
          for(j=0;j<c1;++j)
             {
              printf("%d\t", sum[i][j]);
              if(j==c1-1)
                {
                 printf("\n\n");
                }
             }
         }
      }
    else
      {
      printf("\nAddition not possible\n");
      }
    if(r2==c1)
      {
       printf("Product of the two matrices:\n");
       for(i=0;i<r1;i++)
          {
          for(j=0;j<c2;j++) 
             {
             mul[i][j]=0;
             for(k=0;k<c1;k++)
                {
                mul[i][j] = mul[i][j]+a[i][k]*b[k][j];
                }
             printf("%d\t",mul[i][j]);
             }
          printf("\n\n");
          }
      }
    else
        {
        printf("\mMultiplication not possible\n");
       } 
    printf("Transpose of 1st matrix:\n");
    for(i=0;i<r1;i++)
       {
       for(j=0;j<c1;j++)
          {
          printf("%d\t",a[j][i]);
          }
       printf("\n\n");
       }
    printf("Transpose of 2nd matrix:\n");
    for(i=0;i<r2;i++)
       {
       for(j=0;j<c2;j++)
          {
          printf("%d\t",b[j][i]);
          }
       printf("\n\n");
       }
    return 0;
}
