#include <cs50.h>
#include <stdio.h>
void drow(int height);
int main(void)
{
    int n = get_int("Height :");
    drow(n);
}


void drow(int height)
{
    if ( height >= 0)
    {
    drow(height - 2);
    }
    else
    {
        return;
    }
    for (int i = 0; i < height ; i++)
    {
        printf("#");
    }
    printf("\n");

}