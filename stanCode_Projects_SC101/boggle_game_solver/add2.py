"""
File: add2.py
Name: Norah Liao
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    cur1 = l1
    cur2 = l2
    lst1 = []
    lst2 = []

    while cur1 is not None:
        lst1.append(cur1.val)
        cur1 = cur1.next
    while cur2 is not None:
        lst2.append(cur2.val)
        cur2 = cur2.next

    value1 = 0
    value2 = 0
    counter = 0
    for i in range(len(lst1)-1, -1, -1):
        value1 += lst1[i] * (10 ** counter)
        counter += 1

    counter = 0
    for j in range(len(lst2)-1, -1, -1):
        value2 += lst2[j] * (10 ** counter)
        counter += 1

    new_value = value1 + value2

    l3 = None
    if new_value == 0:
        l3 = ListNode(0, None)
    else:
        while new_value != 0:
            data = new_value % 10
            new_node = ListNode(data, None)
            if l3 is None:
                # first data
                l3 = new_node
                new_value = new_value // 10
            else:
                cur3 = l3
                while cur3.next is not None:
                    cur3 = cur3.next
                cur3.next = new_node
                new_value = new_value // 10
    return l3


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
