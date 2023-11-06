#include "lists.h"

/**
 * _palindrome - function that palind or not
 * @head: struct
 * Return: 0 if it's not a palindrome and 1 if not.
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	return (aux_palind(head, *head));
}

/**
 * aux_palind - function to check if it's palindrome.
 * @head: head list.
 * @end: end list.
 * Return: 0
 */

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
	{
		return (1);
	}
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
