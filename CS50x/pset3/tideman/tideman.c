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
bool check_cycle(int winner, int loser);
bool head(int winner);

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
            ranks[rank] = i;
            return true;
        }
    }
    return false;
    // Done :)
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO
    int pre[MAX][MAX];
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (ranks[i] == j)
            {
                for (int k = 0; k < candidate_count; k++)
                {
                    if (i == k)
                    {
                        pre[i][k] = 0;
                        preferences[ranks[i]][ranks[k]] += pre[i][k];
                    }
                    else if (i < k)
                    {
                        pre[i][k] = 1;
                        preferences[ranks[i]][ranks[k]] += pre[i][k];

                    }
                    else if (i > k)
                    {
                        pre[i][k] = 0;
                        preferences[ranks[i]][ranks[k]] += pre[i][k];
                    }
                }
            }
        }
    }
    printf("\n");
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO


    for (int k = 0; k < candidate_count; k++)
    {
        for (int i = 0; i < candidate_count; i++)
        {
            for (int j = 0; j < candidate_count; j++)
            {
                if (i != j)
                {
                    if (preferences[i][j] > preferences[j][i])
                    {
                        pairs[k].winner = i;
                        pairs[k].loser = j;
                        pair_count++;
                    }
                    else if (preferences[i][j] < preferences[j][i])
                    {
                        pairs[k].winner = j;
                        pairs[k].loser = i;
                        pair_count++;
                    }
                }
                if (preferences[i][j] > 0)
                {
                    if (preferences[i][j] > preferences[j][i])
                    {
                        pairs[k].winner = i;
                        pairs[k].loser = j;
                        pair_count++;
                    }
                    else if (preferences[i][j] < preferences[j][i])
                    {
                        pairs[k].winner = j;
                        pairs[k].loser = i;
                        pair_count++;

                    }
                }
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
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
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        // avoiding the equals pairs
        // need conditions locked[pairs[i].winner][pairs[i].loser] = true;
        if (!check_cycle(pairs[i].winner, pairs[i].loser))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }

    }
    return;
}
bool check_cycle(int winner, int loser)
{
    // conditions
    // whe i++ also j++
    if (winner == loser)
    {
        return true;
    }
    int i = 0;
    while (i < pair_count)
    {
        if (loser == pairs[i].winner && locked[pairs[i].winner][pairs[i].loser] == true)
        {
            if (winner == pairs[i].loser)
            {
                return true;
            }
            else
            {
                if (check_cycle(winner, pairs[i].loser))
                {
                    return true;
                }
            }
        }
        i++;
    }
    return false;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    int checker[candidate_count];
    for (int i = 0; i < candidate_count; i++)
    {
        checker[i] = 0;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            checker[i] += locked[j][i];
        }
        if (checker[i] == 0)
        {
            printf("%s\n", candidates[i]);
            return;
        }
    }
    return;
}

