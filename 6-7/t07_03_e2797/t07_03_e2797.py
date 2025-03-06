class HashTable:
    def __init__(self, size=13):
        self.size = size
        self.count = 0
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def is_prime(self, n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def _resize(self):
        old_table = self.table
        new_size = self.size * 2 + 1

        while not self.is_prime(new_size):
            new_size += 2

        self.size = new_size
        self.table = [None] * self.size
        self.count = 0

        for key in old_table:
            if key is not None:
                self.add(key)

    def add(self, key):
        if self.count >= self.size * 0.7:
            self._resize()

        index = self.hash(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return
            index = (index + 1) % self.size
            if index == start_index:
                return

        self.table[index] = key
        self.count += 1

    def get(self, key):
        index = self.hash(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size
            if index == start_index:
                return
        return False

def main():
    n = input()
    numbers = list(map(int, input().strip().split()))

    hash_table = HashTable()

    for number in numbers:
        hash_table.add(number)

    print(hash_table.count)


if __name__ == "__main__":
    main()
