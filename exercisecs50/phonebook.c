#include <stdio.h>
#include <cs50.h>

int main (void)
{
    string name = get_string("Enter User's Name: ");

    int age = get_int("Enter User's Age: ");

    int number = get_int("Enter user's Phone Number: ");

    printf("Name is %s. Age is %i. Phone Number is %i.", name, age, number);

}