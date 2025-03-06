class HashTable:

    def __init__(self, size=13):
        self.size = size
        self.count = 0
        self.table = [None] * self.size

    def hash(self, key):
        return sum(ord(c) for c in key) % self.size

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
        if self.count > self.size * 0.7:
            self._resize()

        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return
            index = (index + 1) % self.size

        self.table[index] = key
        self.count += 1

    def find(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size
        return False


def taking_text(line, hash_table):
    word = ""
    for l in line:
        if 'a' <= l <= 'z':
            word += l
        elif word:
            hash_table.add(word)
            word = ""
    if word:
        hash_table.add(word)


def main():
    n, m = map(int, input().split())

    dict = HashTable()
    text = HashTable()

    for i in range(n):
        word = input().lower()
        dict.add(word)

    for i in range(m):
        line = input().lower()
        taking_text(line, text)

    not_in_dict = False
    not_in_text = False

    for word in text.table:
        if word is not None and not dict.find(word):
            not_in_dict = True
            break

    if not not_in_dict:
        for word in dict.table:
            if word is not None and not text.find(word):
                not_in_text = True
                break

    if not_in_dict:
        print("Some words from the text are unknown.")
    elif not_in_text:
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")


if __name__ == "__main__":
    main()
