#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
// here the memory is called heap why because the aray hasn't any value at it
int main(void)
{
    int *car = malloc(25 * sizeof(int));
    for (int i = 0; i < 25; i++)
    {
        printf("%p\n", (car + i));
    }
    free(car);
}