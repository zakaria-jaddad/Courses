#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    // declaring the 
    char *s = get_string("s  :");
    char *t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }
    strcpy(t, s);
    if (strlen(s) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("%s\n", s);
    printf("%s\n", t);

    free(t);
    return 0;

}