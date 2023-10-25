############################################################
# L0322.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################
import sys
############################################################
# All imports
###########################################################
from typing import List
from time import process_time


class Solution:
    ## YOU CANNOT CHANGE THIS INTERFACE
    ## LEETCODE INTERFACE
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## YOU CANNOT CHANGE ANYTHING IN THIS PROCEDURE
        work = [0]
        changes = []  # If change cannot be given, you must put -1 in changes[0]
        show = False
        p = L0322(coins, amount, changes, work, show)
        num_change = len(changes)
        if (num_change == 1):
            if (changes[0] == -1):
                num_change = -1
        return num_change


class L0322:
    def __init__(self, coins: List[int], amount: 'int', changes: 'list of int', work: 'List of size 1',
                 show: 'boolean'):
        # NOTHING CAN BE CHANGED
        self._d = coins
        self._n = amount
        self._ans = changes
        self._work = work
        self._show = show
        # YOU MUST GENERATE V table and k table
        self._v = []
        self._k = []
        # You can have any number of data structures here
        # MUST WRITE TWO ROUTINES
        self._alg()
        self._get_solution()

    def _increment_work(self):
        self._work[0] = self._work[0] + 1

    ############################################################
    # WRITE CODE BELOW
    ###########################################################

    ############################################################
    # TIME (n * k ) = O(n)
    # SPACE O(n)
    ############################################################
    def _alg(self):
        # print("self._n", self._n)
        # print("self._d", self._d)
        for i in range(self._n + 1):
            # print("Start")
            v, k = self._calculate_change(i)
            # print("Final v,k ", v, k)
            # print("for", i)
            # print()
            self._v.append(v)
            self._k.append(k)

    def _calculate_change(self, amount: "int") -> ["int", "int"]:
        if amount == 0:
            return 0, 0

        k = v = sys.maxsize

        for i in range(len(self._d)):
            # print("amount", amount)
            # print("self._d[i]", self._d[i])
            if amount - self._d[i] >= 0:
                self._increment_work()
                if self._v[amount - self._d[i]] == -1:
                    continue
                temp_v = self._v[amount - self._d[i]] + 1
                temp_k = self._d[i]
                # print("amount", amount)
                # print("i", i)
                # print("self._d[i]", self._d[i])
                # print("temp_v", temp_v)
                # print("temp_k", temp_k)
                # print(temp_v < v)

                if temp_v < v:
                    v = temp_v
                    k = temp_k
                    # print(v,k)
        # print(v, k)
        if k == sys.maxsize:
            return -1, -1
        return v, k

    ############################################################
    # NOTHING CAN BE CHANGED IN THIS ROUTINE BELOW
    ###########################################################
    def _get_solution(self):
        if (self._show):
            a = []
            for i in range(self._n + 1):
                a.append(i)
            print(a)
            print(self._v)
            print(self._k)
        if (self._n < 1000):
            for i in range(self._n + 1):
                if (self._show):
                    print("minimum change for", i, "cents can be achieved using", self._v[i], "coins.")
                self._get_solution1(i)
        else:
            self._get_solution1(self._n)

    ############################################################
    # TIME O(n)
    # SPACE THETA(1)
    # How will you give change for p cents
    # WRITE CODE BELOW
    ############################################################
    def _get_solution1(self, p: 'int'):
        # print(self._v)
        # print(self._k)
        self._ans.clear()
        while p != 0:
            if self._k[p] == -1:
                self._ans.append(-1)
                break
            self._ans.append(self._k[p])
            p -= self._k[p]
        # print(self._ans)
