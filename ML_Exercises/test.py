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
class Solution:
    def __init__(self):
        self.result_stack = []
    def compute(self,num1, num2, carry):
        if num1.next == num2.next == None:
            sum = num1.val + num2.val
            if sum >= 10:
                sum -= 10
                carry = 1
            self.result_stack.append(sum)
            return carry
        else:
            sum = self.compute(num1.next, num2.next, carry) + num1.val + num2.val
            if sum >= 10:
                sum -= 10
                carry = 1
            else:
                carry = 0
            self.result_stack.append(sum)
            return carry
            
    def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
        length_l1 = 0
        length_l2 = 0
        head_l1 = l1
        head_l2 = l2
        # Counting the elements in the linked list
        while l1 != None:
            length_l1 += 1
            l1 = l1.next
        l1 = head_l1                # Come back to head node of 1st linked list
            
        while l2 != None:
            length_l2 += 1
            l2 = l2.next 
        l2 = head_l2                # Come back to head node of 2nd linked list
        
        # Shifting the pointer of long list to match head of smaller list
        # No need when lengths are equal
        if length_l1 >= length_l2:
            for _ in range(length_l1 - length_l2):
                l1 = l1.next
            carry = self.compute(l1, l2, 0)  # head nodes of list with carry 0
            l1 = head_l1
            print(carry)
            print(l1.val)
            for _  in range(length_l1 - length_l2):
                sum = l1.val + carry
                if sum >= 10:
                    sum -= 10
                    carry = 1
                else:
                    carry = 0
                self.result_stack.append(sum)
                l1 = l1.next
        elif length_l2 > length_l1:
            for _ in range(length_l2 - length_l1):
                l2 = l2.next
            carry = self.compute(l1, l2, 0)  # head nodes of list with carry 0
            l2 = head_l2
            for _ in range(length_l2 - length_l1):
                sum = l2.val + carry
                if sum >= 10:
                    sum -= 10
                    carry = 1
                else:
                    carry = 0
                self.result_stack.append(sum)
                l2 = l2.next
        if carry == 1:
            self.result_stack.append(1)

            
        # Calling the function to compute sum of trimmed lists
        
        
        print(self.result_stack)
        
l1 = LinkedList()
l2 = LinkedList()

a1 = [2,9,9,1,2,3,4]
a2 = [9,4,2,9]
for i in range(len(a1)):
    l1.append(a1[i])
for i in range(len(a2)):
    l2.append(a2[i])


sol = Solution()
sol.addTwoNumbers(l1.head, l2.head)

            