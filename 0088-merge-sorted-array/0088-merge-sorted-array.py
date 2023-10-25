############################################################
# L0088.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2021
###########################################################
############################################################
# All imports
###########################################################
from typing import List
from time import process_time
import math

class Solution:
    #YOU CANNOT CHANGE THIS INTERFACE
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        work = [0]
        p = L0088(nums1,m,nums2,n,work,"ntime_1space")

class L0088:
    def __init__(self,nums1: List[int], m: int, nums2: List[int], n: int,work:'List of size 1',alg:'string') -> None:
        self._nums1 = nums1
        self._m = m
        self._nums2 = nums2
        self._n = n
        self._work = work ;


        if (alg == "ntime_1space"):
            self._n_time_constant_space()
        elif (alg == "nlogntime_1space"):
            self._nlogn_time_constant_space()
        elif (alg == "ntime_nspace"):
            self._n_time_n_space()

        else:
            assert(False)


    ########################################
    # TIME:THETA(Nlogn)
    # Space:THETA(1)
    #########################################
    def _nlogn_time_constant_space(self):
        for i in range(self._m, len(self._nums1)):
            self._nums1[i] = self._nums2[i - self._m]
        self._nums1.sort()
        self._work[0] += math.ceil(len(self._nums1) * math.log(len(self._nums1), 2))

    ########################################
    # TIME:THETA(N)
    # Space:THETA(N)
    #########################################
    def _n_time_n_space(self):
        _temp_nums1 = []
        _ptr_to_nums1 = 0
        _ptr_to_nums2 = 0
        index = 0

        while _ptr_to_nums1 < self._m and _ptr_to_nums2 < self._n:
            self._work[0] += 1

            num1 = self._nums1[_ptr_to_nums1]
            num2 = self._nums2[_ptr_to_nums2]

            if num1 < num2:
                _temp_nums1.append(num1)
                _ptr_to_nums1 += 1
                index += 1
            else:
                _temp_nums1.append(num2)
                _ptr_to_nums2 += 1
                index += 1

        while _ptr_to_nums1 < self._m:
            self._work[0] += 1
            _temp_nums1.append(self._nums1[_ptr_to_nums1])
            _ptr_to_nums1 += 1
            index += 1

        while _ptr_to_nums2 < self._n:
            self._work[0] += 1
            _temp_nums1.append(self._nums2[_ptr_to_nums2])
            _ptr_to_nums2 += 1
            index += 1

        for i in range(len(self._nums1)):
            self._work[0] += 1
            self._nums1[i] = _temp_nums1[i]

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    #########################################
    def _n_time_constant_space(self):

        if len(self._nums2) == 0:
            return
        _ptr_to_nums1 = self._m - 1
        _ptr_to_nums2 = self._n - 1
        index = self._m + self._n - 1

        while index != 0 and _ptr_to_nums1 >= 0 and _ptr_to_nums2 >= 0:
            self._work[0] += 1

            num1 = self._nums1[_ptr_to_nums1]
            num2 = self._nums2[_ptr_to_nums2]

            if num2 >= num1:
                self._nums1[index] = num2
                _ptr_to_nums2 -= 1
            elif num2 <= num1:
                self._nums1[index] = num1
                _ptr_to_nums1 -= 1

            index -= 1

        while _ptr_to_nums2 >= 0:
            self._work[0] += 1
            num2 = self._nums2[_ptr_to_nums2]
            self._nums1[index] = num2
            _ptr_to_nums2 -= 1
            index -= 1
