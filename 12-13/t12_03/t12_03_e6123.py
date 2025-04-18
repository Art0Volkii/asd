class Node:
    def __init__(self, item, next_node=None):
        self.item = item
        self.next = next_node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        self.top = self.push_rec(item, self.top)
        return "ok"

    def push_rec(self, item, curr):
        if curr is None:
            return Node(item)
        else:
            return Node(item, curr)

    def pop(self):
        if self.top is not None:
            item = self.top.item
            self.top = self.top.next
            return item
        else:
            return "error"

    def back(self):
        if self.top is not None:
            return self.top.item
        else:
            return "error"

    def size(self):
        return self.size_rec(self.top)

    def size_rec(self, curr):
        if curr is None:
            return 0
        else:
            return 1 + self.size_rec(curr.next)

    def clear(self):
        self.top = self.__init__()
        return "ok"

def main():
    s = Stack()
    while True:
        try:
            command = input().strip()
        except: break

        if command.startswith("push"):
            _, num = command.split()
            print(s.push(int(num)))
        elif command == "pop":
            print(s.pop())
        elif command == "back":
            print(s.back())
        elif command == "size":
            print(s.size())
        elif command == "clear":
            print(s.clear())
        elif command == "exit":
            print("bye")
            break

if __name__ == "__main__":
    main()

#RES: 100%
