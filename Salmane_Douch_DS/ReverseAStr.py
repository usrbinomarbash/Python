def reverseStr(mystr):
    lst = list(mystr)
    rev=""
    while(lst):
        b=lst.pop()
        print("Last element popped: "+b)
        rev+=b
    return rev
print(reverseStr("apple"))

def pushToAStack(el, the_stack):
    the_stack+=[el]
    print(the_stack)

def isPalindrome(mystr):
    stack_toPush=[]
    for ch in mystr:
        stack_toPush.append(ch)
    for ch in mystr:
        if ch != stack_toPush.pop():
            print("NotPalindrom")
            return False
    return True
        
print(isPalindrome("omaamo"))
