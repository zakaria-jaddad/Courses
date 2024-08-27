// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    //  LENGHT == 45 you need to remember this
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 676;

// Hash table
node *table[N];

// tracing the size of dictionary
int tracker = 0;
// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // you will use hash here to get the world
    int i = hash(word);
    // checking
    for (node *n = table[i]; n != NULL; n = n -> next)
    {
        if (strcasecmp(n -> word, word) == 0)
        {
            return true;
        }
    }
    return false;
    // you will use strcasecmp to compeare tow strings
}

// Hashes word to a number problem here need to bi fixed
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int summe = toupper(word[1]) * (toupper(word[1]) + 3);
    return summe % 26;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    int i;
    FILE *f = fopen(dictionary, "r");
    char word[LENGTH + 1];
    // strting the loop
    while (fscanf(f, "%s", word) != EOF)
    {
        // allocating new node
        node *n = calloc(1, sizeof(node));
        // checking if null
        if (n == NULL)
        {
            return false;
        }

        // copying string amd hashing it

        strcpy(n -> word, word);
        i = hash(n -> word);

        // checking

        if (table[i] == NULL)
        {
            // set table to point at n
            table[i] = n;
        }
        // if list isn't empty
        else
        {
            // set n pointing to the first node in the linked list
            n -> next = table[i];
            // set head linked list to point at n which is the bigginig of LL
            table[i] = n;
            // here
        }
        tracker++;
        // freing n for each loop
    }
    fclose(f);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return tracker;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // freeing programe memory
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *n = table[i] -> next;
            free(table[i]);
            table[i] = n;
        }
    }
    // after freeing all memory the function should return true

    return true;
}

// to use debuger

// debug50 ./speller dictionaries/small texts/cat.txt
// well i had fun wiht you so much it was a great time learning wiht you, i start to kno that if i'm stuck with some thing i should reaserch about it
// for the last time thank you <3