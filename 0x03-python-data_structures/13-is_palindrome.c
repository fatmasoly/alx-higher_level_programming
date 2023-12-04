#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * recursive_palindrom - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @end: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
int recursive_palindrom(listint_t **head, listint_t *end)
{
if (end == NULL)
return (1);
if (recursive_palindrom(head, end->next) && ((*head)->n == end->n))
{
(*head) = (*head)->next;
return (1);
}
return (0);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: A double pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *head2 = *head;
listint_t **head_copy = &head2;
if (head == NULL || *head == NULL)
return (1);
return (recursive_palindrom(head_copy, *head));
}
