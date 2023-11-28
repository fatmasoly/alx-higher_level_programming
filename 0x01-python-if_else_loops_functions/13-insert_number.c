#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The number to be inserted.
 *
 * Return: The address of the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head;
listint_t *new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);
new_node->n = number;
new_node->next = NULL;
if (node == NULL || new_node->n < node->n)
{
new_node->next = node;
return (*head = new_node);
}
while (node)
{
if (node->next == NULL || new_node->n < node->next->n)
{
new_node->next = node->next;
node->next = new_node;
return (new_node);
}
node = node->next;
}
return (NULL);
}

