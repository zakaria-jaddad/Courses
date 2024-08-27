#include <cs50.h>
#include <stdio.h>
long number(long n);
int main(void)
{
    long n = 0;
    while (n < 1)
    {
        // here is askin for number it's loop
        // promping for input
        n = get_long("Number: \n");
    }
    // visa
    if (number(n) % 10 == 0 && n >= 4000000000000 && n <= 4999999999999999)
    {
        printf("VISA\n");
    }
    // MASTERCARD
    else if (number(n) % 10 == 0 && n > 5099999999999999 && n < 5600000000000000)
    {
        printf(" MASTERCARD\n");
    }
    // American Express
    else if ((number(n) % 10) - 6 == 0 && n > 339999999999999 && n < 380000000000000)
    {
        printf("AMEX\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

long number(long n)
{
    // to get the first number
    long a = ((n % 10));
    long b = ((n % 100) / 10) * 2;
    long c = ((n % 1000) / 100);
    long d = ((n % 10000) / 1000) * 2;
    long e = ((n % 100000) / 10000);
    long f = ((n % 1000000) / 100000) * 2;
    long g = ((n % 10000000) / 1000000);
    long h = ((n % 100000000) / 10000000) * 2;
    long i = ((n % 1000000000) / 100000000);
    long j = ((n % 10000000000) / 1000000000) * 2;
    long k = ((n % 100000000000) / 10000000000);
    long l = ((n % 1000000000000) / 100000000000) * 2;
    long m = ((n % 10000000000000) / 1000000000000);
    long r = ((n % 100000000000000) / 10000000000000) * 2;
    long o = ((n % 1000000000000000) / 100000000000000);
    long p = ((n % 10000000000000000) / 1000000000000000) * 2;

    // sepering the two digits B

    if (b > 8)
    {
        long z = b % 10;
        long y = (b % 100) / 10;
        b = z + y;
    }
    else
    {
        b = ((n % 100) / 10) * 2;
    }
    // sepering the two digits D

    if (d > 8)
    {
        long z1 = d % 10;
        long y1 = (d % 100) / 10;
        d = z1 + y1;
    }
    else
    {
        d = ((n % 10000) / 1000) * 2;
    }
    // sepering the two digits F
    if (f > 8)
    {
        long z2 = f % 10;
        long y2 = (f % 100) / 10;
        f = z2 + y2;
    }
    else
    {
        f = ((n % 1000000) / 100000) * 2;
    }
    // seperating the tow digits of H
    if (h > 8)
    {
        long z3 = h % 10;
        long y3 = (h % 100) / 10;
        h = z3 + y3;
    }
    else
    {
        h = ((n % 100000000) / 10000000) * 2;
    }
    // sepearting J
    if (j > 8)
    {
        long z4 = j % 10;
        long y4 = (j % 100) / 10;
        j = z4 + y4;
    }
    else
    {
        j = ((n % 10000000000) / 1000000000) * 2;
    }
    // seperitaing L
    if (l > 8)
    {
        long z5 = l % 10;
        long y5 = (l % 100) / 10;
        l = z5 + y5;
    }
    else
    {
        l = ((n % 1000000000000) / 100000000000) * 2;
    }
    // seperating N
    if (r > 8)
    {
        long z6 = r % 10;
        long y6 = (r % 100) / 10;
        r = z6 = y6;
    }
    else
    {
        r = ((n % 100000000000000) / 10000000000000) * 2;
    }
    if (p > 8)
    {
        long z7 = p % 10;
        long y7 = (p % 100) / 10;
        p = z7 + y7;
    }
    else
    {
        p = ((n % 10000000000000000) / 1000000000000000) * 2;
    }
    return a + b + c + d + e + f + g + h + i + j + k + l + m + r + o + p;
}