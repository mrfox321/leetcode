import heapq

def mergeKLists(lists):

#manicure lists
    lists = [x for x in list1 if x]
    if not lists or not lists[0]:
        return
    print lists
    head = ListNode(0)
    root  = head
    #initialize lists into heap
    bubble = []

    for linked in lists:
        heapq.heappush(bubble,(linked.val,linked))

    while bubble:
        node = heapq.heappop(bubble)
        #node[1] is node object
        root.next = node[1]
        if node[1].next is not None:
            newnode = node[1].next
            heapq.heappush(bubble,(newnode.val,newnode))
            node[1].next = None
        root = root.next
    return head.next
