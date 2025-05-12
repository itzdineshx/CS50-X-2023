#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get the length from the user
    int length;
    do
    {
        length = get_int("Enter Number: ");
    }
    while (length < 1);

    // Declare our Array
    int twice[length];

    // set the first value of array
    twice[0] = 1;
    printf("%i\n", twice[0]);

    // twice the number and print!
    for (int i = 1; i < length; i++)
    {
        twice[i] = 2 * twice[i - 1];
        printf("%i\n", twice[i]);
    }
}