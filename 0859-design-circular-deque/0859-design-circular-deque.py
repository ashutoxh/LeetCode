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


class MyCircularDeque:
    def __init__(self, k: int):
        # NOTHING CAN BE CHANGED HERE
        self._K = k
        self._s = Slist()

    def insertFront(self, value: int) -> bool:
        if self._s._len < self._K:
            self._s._add_first(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self._s._len < self._K:
            self._s._add_last(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self._s._len != 0:
            self._s._delete_first()
            return True
        return False

    def deleteLast(self) -> bool:
        if self._s._len != 0:
            self._s._delete_last()
            return True
        return False

    def getFront(self) -> int:
        if self._s._len != 0:
            return self._s._get_first()
        return -1

    def getRear(self) -> int:
        if self._s._len != 0:
            return self._s._get_last()
        return -1

    def isEmpty(self) -> bool:
        if self._s._len == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self._s._len == self._K:
            return True
        return False

############################################################
#  MyCircularDeque
# 641. Design Circular Deque
# https://leetcode.com/problems/design-circular-deque

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        # NOTHING CAN BE CHANGED HERE
        self._K = k
        self._s = Slist()

    def insertFront(self, value: int) -> bool:
        if self._s._len < self._K:
            self._s._add_first(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self._s._len < self._K:
            self._s._add_last(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self._s._len != 0:
            self._s._delete_first()
            return True
        return False

    def deleteLast(self) -> bool:
        if self._s._len != 0:
            self._s._delete_last()
            return True
        return False

    def getFront(self) -> int:
        if self._s._len != 0:
            return self._s._get_first()
        return -1

    def getRear(self) -> int:
        if self._s._len != 0:
            return self._s._get_last()
        return -1

    def isEmpty(self) -> bool:
        if self._s._len == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self._s._len == self._K:
            return True
        return False