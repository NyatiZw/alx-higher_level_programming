#include "lists.h"

/**
 * check_cycle:- 'Function to check cycle in singly linked list
 * @list:- list to check
 * Return: 0 (Fail) || 1 (Success)
 */

int check_cycle(listint_t *list)
{
	listint_t *needle = list;
	listint_t *heystack = list;

	if (!list)
	{
		return (0);
	}

	while (needle && heystack && heystack->next)
	{
		needle = needle->next;
		heystack = heystack->next->next;
		if (needle == heystack)
		{
			return (1);
		}
	}
	return (0);
}
