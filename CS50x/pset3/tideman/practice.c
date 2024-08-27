#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int l[3];
    int m[3] = {0, 1, 2};
    int w[3] = {1, 2, 3};
    int some[3];
    for (int i = 0; i < 3; i++)
    {
        l[i] = m[i] + w[i];
        some[i] = l[i] + 1;
        printf("%i\n", some[i]);
    }
}