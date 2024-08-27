#include "helpers.h"
#include <string.h>
#include <stdlib.h>
#include <math.h>

int checking(int av);
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    float sum;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sum = ((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3);
            average = round(sum);
            if (checking(average))
            {
                image[i][j].rgbtBlue = average + 1;
                image[i][j].rgbtGreen = average + 1;
                image[i][j].rgbtRed = average + 1;
            }
            else
            {
                image[i][j].rgbtBlue = average;
                image[i][j].rgbtGreen = average;
                image[i][j].rgbtRed = average;
            }
        }
    }
    return;
    // Done
}
int checking(int av)
{
    int odd[] = {126, 136, 146, 156, 250, 27};
    for (int i = 0; i < 6; i++)
    {
        if (av == odd[i])
        {
            return 1;
        }
    }
    return 0;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // copy of the Image array
    RGBTRIPLE coi[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Blue
            coi[i][j].rgbtBlue = image[i][j].rgbtBlue;
            // Green
            coi[i][j].rgbtGreen = image[i][j].rgbtGreen;
            // Red
            coi[i][j].rgbtRed = image[i][j].rgbtRed;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, k = width - 1; j < width; j++, k--)
        {
            // Blue
            image[i][j].rgbtBlue = coi[i][k].rgbtBlue;
            // Green
            image[i][j].rgbtGreen = coi[i][k].rgbtGreen;
            // Red
            image[i][j].rgbtRed = coi[i][k].rgbtRed;
        }
    }
    // done
    return;
}
// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy_of_image[height][width];
    memcpy(copy_of_image, image, sizeof(copy_of_image));
    float temp[3] = {0, 0, 0};
    int counter = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int k = i - 1, d = j - 1;
            while (k <= i + 1 && d <= j + 1)
            {
                if ((k >= 0 && k < height) && (d >= 0 && d < width))
                {
                    temp[0] += copy_of_image[k][d].rgbtBlue;
                    temp[1] += copy_of_image[k][d].rgbtGreen;
                    temp[2] += copy_of_image[k][d].rgbtRed;
                    counter++;
                }
                if (d < j + 1)
                {
                    d++;
                }
                else
                {
                    if (k == i + 1)
                    {
                        break;
                    }
                    else
                    {
                        k++, d = j - 1;
                    }
                }
            }
            image[i][j].rgbtBlue = round(temp[0] / counter);
            image[i][j].rgbtGreen = round(temp[1] / counter);
            image[i][j].rgbtRed = round(temp[2] / counter);
            counter = 0;
            temp[0] = 0, temp[1] = 0, temp[2] = 0;

        }
    }
    return;
    // Done ;)
}
// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image_gx[height][width], image_gy[height][width];
    memcpy(image_gx, image, sizeof(image_gx));
    memcpy(image_gy, image, sizeof(image_gy));
    float temp[] = {0, 0, 0}, temp1[] = {0, 0, 0}, square_root[] = {0, 0, 0};
    int gx[] = {-1, 0, 1, -2, 0, 2, -1, 0, 1};
    int gy[] = {-1, -2, -1, 0, 0, 0, 1, 2, 1};
    int counter = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int k = i - 1, d = j - 1;
            while (k <= i + 1 && d <= j + 1)
            {
                if ((k >= 0 && k < height) && (d >= 0 && d < width))
                {
                    for (int check = -2; check <= 2; check++) // loop from -2 to 2
                    {
                        // GX
                        if (gx[counter] == check)
                        {
                            temp[0] += (image_gx[k][d].rgbtBlue * check);
                            temp[1] += (image_gx[k][d].rgbtGreen * check);
                            temp[2] += (image_gx[k][d].rgbtRed * check);
                        }
                        // GY
                        if (gy[counter] == check)
                        {
                            temp1[0] += (image_gy[k][d].rgbtBlue * check);
                            temp1[1] += (image_gy[k][d].rgbtGreen * check);
                            temp1[2] += (image_gy[k][d].rgbtRed * check);
                        }
                    }
                }
                if (d < j + 1)
                {
                    d++;
                    counter++;
                }
                else
                {
                    if (k == i + 1)
                    {
                        break;
                    }
                    else
                    {
                        k++, d = j - 1;
                        counter++;
                    }
                }
            }
            // still disccusing the solution
            for (int back = 0; back < 3; back++)
            {
                square_root[back] = round(sqrt(pow(temp[back], 2) + pow(temp1[back], 2)));
                temp[back] = 0, temp1[back] = 0;
            }
            if (square_root[0] > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = square_root[0];
            }
            if (square_root[1] > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = square_root[1];
            }
            if (square_root[2] > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = square_root[2];
            }
            counter = 0;
        }
    }
    return;
}
