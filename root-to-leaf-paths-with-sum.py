# Python program to find if there is a root to sum path

import copy
# A binary tree node 
class Node:
  def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
""" 
 Given a tree and a sum, return true if there is a path from the root
 down to a leaf, such that adding up all the values along the path
 equals the given sum.
  
 Strategy: subtract the node value from the sum when recurring down,
 and check to see if the sum is 0 when you run out of tree.
"""
# s is the sum

class Solution:
    def pathSum(self, A, B):
        if not A : return
        self.result = []
        self.allpath(A, B, [])
        return self.result
    def allpath(self,node,s,list,):
            ans = 0
            subSum = s - node.val
            list.append(node.val)
            if(subSum == 0 and node.left == None and node.right == None):
                self.result.append(copy.deepcopy(list))
            if node.left is not None:
                    self.allpath(node.left,subSum, list)
            if node.right is not None:
                    self.allpath(node.right,subSum, list)
            list.pop()
 
