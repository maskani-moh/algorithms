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

class Queue(list):

    def __init__(self):
        super(Queue, self).__init__()
        # TODO : use deque from 'collections' module
        # TODO : add max_size parameter ?

    def enqueue(self, x):
        """
        Add element in the Queue

        :param x: undefined | Element to add
        :return: self | Queue with new element added at the end
        """
        self.append(x)

    # TODO : complete
    def dequeue(self):
        """
        Remove the first element enqueued that is still in the queue

        :return: self | Queue with first element removed
        """

        def _pop_left(l):
            l_ = l[::-1]  # inverse the elements of the list
            l_.pop()
            return l_[::-1]

        return self

    def is_empty(self):
        pass

    def size(self):
        pass

    def peek(self):
        pass
