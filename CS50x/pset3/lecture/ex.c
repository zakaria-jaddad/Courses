#include <cs50.h>
#include <stdio.h>
int times(int n);
int main(void)
{
    int n = get_int("number :");
        printf("%i\n", times(n));
}




int times(int n)
{

    if (n <= 1)
    {
        return false;
    }
    else if (n % 2 == 0)
    {
        return 0 + times(n/2);// n/2 is just the value of the variable in the function like it change every loop˜`
        // inside
      //return 1
    }
    else
    {
        return 0 + times(1 + (n * 3));
    }

}

