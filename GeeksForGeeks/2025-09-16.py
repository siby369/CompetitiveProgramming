"""
Problem: Evaluate Postfix Expression
Difficulty: Medium
Link: https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1

Approach:
- Use a stack to evaluate the postfix expression.
- Traverse each token in the input array:
  - If it is an operand, convert it to an integer and push it to the stack.
  - If it is an operator (+, -, *, /, ^):
    - Pop the top two elements from the stack.
    - Apply the operator with correct operand order (second popped element as left operand, first popped as right operand).
    - Push the result back to the stack.
- At the end, the stack will contain a single element which is the final result.

Time Complexity: O(n), where n = number of tokens in the postfix expression.
Space Complexity: O(n), for the stack used to store operands during evaluation.
"""

class Solution:
    def evaluatePostfix(self, arr):
        st=[]
        for z in arr:
            if z=="+":
                a=st.pop()
                b=st.pop()
                st.append(b+a)
            elif z=="-":
                a=st.pop()
                b=st.pop()
                st.append(b-a)
            elif z=="*":
                a=st.pop()
                b=st.pop()
                st.append(b*a)
            elif z=="/":
                a=st.pop()
                b=st.pop()
                st.append(int(b/a))
            elif z=="^":
                a=st.pop()
                b=st.pop()
                st.append(pow(b,a))
            else:
                st.append(int(z))
        return st[-1]
