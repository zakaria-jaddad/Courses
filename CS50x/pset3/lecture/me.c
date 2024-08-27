#include <stdio.h>
#include <cs50.h>

void draw(int n);
int main(void)
{
    int height = get_int("height :");
    draw(height);
}
//  so here the last loop will pritn the firs peramid a.k.a the user number will = the number of hashes
//and after it the function will print the other numbers of the peramid which is the n-1 layers
//in conclusion the loop will print the last layer and the function will print the other peramid

void draw(int n)
{
    if (n <= 0)
    {
        return;
    }
    else
    {
    draw( n - 1);

    for (int i = 0; i < n; i++)
    {
        printf("#  #");
    }
    printf("\n");
    }
}