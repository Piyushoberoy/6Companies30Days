#PROBLEM STATEMENT:-
#You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

#LINK:-
#https://leetcode.com/problems/evaluate-reverse-polish-notation/

#CODE:-
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        F = []
        for a in tokens:
            if a == "+":
                n1 = int(F.pop())
                n2 = int(F.pop())
                F.append(int(n1+n2))
            elif a=="-":
                n1 = int(F.pop())
                n2 = int(F.pop())
                F.append(int(n2-n1))
            elif a == "/":
                n1 = int(F.pop())
                n2 = int(F.pop())
                F.append(int(n2/n1))
            elif a=="*":
                n1 = int(F.pop())
                n2 = int(F.pop())
                F.append(int(n1*n2))
            else:
                F.append(int(a))
        return F.pop()
        
#DATA STRUCTURE USED:-
#STACK
