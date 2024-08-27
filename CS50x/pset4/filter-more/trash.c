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
                    for (int check = -2; check <= 2; check++)
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
                    if (k == i + 1)
                        break;
                    else
                    {
                        k++, d = j - 1;
                        counter++;
                    }
            }
            // still disccusing the solution
            for (int back = 0; back < 3; back++)
            {
                square_root[back] = sqrt(pow(temp[back] , 2) + pow(temp1[back] , 2));
                temp[back] = 0, temp1[back] = 0;
            }
            image[i][j].rgbtBlue = round(square_root[0]);
            image[i][j].rgbtGreen = round(square_root[1]);
            image[i][j].rgbtRed = round(square_root[2]);
            counter = 0;
        }
    }
    return;
}




            if (square_root[0] > 255)
                image[i][j].rgbtBlue = 255;
            else
                image[i][j].rgbtBlue = square_root[0];
            if (square_root[1] > 255)
                image[i][j].rgbtGreen = 255;
            else
                image[i][j].rgbtGreen = square_root[1];
            if (square_root[2] > 255)
                image[i][j].rgbtRed = 255;
            else
                image[i][j].rgbtRed = square_root[2];
            counter = 0;
        }