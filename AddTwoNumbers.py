class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        
        count = total = 0
        while l1 != None or l2!=None:
            if l1 != None and l2!=None:
                total += (l1.val + l2.val)*(10**count)
                count+=1
                l1 = l1.next
                l2 = l2.next
                
            elif l1 ==None :
                total += l2.val*(10**count)
                count+=1
                l2 = l2.next
                
            elif l2 == None:
                total += l1.val*(10**count)
                count+=1
                l1 = l1.next
        print(total)
        Answer = temp = ListNode(total%10)
        total = total//10
        while total!=0:
            temp.next = ListNode(total%10)
            temp = temp.next
            # temp.val = 
            total=total//10
        return Answer
        
        