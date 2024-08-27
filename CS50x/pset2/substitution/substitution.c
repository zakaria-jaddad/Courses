#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(int argc, string argv[])
{
    string s = argv[1];
    int n = strlen(s);
// here the start of the conditions
    if (argc == 2 && n == 26)
    {
        if (isalpha(s[0]) && isalpha(s[1]) && isalpha(s[2]) && isalpha(s[3]) && isalpha(s[4]) && isalpha(s[5]) && isalpha(s[6]) && isalpha(s[7]) && isalpha(s[8]) && isalpha(s[9]) && isalpha(s[10]) && isalpha(s[11]) && isalpha(s[12]) && isalpha(s[13]) && isalpha(s[14]) && isalpha(s[15]) && isalpha(s[16]) && isalpha(s[17]) && isalpha(s[18]) && isalpha(s[19]) && isalpha(s[20]) && isalpha(s[21]) && isalpha(s[22]) && isalpha(s[23]) && isalpha(s[24]) && isalpha(s[25]))
        {
                        if (5 > 0)
            {
                // no clue how to put this condition ?
                // how can i do it ?
                string word = get_string("plaintext:  ");
                string w = word;
                int number = strlen(w);
                int low[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
                int up[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
                printf("ciphertext: ");
                for (int i = 0; i < number; i++)
                {
                    if (isalpha(w[i]) != 0)
                    {
                        if (isupper(w[i]) != 0)
                        {
                            //lower and upper key
                                for (int k = 0; k < 26;k++)
                                {     //key  == word
                                    if (s[k] == up[c])
                                    {
                                        if (islower(s[k]) != 0)
                                        {
                                            printf("%c", s[c] - 32);
                                        }
                                        else
                                        {
                                            printf("%c", s[c]);
                                        }
                                    }

                                }
                        }
                        else // lower case
                        {
                            if (isupper(s[i]) != 0)
                            //upper and lower key
                            {
                                printf("%c", s[i] + 32);
                            }
                            else
                            {
                                printf("%c", s[i]);
                            }
                        }
                    }
                    else
                    {
                        printf("%c", w[i]);
                    }

                }
                printf("\n");
            }
            else
            {
                printf("key must not contain repeated charcters.\n");
                return 1;
            }
        }
        else
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }
    }
    else if (argc == 2)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
} // this is ain't meant to bee sorry dude i coudn't do it :(