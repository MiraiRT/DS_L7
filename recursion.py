class node:
    def __init__(self, data, next=None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next


def work(n):
    if n == 1:
        print('do work', n)
    elif n < 0:
        return 'Failed'
    else:
        print('do work', n)
        work(n - 1)


def printNdown(n):
    if n == 1:
        print(n)
    elif n < 0:
        return 'Failed'
    else:
        print(n)
        printNdown(n - 1)


def printToN(n):
    if n == 1:
        print(n)
    elif n < 0:
        return 'Failed'
    else:
        printToN(n - 1)
        print(n)


def sumToN(n):
    sum = 0
    if n == 1:
        sum = sum + n
    elif n < 0:
        return 'Failed'
    else:
        sum = sumToN(n - 1) + n
    return sum


def printfw(l, i):
    if i < len(l):
        print(l[i], end='')
        printfw(l, i + 1)
    else:
        print()


def printbw(l, i):
    if i < len(l):
        printbw(l, i + 1)
        print(l[i], end='')
    else:
        print()


def append1toN(l, n):
    if n == 1:
        l.append(n)
    elif n < 0:
        return 'Failed'
    else:
        append1toN(l, n - 1)
        l.append(n)
    return l


def appendNto1(l, n):
    if n == 1:
        l.append(n)
    elif n < 0:
        return 'Failed'
    else:
        l.append(n)
        appendNto1(l, n - 1)
    return l


def printList(h):
    if h != None:
        print(h.data, end=' ')
        printList(h.next)


def createList(h, n):
    if n > 0:
        p = node(n, h)
        p = createList(p, n - 1)
        return p
    else:
        return h


def createListfromPythonList(h, i):
    global list
    if i >= 0:
        p = node(list[i], h)
        p = createListfromPythonList(p, i - 1)
        return p
    else:
        return h


list = [1, 1, 1, 4]
h = None
l = createListfromPythonList(h, len(list) - 1)
printList(l)
