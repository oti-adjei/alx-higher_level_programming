#include "lists.h"

/**
 * check_cycle - check if the list
 * has a cycle
 * @list: head pointer
 * Return: int
 */
int check_cycle(listint_t *list)
{

listint_t *slow = list;
listint_t *fast = list;

while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
{
return (1);
}
}
return (0);
}
