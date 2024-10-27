import random
import string
import time

class Node:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hashFunction(self, key):
        return abs(hash(key) % self.size)

    def insert(self, isbn, title):
        index = self.hashFunction(isbn)
        new_node = Node(isbn, title)
        
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while True:
                if current.isbn == isbn:
                    current.title = title
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def lookup(self, isbn):
        index = self.hashFunction(isbn)
        current = self.table[index]
        
        while current is not None:
            if current.isbn == isbn:
                return current.title
            current = current.next
        
        return None

    def delete(self, isbn):
        index = self.hashFunction(isbn)
        current = self.table[index]
        previous = None
        
        while current is not None:
            if current.isbn == isbn:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        
        return False

    def display(self):
        for index in range(self.size):
            current = self.table[index]
            if current:
                print(f"Index {index}: ", end="")
                while current:
                    print(f"({current.isbn}, {current.title}) -> ", end="")
                    current = current.next
                print("None")

def generate_isbn():
    return ''.join(random.choices(string.digits, k=13))

def measure_insertion_time(size):
    hash_table = HashTable(size)
    start_time = time.time()

    for _ in range(size):
        isbn = generate_isbn()
        title = f"Book {isbn[-1]}"
        hash_table.insert(isbn, title)

    end_time = time.time()
    print(f"Insertion time for {size} records: {end_time - start_time:.6f} seconds")

def measure_lookup_time(size):
    hash_table = HashTable(size)
    
    for _ in range(size):
        isbn = generate_isbn()
        title = f"Book {isbn[-1]}"
        hash_table.insert(isbn, title)

    start_time = time.time()

    for _ in range(size):
        isbn = random.choice([node.isbn for index in range(hash_table.size) if hash_table.table[index] for node in iterate_nodes(hash_table.table[index])])
        hash_table.lookup(isbn)

    end_time = time.time()
    print(f"Lookup time for {size} records: {end_time - start_time:.6f} seconds")

def iterate_nodes(node):
    while node:
        yield node
        node = node.next

def measure_deletion_time(size):
    hash_table = HashTable(size)
    
    for _ in range(size):
        isbn = generate_isbn()
        title = f"Book {isbn[-1]}"
        hash_table.insert(isbn, title)

    start_time = time.time()

    for index in range(size):
        isbn = random.choice([node.isbn for index in range(hash_table.size) if hash_table.table[index] for node in iterate_nodes(hash_table.table[index])])
        hash_table.delete(isbn)

    end_time = time.time()
    print(f"Deletion time for {size} records: {end_time - start_time:.6f} seconds")

def main():
    sizes = [10, 100, 1000]

    for size in sizes:
        print(f"\nTesting with {size} records:")
        measure_insertion_time(size)
        measure_lookup_time(size)
        measure_deletion_time(size)

if __name__ == "__main__":
    main()
