#include<stdio.h>
void main()
{
    int a,b;
    char op;
    printf("enter the numbers:");
    scanf("%d %d",&a, &b);
    printf("enter choice(+,-,*,/,%):");
    scanf("%s",&op);
    switch(op)
    {
        case '+':printf("result%d",a+b);
        break;
        case '-':printf("result=%d",a-b);
        break;
        case '*':printf("result=%d",a*b);
        break;
        case '/':printf("reult=%f",a/b);
        break;
        case '%':printf("result=%f",a%b);
        break;
        default:printf("invalid");

    }

}