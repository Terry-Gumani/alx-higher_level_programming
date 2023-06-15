# include "lists.h"
/**
 * print_dlistint - function that prints all the elements of a dlistint_t list.
 * @h: input node
 * Return: number of element
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *tmp = NULL;
	size_t count = 0;
	if (h == NULL)
		return (0);
	tmp = h;
	if (tmp->prev != NULL)
	{
		while (tmp->prev != NULL)
		{
			tmp = tmp->prev;
		}
	}
	while (tmp != NULL)
	{
		printf("%d\n", tmp->n);
		count++;
		tmp = tmp->next;
	}
	return (count);
}
