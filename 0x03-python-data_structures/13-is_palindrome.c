#include "lists.h"
#include <stddef.h>

/**
 * listint - linked list
 * @head: Pointer to the first node in the list
 *
 * Return: Pointer to the first node in the new list
 */
void listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the linked list
 *
 * Return: 1 if it is true or 0 if not true
 */
int is_palindrome(listint_t **head)
{
	listint_t *sedate = *head, *swift = *head, *temp = *head, *del = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		swift = swift->next->next;
		if (!swift)
		{
			del = sedate->next;
			break;
		}
		if (!swift->next)
		{
			del = sedate->next->next;
			break;
		}
		sedate = sedate->next;
	}

	listint(&del);

	while (del && temp)
	{
		if (temp->n == del->n)
		{
			del = del->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!del)
		return (1);

	return (0);
}
