#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start;
    do
    {
        start = get_int("Start Size? ");
    }
    while (start < 9);

    int end;
    do
    {
        end = get_int("End Size? ");
    }
    while (end < start);

    int years = 0;
    while (start < end) // Corrected while loop condition
    {
        start = start + (start / 3) - (start / 4);
        years++;
    }

    printf("Years: %i\n", years);

    return 0; // Added return statement
}
