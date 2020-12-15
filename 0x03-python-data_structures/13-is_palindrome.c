#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if is a palindrome
 * @head: a linked list
 * Return: 1 if true 0 if false
**/
int is_palindrome(listint_t **head)
{
	listint_t *first;
	listint_t *last;
	int i = 0;
	int j = 0;
	int k = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	first = *head;
	last = *head;
	while (last->next != NULL)
	{
		last = last->next;
		j++;
	}
	while (first != last && last->next != first)
	{
		if (first->n == last->n)
		{
			j--;
			last = *head;
			k = 0;
			while (k != j)
			{
				last = last->next;
				k++;
			}
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
