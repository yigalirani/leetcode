# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from viztree import *
def read_tokens(s):
    def push_token():
        ans.append((int(''.join(acum_num)),acum_depth))
    ans=[]
    in_num=True
    acum_num=[]
    acum_depth=0
    for c in s:
        if in_num:
            if c!='-':
                acum_num.append(c)
            else:
                push_token()
                acum_depth=1
                acum_num=[]
                in_num=False
        else:
            if c=='-':
                acum_depth+=1
            else:
                in_num=True;
                acum_num=[c]
    push_token()
    return ans
def calc(tokens,pos,depth):#->return tree, new_pos
    if pos>=len(tokens):
        return None,pos
    tval,tdepth=tokens[pos]
    if tdepth!=depth:
        return None,pos
    ans=TreeNode(tval)
    ans.left,right_pos=calc(tokens,pos+1,depth+1)
    ans.right,ans_pos=calc(tokens,right_pos,depth+1)
    return ans,ans_pos
class Solution:
    def recoverFromPreorder(self, S):
        tokens=read_tokens(S)
        print(tokens)
        return calc(tokens,0,0)[0]
t=Solution().recoverFromPreorder("1-2--3--4-5--6--7")
drawtree(t)
