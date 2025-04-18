class Node:
    def __init__(self, item, next_node=None):
        self.item = item
        self.next = next_node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        if self.top is not None:
            item = self.top.item
            self.top = self.top.next
            return item
        else:
            return None

    def back(self):
        if self.top is not None:
            return self.top.item
        else:
            return None

    def clear(self):
        self.top = self.__init__()

def function(n, a):
    station = Stack()
    next = 1
    index = 0
    while index < n:
        while next <= n and (station.back() != a[index]):
            station.push(next)
            next += 1
        if station.back() == a[index]:
            station.pop()
            index += 1
        else:
            return False
    return True

def main():
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                continue
            lines.append(line.strip())
        except: break

    i = 0
    while i < len(lines):
        if lines[i] == "0":
            break
        n = int(lines[i])
        i += 1
        while i < len(lines) and lines[i] != "0":
            permutation = list(map(int, lines[i].split()))
            if function(n, permutation):
                print("Yes")
            else:
                print("No")
            i += 1
        print()
        i += 1

if __name__ == "__main__":
    main()

#RES: 100%
