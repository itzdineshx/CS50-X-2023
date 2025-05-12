#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>

bool valid_triangle(float x, float y, float z);

float sum(float a, float b, float c);

int main(void)
{
    // get the sides of the triangle
    int side1, side2, side3;

    side1 = get_int("Enter side1: ");
    side2 = get_int("Enter side2: ");
    side3 = get_int("Enter side3: ");

    // check if it's a valid triangle

    if (valid_triangle(side1, side2, side3))
    {
        printf("Valid Triangle.\n");
        // calculate the sum of the triangle
        float sum_of_triangle = sum(side1, side2, side3);
        printf("Sum of Trinagle is %2f\n", sum_of_triangle);
    }
    else
    {
        printf("Not a Valid Triangle.\n");
    }
}
bool valid_triangle(float x, float y, float z)
{
    if (x <= 0 || y <= 0 || z <= 0)
    {
        return false;
    }

    if ((x + y <= z) || (y + z <= x) || (x + z <= y))
    {
        return false;
    }

    return true;
}

float sum(float a, float b, float c)
{
    float sum = a + b + c;
    return sum;
}
