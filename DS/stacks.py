#LL implement

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self._size = 0


    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        data = self.top.value
        self.top = self.top.next
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack Overflow")
        return self.top.value

    def is_empty(self):
        return self.top == None

    def size(self):
        return self._size

    def __repr__(self):
        items, curr = [], self.top
        while curr:
            items.append(str(curr.value))
            curr = curr.next
        return "TOP -> " + " -> ".join(items) + " -> None"



def is_balanced(s):
    match = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for ch in s:
        if ch in '([{':
            stack.push(ch)
        elif ch in ')]}':
            if stack.is_empty() or stack.pop() != match[ch]:
                return False
    return stack.is_empty()


def reverse_string(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)
    return "".join(stack.pop() for _ in range(stack.size()))


def evaluate_postfix(expression):
    """Evaluate a postfix (RPN) expression.  O(n)
    Example: '3 4 + 2 *' → 14
    """
    stack = Stack()
    for token in expression.split():
        if token.lstrip('-').isdigit():
            stack.push(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            if token == '+': stack.push(a + b)
            elif token == '-': stack.push(a - b)
            elif token == '*': stack.push(a * b)
            elif token == '/': stack.push(int(a / b))
    return stack.pop()



s = Stack()
for v in [1,51,6,1,6,16,565,7541,7,51,614,61,36,7,51,6, 2, 3]:
    s.push(v)
print(s)                          # TOP -> 3 -> 2 -> 1 -> None
print(s.peek())                   # 3
print(s.pop())                    # 3
print(s)                          # TOP -> 2 -> 1 -> None

print(is_balanced("({[]})"))      # True
print(is_balanced("({[})"))       # False

print(reverse_string("hello"))    # olleh

print(evaluate_postfix("3 4 + 2 *"))  # 14