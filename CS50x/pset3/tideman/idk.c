#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count ; i++)
    {
        if (strcmp(name, candidates[i]) == 0)
        {
            ranks[i] = rank + 1;
            printf("%i\n", ranks[i]);
            return true;
        }
    }
    return false;
    // Done :)
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    int pre[MAX][MAX];
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (ranks[i] < ranks[j])
            {
                pre[i][j] = 1;
                preferences[i][j] = preferences[i][j] + pre[i][j];
            }
            else
            {
                pre[i][j] = 0;
                preferences[i][j] = preferences[i][j] + pre[i][j];

            }
        }
    }
    return;
// man i dont know how to make it ?
// it is hard but the problem is in my logic
// but i don't kno how to tell the computer how to do it so tomorrow i nedde more practice
// done after 3 days
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > 0)
            {
                pairs[i].winner = i;
                pairs[i].loser = j;
                pair_count++;


            }
        }
    }
    return;
    // easy done after 300 min :)
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO this one os hard though
    // if preferences[i][j] is the higher
    // than i is the more prferd
    int counter = 0;
    int p = 0;
    for (int i = 0, k = 0; i < candidate_count; i++, k++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > counter)
            {
                counter = preferences[i][j];
            }
        }
    }
    for (int k = 0; k < candidate_count; k++)
    {
        for (int i = 0; i < candidate_count; i++)
        {
            for (int j = 0; j < candidate_count; j++)
            {
                if (preferences[i][j] == counter - k)
                {
                    pairs[p].winner = i;
                    pairs[p].loser = j;
                    p++;
                }
            }
        }
    }
    return;
// i trouly belive that i can do it
// done and i belive it's done
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    int some, some2;
    for (int i = 0, j = 1; i < candidate_count; i++, j++)
    {
        some = pairs[i].winner + pairs[i].loser;
        some2 =pairs[j].winner + pairs[j].loser;
        if (some < some2)
            locked[pairs[i].winner][pairs[i].loser] = true;
        else
            locked[pairs[i].winner][pairs[i].loser] = false;
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    int checking[candidate_count];
    for (int i = 0; i < candidate_count; i++)
    {
        checking[i] = 0;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (pairs[i].winner == pairs[j].loser)
                checking[i]++;
        }
        if (checking[i] == 0)
        {
            printf("%s\n", candidates[pairs[i].winner]);
            return;
        }
    }
    return;
}
                if (c[i] == 0)
                {
                    if (pairs[i].winner == i)
                        locked[pairs[i].winner][pairs[i].loser] = true;
                    else if (pairs[i].loser == i)
                        locked[pairs[i].winner][pairs[i].loser] = false;
                }
                else
                    locked[pairs[i].winner][pairs[i].loser] = true;






n