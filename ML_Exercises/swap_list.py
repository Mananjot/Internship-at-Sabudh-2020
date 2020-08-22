# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    def appendHead(self, val):
        if self.count == 0:
            self.head = ListNode(val)
        else:
            curr = ListNode(val, self.head)
            self.head = curr
        self.count += 1
    def append(self, val):
        if self.count == 0:
            self.head = ListNode(val)
        else:
            prev = self.head
            for _ in range(self.count - 1):
                prev = prev.next 
            add = ListNode(val)
            prev.next = add
        self.count += 1
    def clear(self):
        self.head = None
    def display(self):
        curr = self.head
        for _ in range(self.count):
            print(curr.val)
            curr = curr.next
  
        
class Solution:
    def swapLinkedLists(self, l1: ListNode,key: int) -> ListNode:
        swapList = LinkedList()
        resultList = LinkedList()
        while l1 != None:
            for _ in range(key):
                swapList.appendHead(l1.val)
                l1 = l1.next
            ptr = swapList.head
            for _ in range(key):
                resultList.append(ptr.val)
                ptr =ptr.next
            swapList.clear()
        resultList.display()
        return resultList.head
          
l1 = LinkedList()
l2 = LinkedList()

a1 = [2,9,1,2,1,3]

for i in range(len(a1)):
    l1.append(a1[i])
solution = Solution()
solution.swapLinkedLists(l1.head, 3)
