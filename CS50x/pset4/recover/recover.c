#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
int main(int argc, char *argv[])
{
    if (argc == 1 || argc > 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    char filename[8];
    BYTE buffer[sizeof(512 * sizeof(BYTE))];
    int image_counter = 0;
    FILE *output = NULL;
    FILE *card = fopen(argv[1], "r");
    while (fread(buffer, 1, sizeof(512 * sizeof(BYTE)), card) == sizeof(512 * sizeof(BYTE)))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (image_counter == 0)
            {
                sprintf(filename, "%03i.jpg", image_counter);
                output = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), sizeof(512 * sizeof(BYTE)), output);
                image_counter++;
            }
            else if (image_counter > 0)
            {
                fclose(output);
                sprintf(filename, "%03i.jpg", image_counter);
                output = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), sizeof(512 * sizeof(BYTE)), output);
                image_counter++;

            }
        }
        else
        {
            if (image_counter > 0)
            {
                fwrite(buffer, sizeof(BYTE), sizeof(512 * sizeof(BYTE)), output);
            }
        }
    }
    fclose(output);
    fclose(card);
}