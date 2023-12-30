class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = second = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                first.next = list1
                list1 = list1.next
            else:
                first.next = list2
                list2 = list2.next
            first = first.next

        if list1:
            first.next = list1
        else:
            first.next = list2

        return second.next