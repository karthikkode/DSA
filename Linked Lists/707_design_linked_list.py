from typing import Optional

class Node:
    def __init__(self, val: int) -> None:
        self.next: Optional['Node'] = None
        self.val: int = val


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size or self.head is None:
            return -1
        
        curr_node = self.head
        for i in range(index):
            curr_node = curr_node.next  
        
        return curr_node.val
            
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        newNode = Node(val)
        curr_node = self.head
        for _ in range(index - 1):
            curr_node = curr_node.next
        newNode.next = curr_node.next
        curr_node.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            curr_node = self.head
            for _ in range(index - 1):
                curr_node = curr_node.next
            curr_node.next = curr_node.next.next
        self.size -= 1

    def middleNode(self):
        curr = self.head
        size = 0
        mid = 0
        while curr.next is not None:
            curr = curr.next
            size+=1

        if size%2==0:
            mid = size//2
        else:
            mid = (size//2)+1

        curr = self.head
        for i in range(mid):
            curr = curr.next
        
        return curr
    
    def middleNodeSFPointer(self):
        s=self.head
        f=self.head
        while (f is not None and f.next is not None):
            s = s.next
            f = f.next.next
        return s

# Your MyLinkedList object will be instantiated and called as such: