# ── Stack (Array / List implementation) ──────────────────────────────────────


class Stack:

    def __init__(self):
        self._data = []         

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop() 

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]    

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        items = [str(x) for x in reversed(self._data)]
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
    n = stack.size()
    return "".join(stack.pop() for _ in range(n))


def is_palindrome(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)
    for ch in s:
        if stack.pop() != ch:
            return False
    return True


def evaluate_postfix(expression):
    """Evaluate a postfix (RPN) expression.
    Example: '3 4 + 2 *' -> 14
    Tokens must be space-separated.
    """
    stack = Stack()
    for token in expression.split():
        if token.lstrip('-').isdigit():
            stack.push(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            if   token == '+': stack.push(a + b)
            elif token == '-': stack.push(a - b)
            elif token == '*': stack.push(a * b)
            elif token == '/': stack.push(int(a / b))
    return stack.pop()


def infix_to_postfix(expression):
    """Convert infix to postfix using the Shunting Yard algorithm.
    Supports: + - * / ^ and parentheses ( )
    Tokens must be space-separated.
    Example: '3 + 4 * 2' -> '3 4 2 * +'
    """
    precedence  = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_assoc = {'^'}
    stack  = Stack()
    output = []

    for token in expression.split():
        if token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            if stack.is_empty():
                raise ValueError("Mismatched parentheses: extra ')'")
            stack.pop()
        elif token in precedence:
            while (not stack.is_empty()
                   and stack.peek() in precedence
                   and (precedence[stack.peek()] > precedence[token]
                        or (precedence[stack.peek()] == precedence[token]
                            and token not in right_assoc))):
                output.append(stack.pop())
            stack.push(token)
        else:
            output.append(token)

    while not stack.is_empty():
        op = stack.pop()
        if op == '(':
            raise ValueError("Mismatched parentheses: extra '('")
        output.append(op)

    return " ".join(output)



def menu():
    print("\n\t\t----------------------------------------")
    print("\n\t\t1. Push to Stack")
    print("\n\t\t2. Pop from Stack")
    print("\n\t\t3. Peek Top of Stack")
    print("\n\t\t4. Display Stack / Size")
    print("\n\t\t5. Extra Functions")
    print("\n\t\t6. Quit")
    print("\n\t\t----------------------------------------")
    print("\n\t\tYour choice please: ", end="")


def extra_menu(s):
    print("\n\t\t  --- Extra Functions ---")
    print("\n\t\t  a. Check Balanced Brackets")
    print("\n\t\t  b. Reverse a String")
    print("\n\t\t  c. Check Palindrome")
    print("\n\t\t  d. Evaluate Postfix Expression")
    print("\n\t\t  e. Convert Infix to Postfix")
    print("\n\t\t  Choice: ", end="")
    sub = input().strip().lower()

    if sub == 'a':
        print("\n\t\tEnter expression (e.g. ({[]})): ", end="")
        expr = input().strip()
        result = is_balanced(expr)
        print(f"\n\t\t'{expr}' is {'BALANCED' if result else 'NOT balanced'}!")

    elif sub == 'b':
        print("\n\t\tEnter string to reverse: ", end="")
        string = input().strip()
        print(f"\n\t\tReversed: '{reverse_string(string)}'")

    elif sub == 'c':
        print("\n\t\tEnter string to check: ", end="")
        string = input().strip()
        result = is_palindrome(string)
        print(f"\n\t\t'{string}' is {'a palindrome' if result else 'NOT a palindrome'}!")

    elif sub == 'd':
        print("\n\t\tEnter postfix expression (space-separated, e.g. 3 4 + 2 *): ", end="")
        expr = input().strip()
        try:
            result = evaluate_postfix(expr)
            print(f"\n\t\tResult: {result}")
        except Exception as e:
            print(f"\n\t\tError: {e}")

    elif sub == 'e':
        print("\n\t\tEnter infix expression (space-separated, e.g. 3 + 4 * 2): ", end="")
        expr = input().strip()
        try:
            result = infix_to_postfix(expr)
            print(f"\n\t\tPostfix: '{result}'")
        except Exception as e:
            print(f"\n\t\tError: {e}")

    else:
        print("\n\t\tInvalid sub-option!")


def main():
    s = Stack()

    while True:
        menu()
        try:
            choice = int(input().strip())
        except ValueError:
            print("\n\t\tWrong input! Please enter 1-6.")
            continue

        if choice == 1:
            print("\n\t\tEnter value to push: ", end="")
            value = input().strip()
            s.push(value)
            print(f"\n\t\t'{value}' pushed to the stack successfully!")

        elif choice == 2:
            try:
                val = s.pop()
                print(f"\n\t\t'{val}' popped from the stack!")
            except IndexError:
                print("\n\t\tStack is EMPTY! Nothing to pop.")

        elif choice == 3:
            try:
                print(f"\n\t\tTop of stack: '{s.peek()}'")
            except IndexError:
                print("\n\t\tStack is EMPTY!")

        elif choice == 4:
            if s.is_empty():
                print("\n\t\tStack is EMPTY!")
            else:
                print(f"\n\t\t{s}")
                print(f"\n\t\tSize: {s.size()}")

        elif choice == 5:
            extra_menu(s)

        elif choice == 6:
            print("\n\t\tYou decided to QUIT\n\n\t\tBYE!\n")
            break

        else:
            print("\n\t\tWrong input! Please enter 1-6.")

main()