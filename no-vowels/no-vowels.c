#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>


//include the prototype of modifying function
string replace_vowels(string phrase);

int main(int argc, string argv[])
{
    //check the input count

    if (argc != 2)
    {
        printf("Usage: %s <input_string>\n", argv[0]);
        return 1;
    }

    string modified = replace_vowels(argv[1]);

    printf("Modified Number: %s\n", modified);

    return 0;
}

string replace_vowels(string result)
{
    int length = strlen(result);

    for (int i = 0; i < length; i++)
    {
        //make the each element to lower
        char c = tolower(result[i]);

        switch (c)
        {
            case 'a':
                result[i] = 54; // ascii value of 'a'
                break;
            case 'e':
                result[i] = 51; // ascii value of 'e'
                break;
            case 'i':
                result[i] = 49; // ascii value of 'a'
                 break;
            case 'o':
                result[i] = 48; // ascii value of 'i'
                break;
            default:
                break;
        }
    }

    return result;
}
