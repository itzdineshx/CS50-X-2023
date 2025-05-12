#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        // Check the command line argument is 2
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open file for reading
    FILE *input_file = fopen(argv[1], "r");

    // Check if the input_file is valid
    if (input_file == NULL)
    {
        printf("Could not open file\n");
        return 2;
    }

    // Store blocks of 512 bytes in an array
    unsigned char buffer[512];

    // Track the number of images generated
    int count_image = 0;

    // File pointer for recovered images
    FILE *output_file = NULL;

    // Allocate memory for filename
    char filename[8];

    // Read the blocks with a while loop
    while (fread(buffer, sizeof(char), 512, input_file))
    {
        // Check if bytes indicate the start of a JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous output file if it's open
            if (output_file != NULL)
            {
                fclose(output_file);
            }

            // Write the JPEG file names
            sprintf(filename, "%03i.jpg", count_image);

            // Open output file for writing
            output_file = fopen(filename, "w");

            // Increment the count of found images
            count_image++;
        }

        // Check if output_file is valid
        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output_file);
        }
    }

    // Close the opened files
    fclose(input_file);

    // Close the last output file if it's open
    if (output_file != NULL)
    {
        fclose(output_file);
    }

    return 0;
}
