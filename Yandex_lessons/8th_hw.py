class Node():
    def __init__(self, val, par = None):
        self._left : Node = None
        self._right : Node = None
        self._p : Node = par
        self._val = val

    def find(self, v):
        if v == self._val:
            return self
        elif v > self._val:
            if self._right == None:
                return -1
            return self._right.find(v)
        else:
            if self._left == None:
                return -1
            return self._left.find(v)

    def add(self, v):
        if v == self._val:
            return None
        elif v > self._val:
            if self._right == None:
                self._right = Node(v, par=self)
            else:
                self._right.add(v)
        else:
            if self._left == None:
                self._left = Node(v, par=self)
            else:
                self._left.add(v)

    def height(self):
        if self._left == None:
            if self._right == None:
                return 0
            else:
                return 1 + self._right.height()
        elif self._right == None:
            return 1 + self._left.height()
        else:
            return max(1 + self._left.height(), 1 + self._right.height())
    
    def node_height(self, v):
        if v == self._val:
            return 1
        elif v > self._val:
            return 1 + self._right.node_height(v)
        else:
            return 1 + self._left.node_height(v)

    def __str__(self):
        if self._left == None:
            if self._right == None:
                return f"|{self._val}|"
            else:
                return f"{self._val}->{self._right}"
        else:
            if self._right == None:
                return f"{self._left}<-{self._val}"
            else:
                return f"{self._left}<-{self._val}->{self._right}"

    def max(self):
        if self._right == None:
            return self._val
        else: 
            return self._right.max()

    def second_max(self):
        if self._right == None:
            if self._left == None:
                if self._p == None:
                    return self._left.max()
                else:
                    return self._p._val
            else:
                return self._left.max()
        else:
            return self._right.second_max()

    def go_inc(self):
        if self._left != None:
            self._left.go_inc()
        print(self._val)
        if self._right != None:
            self._right.go_inc()

def task_A():
    inp = "7 3 2 1 9 5 4 6 8 0"
    arr = list(map(int, inp.split()))
    head = Node(arr[0])
    for x in arr:
        head.add(x)

    # print(head)
    print(head.height())

def task_B():
    arr = list(map(int, input().split()))
    head = Node(arr[0])
    nums = set()
    nums.add(arr[0])

    ans = ['1']
    for x in arr:
        if x not in nums and x != 0:
            head.add(x)
            nums.add(x)
            ans.append(str(head.node_height(x)))
    print(' '.join(ans))

def task_C():
    # inp = "7 3 2 1 9 5 4 6 8 0"
    # arr = list(map(int, inp.split()))
    arr = list(map(int, input().split()))
    head = Node(arr[0])
    for x in arr[:-1]:
        head.add(x)

    print(head.second_max())

def task_D():
    # inp = "7 3 2 1 9 5 4 6 8 0"
    # arr = list(map(int, inp.split()))
    arr = list(map(int, input().split()))
    head = Node(arr[0])
    for x in arr[:-1]:
        head.add(x)

    head.go_inc()

task_D()