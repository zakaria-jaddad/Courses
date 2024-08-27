    while (i < pair_count)
    {
        if (winner != loser && winner == pairs[i + 1].loser && loser == pairs[i + 1].winner)
        {
            i++;
            return true;
        }
        i++;
    }
    return false;





        if (winner == loser)
    {
        return false;
    }
    int i = 0;
    while (i < pair_count)
    {
        if (winner == pairs[i].loser && locked[pairs[i].winner][pairs[i].loser] == true)
        {
            if (loser == pairs[i].winner)
            {
                return true;
            }
            else
            {
                if (head(winner, pairs[i].loser))
                {}
            }
        }
        i++;
    }
    return true;
}
// print winner function
void print_winner(void)
{
    // TODO
    for (int i = 0; i < pair_count; i++)
    {
        if (locked[pairs[i].winner][pairs[i].loser] == true)
        {
            if (!head(pairs[i].winner, pairs[i].loser))
            {
                printf("%s\n", candidates[pairs[i].winner]);

            }
        }
    }
    return;
}
bool head(int winner, int loser)
{
}

// print winner second
void print_winner(void)
{
    // TODO
    for (int i = 0; i < pair_count; i++)
    {
        if (locked[pairs[i].winner][pairs[i].loser] == true)
        {
            if (!head(pairs[i].winner))
            {
                printf("%s\n", candidates[pairs[i].winner]);
                return;

            }
        }
    }
    return;
}

bool head(int winner)
{
    for (int i = 0; i < pair_count; i++)
    {
        if (locked[pairs[i].winner][pairs[i].loser] == true)
        {
            if (winner == pairs[i].loser)
            {
                return true;
            }
        }
    }
    return false;




    
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




