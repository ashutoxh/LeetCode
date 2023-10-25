############################################################
# L0977.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################
############################################################
# All imports
###########################################################
from typing import List
from time import process_time

########################################
#Nothing can be changed in class Solution
########################################
class Solution:
    #YOU CANNOT CHANGE THIS INTERFACE
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        work = [0]
        p = L0977(nums,ans,work,False)
        return ans

########################################
#Nothing can be changed in class L0977
########################################
class L0977:
    def __init__(self,a:List[int], ans:List[int], work:'List of size 1', show:'bool'):
        self._a = a ;
        self._ans = ans ;
        self._work = work ;
        self._show = show ;
        algb = AlgL0977(self,ans,show)

    def size(self)->'int':
        return len(self._a)

    def get(self,i:'int'):
        self._work[0] = self._work[0] + 1
        return self._a[i]

########################################
# WRITE CLASS AlgL0977
#YOU CAN HAVE ANY NUMBER OF PRIVATE VARIABLES and FUNCTIONS
########################################
class AlgL0977():
    def __init__(self,h:'L0977', ans:List[int],show:'bool'):
        self._h = h
        self._ans = ans
        self._show = show
        self._alg()

    ########################################
    #   WRITE YOUR CODE BELOW
    #######################################

    ########################################
    # TIME:THETA(N)
    # Space:THETA(N)
    #########################################
    def _alg(self):
        n = self._h.size()
        if n == 0:
            return
        if n == 1:
            a = self._h.get(0)
            return self._ans.append(a * a)
        left_ptr_to_a = 0
        right_ptr_to_a = n - 1
        ptr_to_ans = n - 1
        for index in range(n):
            self._ans.append(0)
        while left_ptr_to_a <= right_ptr_to_a:
            a = self._h.get(left_ptr_to_a)
            b = self._h.get(right_ptr_to_a)
            if abs(a) > abs(b):
                self._ans[ptr_to_ans] = a * a
                left_ptr_to_a += 1
            else:
                self._ans[ptr_to_ans] = b * b
                right_ptr_to_a -= 1
            ptr_to_ans -= 1
