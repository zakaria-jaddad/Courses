#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>
#include <string.h>

char ** fizzBuzz(int n);


int main(void)
{
    int n = get_int("how many you want");
    char *c = *fizzBuzz(n);
    printf("%s\n", c);
}


char ** fizzBuzz(int n)
{
    char **answer;
    char s[1240];
    answer = malloc(n * sizeof(char*));
    int i, j;
    for (i = 0, j = 1; i < n; i++, j++){
        answer[i] = malloc(strlen("FizzBuzz"));
        if (j % 3 == 0 && j % 5 == 0)
            sprintf(answer[i], "%s", "FizzBuzz");
        else if (j % 3 == 0)
            sprintf(answer[i], "%s", "Fizz");
        else if (j % 5 == 0)
            sprintf(answer[i], "%s", "buzz");
        else
            sprintf(s, "%d", j), strcpy(answer[i], s);
    }
    return answer;
}