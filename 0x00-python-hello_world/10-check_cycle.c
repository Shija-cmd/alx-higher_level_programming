#include "lists.h"

/**
 * check_cycle - Function to checks if a singly linked list has a cycle.
 * @list: Pointer to the beginning of the node
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *h)
{
	listint_t *current, *check;

	if (h == NULL || h->next == NULL)
		return (0);
	current = h;
	check = current->next;

	while (current != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
