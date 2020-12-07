#include "lists.h"

/**
 * check_cycle - check for a loop in linked list
 * @list: a linked list
 * Return: 1 if loop 0 if not
**/
int check_cycle(listint_t *list)
{
	listint_t *p1;
	listint_t *p2;

	if (list == NULL)
		return (0);

	p1 = list;
	p2 = list;

	while (p2->next != NULL && p2->next->next != NULL)
	{
		p1 = p1->next;
		p2 = p2->next->next;
		if (p1 == p2)
		{
			p1 = list;
			while (p1 != p2)
			{
				p1 = p1->next;
				p2 = p2->next;
			}
			return (1);
		}
	}
	return (0);
}
