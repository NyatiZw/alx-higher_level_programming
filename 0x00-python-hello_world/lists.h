#ifndef _LISTS_H_
#define _LISTS_H_

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer member
 * @next: pointer to next node
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const list_t *h);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* _LISTS_H */
