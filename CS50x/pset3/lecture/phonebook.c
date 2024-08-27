#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
   string person;
   string number;
}
people;


int main(void)
{
    people ana[2];

    ana[0].person =  "zakaria";
    ana[0].number = "0684727595";
    ana[1].person = "aicha";
    ana[1].number = "0650333431";

    for (int i = 0; i < 2 ; i++)
    {
        if (strcmp(ana[i].person, "zakaria") == 0)
        {
            printf("this is :%s\n", ana[i].number);
            return 0;
        }
    }
    printf("sorry the number isn't here :(\n");
    return 1;

}