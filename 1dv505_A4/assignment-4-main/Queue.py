from LinkedList import LinkedList


class Queue:
    def __init__(self):
        self.__elements = LinkedList()

    def enqueue(self, e):
        self.__elements.add(e)

    def dequeue(self):
        if self.getSize() == 0:
            return None
        else:
            return self.__elements.removeAt(0)

    def getSize(self):
        return self.__elements.getSize()

    def __str__(self):
        return self.__elements.__str__()

    def isEmpty(self):
        return self.getSize() == 0