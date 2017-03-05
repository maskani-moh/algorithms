"""

    Queue
    -----

    A queue is a particular kind of abstract data type or collection in which
    the entities in the collection are kept in order and the only
    operations on the collection are the addition of entities to the rear
    terminal position, known as enqueue, and removal of entities from the front
    terminal position, known as dequeue. This makes the queue a
    First-In-First-Out (FIFO) data structure.

    source: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)

"""

class Queue:

    def __init__(self, l=None):
        """
        Constructor

        :param l: list | initial queue
        """
        if l is None:
            self.queue = list()
        else:
            self.queue = l

    def __str__(self):
        return "{}".format(self.queue)

    def enqueue(self, x):
        """
        Add element in the Queue

        :param x: undefined | Element to add
        :return: self | Queue with new element added at the end
        """
        self.queue.append(x)

    def dequeue(self):
        """
        Remove the first element enqueued that is still in the queue

        :return: self | Queue with first element removed
        """

        def _pop_left(l):
            l_ = l[::-1]  # inverse the elements of the list
            l_.pop()
            return l_[::-1]

        self.queue = _pop_left(self.queue)

    def is_empty(self):
        """
        Checks if the queue is empty

        :return: boolean | True if self.queue is empty, False otherwise
        """
        return len(self.queue) == 0

    def size(self):
        """
        Gets size of the queue

        :return: int | Size of the queue
        """
        return len(self.queue)

    def peek(self):
        """
        Get the value at the beginning of the queue

        :return:
        """
        return self.queue[0]
