#include <stdio.h>
#include <cs50.h>



int main(void)
{
    // i'm just testing the consept of data struvture
    typedef struct
    {
        string aicha;
        struct
        {
            int age;
            int hight;
            string me;
        }
        zakaria;
    }
    familly;


familly raja;


    // initialaizing the variables
    raja.aicha = get_string("is aicha happp");
    raja.zakaria.me = get_string("is zakaria happy");
    printf("%s   %s", raja.aicha, raja.zakaria.me);
}