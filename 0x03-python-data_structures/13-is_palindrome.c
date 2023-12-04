#include <stddef.h>
#include "lists.h"
/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL, *current = head, *next = NULL;
while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
return (prev);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);
listint_t *slow = *head, *fast = *head;
listint_t *second_half = NULL, *prev_slow = *head;
int is_palindrome = 1;
while (fast != NULL && fast->next != NULL)
{
prev_slow = slow;
slow = slow->next;
fast = fast->next->next;
}
second_half = reverse_list(slow);
while (*head != NULL && second_half != NULL)
{
if ((*head)->n != second_half->n)
{
is_palindrome = 0;
break;
}
*head = (*head)->next;
second_half = second_half->next;
}
prev_slow->next = reverse_list(reverse_list(slow));
return (is_palindrome);
}

