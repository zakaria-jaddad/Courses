#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char *s = get_string("s  :");
    char *t = malloc(strlen(s) + 1);

    printf("%s\n", s);
    printf("%p\n", t);
    free(t);

}