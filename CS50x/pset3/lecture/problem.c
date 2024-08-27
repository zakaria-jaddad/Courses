#include <stdio.h>
#include <cs50.h>
void droow(int n);

int main(void)
{
    int times = get_int("how muvh ? \n");
    droow(times);
}


void droow(int n)
{
    for (int i = 0; i < n ; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
// this is making sence even if it's ovoius put at firs i didm't get it because the loop is repeating it selfes over and over
// and every times it do repeat it will start from zero again