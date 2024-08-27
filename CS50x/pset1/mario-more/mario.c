#include <cs50.h>
#include <stdio.h>
void seventh(int k);
void sixth(int k);
void fifth(int k);
void fourth(int k);
void third(int k);
void sec(int k);
void space(int j);
void first(int k);
int main(void)
{
    int n = 0;
    while (n < 1 || n > 8)
    {
        // first question loop
        n = get_int("hieght : \n");
    }
    if (n == 1)
    {
        // first layer
        first(n);
    }
    else if (n == 2)
    {
        first(n);
        sec(n);
    }
    else if (n == 3)
    {
        first(n);
        sec(n);
        third(n);
    }
    else if (n == 4)
    {
        first(n);
        sec(n);
        third(n);
        fourth(n);
    }
    else if (n == 5)
    {
        first(n);
        sec(n);
        third(n);
        fourth(n);
        fifth(n);
    }
    else if (n == 6)
    {
        first(n);
        sec(n);
        third(n);
        fourth(n);
        fifth(n);
        sixth(n);
    }
    else if (n == 7)
    {
        first(n);
        sec(n);
        third(n);
        fourth(n);
        fifth(n);
        sixth(n);
        seventh(n);
    }
    else
    {
        //last layer
        first(n);
        sec(n);
        third(n);
        fourth(n);
        fifth(n);
        sixth(n);
        seventh(n);
        printf("########  ########\n");
    }
}



void first(int k)
{
    space(k);
    printf("#  #\n");
}
void sec(int k)
{
    space(k - 1);
    printf("##  ##\n");
}
void third(int k)
{
    space(k - 2);
    printf("###  ###\n");
}
void fourth(int k)
{
    space(k - 3);
    printf("####  ####\n");
}
void fifth(int k)
{
    space(k - 4);
    printf("#####  #####\n");
}
void sixth(int k)
{
    space(k - 5);
    printf("######  ######\n");
}
void seventh(int k)
{
    space(k - 6);
    printf("#######  #######\n");
}


void space(int j)
{
    for (int i = 0 ; i < j - 1; i++)
    {
        printf(" ");
        // space loop
    }
}



