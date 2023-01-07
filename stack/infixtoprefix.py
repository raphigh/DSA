class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[-1]
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def print(self):
        print(self.item)

def isOperator(c):
    return c in ["+",'-','*',"/","^"]

def isalpha(c):
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= "Z"):
        return True
    else:
        return False

def isdigit(c):
    if (c >= '0' and c <= '9'):
        return True
    return False

def getPriority(c):
    if (c == '-') or (c == "+"):
        return 1
    elif (c== "*") or (c == "/"):
        return 2
    elif (c == "^"):
        return 3
    return 0


def infixToPostfix(infix):
    infix = "(" + infix + ")"
    l = len(infix)
    char_stack = Stack()
    output = ""
    for i in range(l):
        if(isalpha(infix[i]) or isdigit(infix[i])):
            output += infix[i]
        elif(infix[i] == "("):
            char_stack.push("(")
        elif(infix[i] == ")"):
            while(char_stack.top() != "("):
                output += str(char_stack.top())
                char_stack.pop()
            char_stack.pop()
        else:
            if(isOperator(char_stack.top())):
                while(getPriority(infix[i]) <= getPriority(char_stack.top())):
                    output += str(char_stack.top())
                    char_stack.pop()
            char_stack.push(infix[i])
    return output



def infixToPrefix(infix):
    l = len(infix)
    char_stack = Stack()
    rinfix = ""

    for k in range((l-1),-1,-1):
        rinfix += infix[k]
    infix = ""

    for i in range(l):
        if rinfix[i] == "(":
            infix += ")"
        elif rinfix[i] == ")":
            infix += "("
        else:
            infix += rinfix[i]

    Prefix = infixToPostfix(infix)
    l = len(Prefix)
    rprefix = ""
    for k in range((l-1),-1,-1):
        rprefix = rprefix + Prefix[k]
    return rprefix

print(infixToPostfix("A+(B*C)"))



