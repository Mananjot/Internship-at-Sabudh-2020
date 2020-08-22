class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    def append(self, val):
        if self.count == 0:
            self.head = Node(val)
        else:
            pre_node = self.head
            for _ in range(self.count - 1):
                pre_node = pre_node.next
            add_node = Node(val)
            pre_node.next = add_node
        self.count += 1
    def changeHead(self,val):
        if self.count == 0:
            self.head = Node(val)

        else:
            curr = Node(val, self.head)
            self.head = curr
            
        self.count += 1
    def display(self):
        curr = self.head
        for _ in range(self.count):
            print(curr.val)
            curr = self.head.next

    
class Solution:
    def __init__(self):
        self.sumList = LinkedList() 
    def computeCarry(self,num1, num2, carry):
        if num1.next == num2.next == None:
            sum = num1.val + num2.val
            if sum >= 10:
                sum -= 10
                carry = 1
            # self.result_stack.append(sum)
            self.sumList.changeHead(sum)
            return carry
        else:
            sum = self.computeCarry(num1.next, num2.next, carry) + num1.val + num2.val
            if sum >= 10:
                sum -= 10
                carry = 1
            else:
                carry = 0
            # self.result_stack.append(sum)
            self.sumList.changeHead(sum)
            return carry
    def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
        l1Length = 0
        l2Length = 0
        l1Head = l1
        l2Head = l2
        # Counting Lengths of Linked List
        while l1Head != None:
            l1Length += 1
            l1Head = l1Head.next           
            
        while l2Head != None:
            l2Length += 1
            l2Head = l2Head.next   

        if l1Length < l2Length:
            for _ in range(l2Length - l1Length):
                curr = Node(0, l1)
                l1 = curr
        # print(l1.val, l1.next.val, l1.next.next.val, l1.next.next.next.val)
        elif l1Length > l2Length:
            for _ in range(l1Length - l2Length):
                curr = Node(0, l2)
                l2 = curr
        # print(l2.val, l2.next.val, l2.next.next.val, l2.next.next.next.val)
        # print(l1.val)
        carry = self.computeCarry(l1, l2, 0)
        if carry == 1:
            # self.result_stack.append(carry)
            self.sumList.changeHead(1)
        # print(self.result_stack)
        self.sumList.display()
        # print(self.sumList.head.val, self.sumList.head.next.val, self.sumList.head.next.next.val )
        


l1 = LinkedList()
l2 = LinkedList()
a2 = [1,2,3,4]
a1 = [9,4,2,9]
for i in range(len(a1)):
    l1.append(a1[i])
for i in range(len(a2)):
    l2.append(a2[i])


sol = Solution()
sol.addTwoNumbers(l1.head, l2.head)
