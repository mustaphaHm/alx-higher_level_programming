#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - function that checks if a linked list has a cycle int it
 * @list: linked list as parameter
 * Return: 0 if there is no cycle otherwise 1
 */
int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
		return (0);
	list node1 = list;
	list node2 = list->next;

	while (node2 != NULL && node2->next != NULL)
	{
		if (node1 == node2)
			return (1);
		node1 = node1->next;
		node2 = node2->next->next;
	}
	return (0);
}
