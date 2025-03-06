EMPTY = "EMPTY"
DELETED = "DELETED"

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class HashTable:

    def __init__(self, size=11):
        self.size = size
        self.count = 0
        self.hash_table = [[EMPTY, EMPTY] for _ in range(self.size)]

    def hash(self, key):
        author, title = key
        merg = author + title
        hash_val = 0

        for l in merg:
            hash_val = (hash_val * 31 + ord(l)) % self.size
        return hash_val

    def _rehash(self):
        old_table = self.hash_table
        old_size = self.size
        self.size = old_size * 2 + 1

        while not is_prime(self.size):
            self.size += 2
        self.hash_table = [[EMPTY, EMPTY] for i in range(self.size)]

        for key in old_table:
            if key[0] not in (EMPTY, DELETED):
                self.addBook(key[0], key[1])

    def addBook(self, author, title):
        if self.count > self.size * 0.7:
            self._rehash()

        key = (author, title)
        idx = self.hash(key)

        while self.hash_table[idx][0] not in (EMPTY, DELETED):
            if self.hash_table[idx] == [author, title]:
                return
            idx = (idx + 1) % self.size

        self.hash_table[idx] = [author, title]
        self.count += 1

    def find(self, author, title):
        key = (author, title)
        idx = self.hash(key)

        while self.hash_table[idx][0] != EMPTY:
            if self.hash_table[idx] == [author, title]:
                return title
            idx = (idx + 1) % self.size
        return None

    def delete(self, author, title):
        key = (author, title)
        idx = self.hash(key)

        while self.hash_table[idx][0] != EMPTY:
            if self.hash_table[idx] == [author, title]:
                self.hash_table[idx] = [DELETED, DELETED]
                self.count -= 1
                return
            idx = (idx + 1) % self.size

    def findByAuthor(self, author):
        books = [key[1] for key in self.hash_table
                 if key[0] == author and key[1] != DELETED]
        return sorted(books)



hash_table: HashTable

def init():
    global hash_table
    hash_table = HashTable()

def addBook(author, title):
    hash_table.addBook(author, title)

def find(author, title):
    return hash_table.find(author, title) is not None

def delete(author, title):
    hash_table.delete(author, title)

def findByAuthor(author):
    return hash_table.findByAuthor(author)


#RESULT:
#[...................................................................................................]
#Score: 100%
