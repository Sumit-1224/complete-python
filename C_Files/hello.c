#include<stdio.h>
int main( )

{
 int a,b,c;
  printf("enter any numbers:");
  //taking input from user 
  scanf("%d%d%d",&a,&b,&c);
  // comparing numbers usin if else
   if(a>b && a>c)
   {
    printf("%d is larget number ",a);
   }
   else if (b>a && b>c)
   {
    printf("%d is larget number ",b);
   }

else 
  printf("%d is largest number ",c);
  return 0;





    }