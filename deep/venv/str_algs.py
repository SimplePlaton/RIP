n = 'hello, world'
print(n[::-1])



def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = "hello, world"
print("The reversed string(using loops) is : ", end="")
print(reverse(s))

def srez(s):
    s = s[::-1]
    return s


s ='hello, world'
print(srez(s))


def recurse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

s ='hello, world'
print(recurse(s))


# Function to create an empty stack. It
# initializes size of stack as 0
def createStack():
    stack = []
    return stack


# Function to determine the size of the stack
def size(stack):
    return len(stack)


# Stack is empty if the size is 0
def isEmpty(stack):
    if size(stack) == 0:
        return true

    # Function to add an item to stack . It


# increases size by 1
def push(stack, item):
    stack.append(item)


# Function to remove an item from stack.
# It decreases size by 1
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()


# A stack based function to reverse a string
def reverse(string):
    n = len(string)

    # Create a empty stack
    stack = createStack()

    # Push all characters of string to stack
    for i in range(0, n, 1):
        push(stack, string[i])

        # Making the string empty since all
    # characters are saved in stack
    string = ""

    # Pop all characters of string and put
    # them back to string
    for i in range(0, n, 1):
        string += pop(stack)

    return string


# Driver code
s = "hello, world"
print(reverse(s))