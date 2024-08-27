#include <stdio.h>
#include <stdlib.h>


typedef struct node
{
    int number;
    struct node *next;
}
node;



int main(void)
{
    node *list = NULL;
    node *n = malloc(sizeof(node));
    // * . is the same as ->
    if (n != NULL)
    {
        n -> number = 1;
        n -> next = NULL;
    }
    list = n;
    n = malloc(sizeof(node));
    // chcking if n is empty
    if (n == NULL)
    {
        free(list);
        return 1;
    }
    // checking if n is not empty
    if (n != NULL)
    {
        n -> number = 2;
        n -> next = NULL;
    }
    // the pointer of the next node is assined to n

    list -> next = n;
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list -> next);
        free(list);
        return 1;
    }
    n -> number = 3;
    n -> next = NULL;

    // printing nubers manually

    // freing all list manually

    // free(list -> next -> next);
    // free(list -> next);
    // free(list);


    // adding a number to the linked list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        while (list != NULL)
        {
        node *temp = list -> next;
            free(list);
            list = temp;
        }
        return 1;
    }

    n -> next = list;
    list = n;



    // printing numbers using for loop
    // firs tpart of the for loop is delaring a pointer and pointing it to what list is pointing
    // second part is checking if temp is NULL
    //third part is like i = i + 1, it's just after the firs loop go and acces the next pointer int the next node





    for (node *temp = list; temp != NULL; temp = temp -> next)
    {
        printf("%i\n", temp -> number);
    }








    // using while loop to free

    while (list != NULL)
    {
       node *temp = list -> next;
        free(list);
        list = temp;
    }
    return 1;
}