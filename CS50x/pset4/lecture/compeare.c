#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string s = get_string("s  :");
    string t = get_string("t  :");

    if ( *s == *t)
    {
        printf("same\n");
        printf("%p  %p\n", s, t);
        printf("%c  %c\n", *s, *t);
        printf("%p  %p\n", &s, &t);
        printf("%i  %i\n", &s, &t);


    }
    else
    {
        printf("different\n");
    }
}