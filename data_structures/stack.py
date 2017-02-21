"""

    Stack
    -----

    A stack or LIFO (last in, first out) is an abstract data type that serves
    as a collection of elements, with two principal operations: push, which
    adds an element to the collection, and pop, which removes the last element
    that was added.

"""

class Stack(list):

    def __init__(self, max_size=None):
        super(Stack, self).__init__()
        self.max_size = max_size

    #TODO : to call "add" instead ?
    def push(self, x):
        """
        Add element in the stack

        :param x: undefined | Element to add
        :return: self | Stack with new element added at the end
        """
        if self.is_full():
            #TODO : check what error to raise ?
            print("Cannot add element. Stack is full. Risk of overflow.")
            pass

        self.append(x)

    # TODO : to call "remove" instead ?
    def pop(self):
        """
        Remove last element added from the stack
        :return: self | Stack  with last element removed
        """
        self.pop()

    def is_empty(self):
        """
        Checks if the stack is empty

        :return: boolean | True if the stack is empty, False otherwise
        """
        return len(self) == 0

    def is_full(self):
        """
        Checks if the stack is full

        :return: boolean | True if stack is full, False otherwise
        """
        if self.max_size is None:
            print("No maximum size has been set to the stack.")
            return False
        return len(self) == self.max_size

    def peek(self):
        """
        Get the top data element of the stack, without removing it.

        """
        return self[-1]
