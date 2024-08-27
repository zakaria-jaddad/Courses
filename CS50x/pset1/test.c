#include <stdio.h>
#include <cs50.h>
long number(long n);
int main(void)
{
    long n;
    {
        n = get_long("number :\n");
        // printf something
        if (number(n) % 10 == 0)
        {
            printf("nice code \n");
        }
        else
        {
            printf("INVALIDE\n");
        }
    }
}
long number(long n)
{
    // to get the first number
    long a = n % 10;
    // to get the second number
    long b = (( n % 100 ) / 10) * 2;
    // to get the therd number
    long c = ( n % 1000 ) / 100;
    //to get the fourth number
    long d = (( n % 10000 ) / 1000) * 2;
    // after geting the numbers time for the algorith
    if (b * 2 > 9)
    {
        // sepering the two digits
        long z = b % 10;
        long y = (b % 100) / 10;
         b = z + y;
    }
    else
    {
       b = (( n % 100 ) / 10) * 2;
    }
    if (d * 2 > 9)
    {
        long z1 = d % 10;
        long y1 = (d % 100) / 10;
        d = z1 + y1;
    }
    else
    {
       d = (( n % 10000 ) / 1000) * 2;
    }
    return a + b + c + d;
}
