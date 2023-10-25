############################################################
# Write code in this file
# Post this file in Canvas
# Cut and paste the whole file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run this file 4 times in 225, 235,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    # NOTHING CAN BE CHANGED HERE
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


############################################################
#  class  Slist
###########################################################


class Slist:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0

    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################

    def _add_first(self, value: int):
        new_node = ListNode(value)

        if self._first is None and self._last is None:
            self._first = new_node
            self._last = new_node
        else:
            new_node.next = self._first
            self._first = new_node
        self._len += 1

    def _add_last(self, value: int):
        new_node = ListNode(value)

        if self._first is None and self._last is None:
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._len += 1

    def _delete_first(self):
        if self._first is not None:
            if self._last == self._first:
                self._first = None
                self._last = None
                self._len -= 1
                return
            self._first = self._first.next
            self._len -= 1
            return True
        return False

    def _delete_last(self):
        if self._first is not None:
            temp = self._first
            if self._last == self._first:
                self._first = None
                self._last = None
                self._len -= 1
                return
            while temp.next.next is not None:
                temp = temp.next
            self._last = temp
            self._last.next = None
            self._len -= 1
            return True
        return False

    def _get_first(self):
        if self._first is not None:
            return self._first.val

    def _get_last(self):
        if self._last is not None:
            return self._last.val

############################################################
#  class  MyStack
# 225. Implement Stack using Queues

# https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, x: int) -> None:
        self._s._add_first(x)

    def pop(self) -> int:
        top = self._s._get_first()
        self._s._delete_first()
        return top

    def top(self) -> int:
        return self._s._get_first()

    def empty(self) -> bool:
        if self._s._len is 0:
            return True
        return False

############################################################
#  class  MyStack
# 225. Implement Stack using Queues

# https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        # NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, x: int) -> None:
        self._s._add_first(x)

    def pop(self) -> int:
        top = self._s._get_first()
        self._s._delete_first()
        return top

    def top(self) -> int:
        return self._s._get_first()

    def empty(self) -> bool:
        if self._s._len is 0:
            return True
        return False