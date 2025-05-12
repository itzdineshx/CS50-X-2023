#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, row, column;
    do
    {
        height = get_int("Enter Height: ");
    }
    while (height < 1 || height > 8);

    for (row = 0; row < height; row++)
    {
        for (column = 0; column < height - row - 1; column++)
        {
            printf(" ");
        }
        for (column = 0; column <= row; column++)
        {
            printf("#");
        }

        printf("  ");

        for (column = 0; column <= row; column++)
        {
            printf("#");
        }
        printf("\n");
    }
}