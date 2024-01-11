#include "lists.h"

/**
 * print_dlistint - prints all the elements of a list
 * @h - list
 * Return: count.
 */
size_t print_dlistint(const dlistint_t *h)
{
	int count;
	dlistint_t *current = h;

	count = 0;
	while (current != NULL)
	{
		count += 1;
		current = current->next;
	}
	return (count);
}
