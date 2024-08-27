#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
int only_digits(string name);
int ABCD[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
int abcd[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
int main(int argc, string argv[])
{
    if (argc == 2 && only_digits(argv[1]) != 0 && atoi(argv[1]) > 0)
    {
        int k = atoi(argv[1]);
        string p = get_string("plaintext: ");
        string s2 = p;
        int n2 = strlen(p), c = 0, l2 = 0;
        printf("ciphertext: ");
        for (int i2 = 0; i2 < n2; i2++)
        {
            if (isalpha(s2[i2]) != 0)
            {
                if (isupper(s2[i2]) != 0)
                {
                    // job to do here
                    c = (((s2[i2] - 65) + k) % 26);
                    printf("%c", ABCD[c]);

                }
                else if (islower(s2[i2]) != 0)
                {
                    //don't know how to make this algorithem
                    c = (((s2[i2] - 97) + k) % 26);
                    printf("%c", abcd[c]);

                    // i gusse i did it :)
                    // no i didn't :(
                    // i gusse i did it idk lets see
                }
            }
            else
            {
                printf("%c", s2[i2]);
            }
        }
        printf("\n");
    }

    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}



int only_digits(string name)
{
    int n = strlen(name);
    string s = name;
    int l = 0;
    for (int i = 0; i < n; i++)
    {
        l = isdigit(s[i]);
    }
    return l;
}
