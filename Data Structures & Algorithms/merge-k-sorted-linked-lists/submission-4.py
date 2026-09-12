# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        def mergeTwoLists(l1:Optional[ListNode],l2:Optional[ListNode])->Optional[ListNode]:
            l=ListNode()
            h=l
            while(l1 and l2):
                if (l1.val<=l2.val):
                    l.next=l1
                    l1=l1.next
                else:
                    l.next=l2
                    l2=l2.next
                l=l.next
            
            while l1:
                l.next=l1
                l1=l1.next
                l=l.next

            while l2:
                l.next=l2
                l2=l2.next
                l=l.next
            
            return h.next

        # Divide and Conquer approach
        while len(lists) > 1:
            merged_lists = []
            
            # Merge lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(mergeTwoLists(l1, l2))
                
            lists = merged_lists
            
        return lists[0]