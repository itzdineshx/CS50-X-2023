#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

//max number of canditates
#define MAX 8

//define a struct called canditates
typedef struct
{
    string name;
    int vote;
}
canditate;

//Array of canditates
canditate canditates[MAX];

int canditate_count;

int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    canditate_count = argc - 1;
    if (canditate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }

    for (int i = 0; i < canditate_count; i++)
    {
        canditates[i].name = argv[i + 1];
        canditates[i].vote = 0;
    }

    int voter_count = get_int("Number of Voters: ");

    //loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        if (!vote(name))
        {
            printf("Invalid Vote.\n");
        }
    }
    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    int a
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    return;
}
