#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check for loop in linked list
 *
 * @list: pointer to list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	if (list == NULL || list->next == NULL)
		return (0);

	a = list->next;
	b = list->next->next;

	while (a && b && b->next)
	{
		if (a == b)
			return (1);
		a = a->next;
		b = b->next->next;
	}
	return (0);
}
