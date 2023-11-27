#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Checks if a linked list has a cycle.
 *
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
listint_t *one = list;
listint_t *two = list;
while (two && two->next)
{
one = one->next;
two = two->next->next;
if (one == two)
return (1);
}
return (0);
}

