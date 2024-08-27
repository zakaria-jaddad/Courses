#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
int count_letters(string name);
int count_words(string name);
int count_sentences(string name);
int main(void)

{
    string s = get_string("Text: ");
    // the average number of letters per 100 words
    // the average number of sentences per 100 words
    float non = count_words(s) * 1.0000;
    float letters = (count_letters(s) / non) * 100;
    float sentences = (count_sentences(s)  / non) * 100;

    // the index
    float index = 0.0588 * letters - 0.296 * sentences - 15.8;
    int x = round(index);
    if (x <= 0)
    {
        printf("Before Grade 1\n");
    }
    else if (x == 1)
    {
        printf("Grade 1\n");
    }
    else if (x == 2)
    {
        printf("Grade 2\n");
    }
    else if (x == 3)
    {
        printf("Grade 3\n");
    }
    else if (x == 4)
    {
        printf("Grade 4\n");
    }
    else if (x == 5)
    {
        printf("Grade 5\n");
    }
    else if (x == 6)
    {
        printf("Grade 6\n");
    }
    else if (x == 7)
    {
        printf("Grade 7\n");
    }
    else if (x == 8)
    {
        printf("Grade 8\n");
    }
    else if (x == 9)
    {
        printf("Grade 9\n");
    }
    else if (x == 10)
    {
        printf("Grade 10\n");
    }
    else if (x == 11)
    {
        printf("Grade 11\n");
    }
    else if (x == 12)
    {
        printf("Grade 12\n");
    }
    else if (x == 13)
    {
        printf("Grade 13\n");
    }
    else if (x == 14)
    {
        printf("Grade 14\n");
    }
    else if (x == 15)
    {
        printf("Grade 15\n");
    }
    else
    {
        printf("Grade 16+\n");
    }
}



// to count letters

int count_letters(string name)
{
    int n = strlen(name);
    string k = name;
    int f = 0;
    for (int i = 0, l = 0; i < n ; i++)
    {
        if (isalpha(k[i]))
        {
            l = 1;
        }
        else
        {
            l = 0;
        }
        f += l;
    }
    return f;
}
// to coumt words

int count_words(string name)
{
    int n = strlen(name);
    string k = name;
    int f = 0;
    for (int i = 0, l = 0 ; i < n ; i++)
    {
        if (k[i] == ' ')
        {
            l = 1;
        }
        else
        {
            l = 0;
        }
        f += l;
    }
    return f + 1;
}
// to count sentecences

int count_sentences(string name)
{
    int n = strlen(name);
    string k = name;
    int f = 0;
    for (int i = 0, l = 0; i < n ; i++)
    {
        if (k[i] == '!' || k[i] == '?' || k[i] == '.')
        {
            l = 1;
        }
        else
        {
            l = 0;
        }
        f += l;
    }
    return f;
}