#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *first;
	listint_t *last;
	int i = 0;
	int j = 0;
	int k = 0;
	int len;

	first = *head;
	last = *head;
	while (last->next != NULL)
	{
		last = last->next;
		len++;
	}

	j = len;
	while (i != j)
	{
		if (first->n == last->n)
		{
			j--;
			last = *head;
			k = 0;
			while (k != j)
				last = last->next;
		}
		else
		{
			return (0);
		}
		i++;
		first = first->next;
	}
	return (1);
}
