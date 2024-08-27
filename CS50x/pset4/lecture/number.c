#include <stdio.h>

int main(void)
{
    int number[] = {5, 6, 9, 0, 4, 1, 90};

// +1 depends what data type used if int [ + 1] means move  with 4 bytes if char [ + 1] means with 1 byte
    printf("%i\n", *number);
    printf("%i\n", *(number + 1));
    printf("%i\n", *(number + 2));
    printf("%i\n", *(number + 3));
    printf("%i\n", *(number + 4));
    printf("%i\n", *(number + 5));
    printf("%i\n", *(number + 6));

}