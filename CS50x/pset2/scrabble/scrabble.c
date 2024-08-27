#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0, 0, 0};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
    // TODO: Print the winner
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int n = strlen(word);
    string s = word;
    int l = 0, f = 0;
    for (int i = 0; i < n ; i++)
    {
        for (int k = 65, j = 97, result = 0; k <= 90 && j <= 122; j++, k++, result++)
        {
            if (s[i] == k)
            {
                l = POINTS[result];
            }
            else if (s[i] == j)
            {
                l = POINTS[result];
            }
            else
            {
                l = POINTS[27];
            }
            f += l;
        }

    }
    return f ;
}









    printf("%i\n",count_letters(s));
    printf("%i\n",count_words(s));
    printf("%i\n",count_sentences(s));