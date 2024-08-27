#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s;
    printf("s  :");
    scanf("%s", s);
    malloc(strlen(s) + 1);
    printf("%s\n", s);
    free(strlen(s) + 1);
}